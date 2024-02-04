import tensorflow as tf
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report, accuracy_score
import numpy as np


# Load and preprocess data
def load_data(train_csv, val_csv, train_dir, val_dir):
    # Load CSV files with no headers
    train_df = pd.read_csv(train_csv, header=None, names=['image', 'label'])
    val_df = pd.read_csv(val_csv, header=None, names=['image', 'label'])

    # Convert label column to string type
    train_df['label'] = train_df['label'].astype(str)
    val_df['label'] = val_df['label'].astype(str)

    train_datagen = ImageDataGenerator(rescale=1. / 255)
    val_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_dataframe(
        dataframe=train_df,
        directory=train_dir,
        x_col="image",
        y_col="label",
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="categorical",
        target_size=(224, 224))

    valid_generator = val_datagen.flow_from_dataframe(
        dataframe=val_df,
        directory=val_dir,
        x_col="image",
        y_col="label",
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="categorical",
        target_size=(224, 224))

    return train_generator, valid_generator


# Define model architecture
def create_model(num_classes):
    base_model = MobileNetV2(weights='imagenet', include_top=False)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)

    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model



# Main execution
if __name__ == "__main__":
    train_generator, valid_generator = load_data('annot/train_info.csv', 'annot/val_info.csv', 'train_set/', 'val_set/')
    num_classes = len(train_generator.class_indices)  # Get the number of classes
    model = create_model(num_classes)

    # Fit the model
    model.fit(train_generator, validation_data=valid_generator, epochs=10, steps_per_epoch=100, validation_steps=50)

    # Save the model
    model.save('model/food_model.h5')

    # Reset the validation generator
    valid_generator.reset()

    # Predict the validation dataset
    val_predictions = model.predict(valid_generator, steps=np.ceil(len(valid_generator.filenames) / valid_generator.batch_size))
    val_predicted_classes = np.argmax(val_predictions, axis=1)

    # Get the true class indices
    val_true_classes = valid_generator.classes

    # Calculate and print precision, recall, F1-score, and accuracy
    report = classification_report(val_true_classes, val_predicted_classes, target_names=list(valid_generator.class_indices.keys()))
    accuracy = accuracy_score(val_true_classes, val_predicted_classes)

    print(report)
    print("Accuracy:", accuracy)
    model.save('model/food_model1.h5')

