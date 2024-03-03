import calories_list

Total_calories = []
# Function to sum Total_calories
def sum_total_calories():
    return round(sum(Total_calories),2)

# Function to empty the Total_calories list
def reset_total_calories():
    Total_calories.clear()


def Calories_Calculator(x1, y1, x2, y2, name):
    calori_item_mili = calories_list.calories.get(name)
    # if calori_item_mili is None:
    #   print('no element found')
    #  return 0
    # return 0
    box_width = x2 - x1
    box_height = y2 - y1
    num_squares_width = box_width / 3.78
    num_squares_height = box_height / 3.78
    total_squares = num_squares_width * num_squares_height
    total_calories = total_squares * calori_item_mili[0] * calori_item_mili[1] * 0.1
    Total_calories.append(total_calories)
    return round(total_calories,2)
