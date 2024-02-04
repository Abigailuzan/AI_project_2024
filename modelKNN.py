import joblib
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model

# Load and preprocess data (same as before)
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


# Feature extraction using MobileNetV2
def extract_features(generator, model):
    features = []
    labels = []
    for i in range(len(generator)):
        x, y = generator[i]
        features.extend(model.predict(x))
        labels.extend(y)
    return np.array(features), np.array(labels)

# Main execution
if __name__ == "__main__":
    train_generator, valid_generator = load_data('annot/train_info.csv', 'annot/val_info.csv', 'train_set/', 'val_set/')

    # Create MobileNetV2 model for feature extraction
    base_model = MobileNetV2(weights='imagenet', include_top=False)
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('out_relu').output)

    # Extract features
    train_features, train_labels = extract_features(train_generator, model)
    val_features, val_labels = extract_features(valid_generator, model)
    train_features = train_features.reshape((train_features.shape[0], -1))
    val_features = val_features.reshape((val_features.shape[0], -1))

    # Flatten the labels
    train_labels = np.argmax(train_labels, axis=1)
    val_labels = np.argmax(val_labels, axis=1)

    # KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=100)
    knn.fit(train_features, train_labels)
    # Save the KNN model
    joblib.dump(knn, 'model/knn_model.sav')

    # Optionally, save the MobileNetV2 model
    #base_model.save('mobilenetv2_feature_extractor.h5')


    # Predict the validation dataset
    val_predicted_classes = knn.predict(val_features)

    # Calculate and print precision, recall, F1-score, and accuracy
    report = classification_report(val_labels, val_predicted_classes, target_names=list(valid_generator.class_indices.keys()))
    accuracy = accuracy_score(val_labels, val_predicted_classes)

    print(report)
    print("Accuracy:", accuracy)
