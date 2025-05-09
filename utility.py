from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsSimpleTextItem
from PyQt6.QtGui import QColor, QFont


def generate_username(first_name, last_name):
    """
    Generates a username based on the first name and last name.

    Args:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Returns:
        str: The generated username.
    """
    if first_name and last_name:
        username = first_name[0].upper() + last_name.capitalize()
        return username
    else:
        return None  # Return None if either first name or last name is empty



def drawPieChart(scene, values):
    total = sum(values)
    if total == 0:
        return

    # Normalize the values
    normalized_values = [value / total for value in values]

    start_angle = 0
    colors = [QColor(255, 102, 102), QColor(205, 133, 63), QColor(255, 178, 102), QColor(34, 139, 34),
              QColor(102, 255, 102), QColor(128, 128, 0), QColor(102, 255, 255), QColor(102, 178, 255),
              QColor(102, 102, 255), QColor(178, 102, 255), QColor(255, 102, 255)]

    labels = ['Protein', 'Carbohydrates', 'Fats', 'Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D', 'Dietary Fibre',
              'Magnesium', 'Iron', 'Calcium']

    y_position = 20  # Initial y position for legend text

    for value, color, label in zip(normalized_values, colors, labels):
        angle = value * 360
        # Draw the pie slice
        circle = QGraphicsEllipseItem(2, 2, 196, 196)
        circle.setStartAngle(int(start_angle * 16))
        circle.setSpanAngle(int(angle * 16))
        circle.setBrush(color)
        scene.addItem(circle)

        # Add label to legend with percentage
        percentage = "{:.1f}%".format(value * 100)
        legend_text = QGraphicsSimpleTextItem(f"{label} ({percentage})")
        legend_text.setFont(QFont("Arial", 10))
        legend_text.setBrush(color)
        legend_text.setPos(220, y_position)
        scene.addItem(legend_text)

        start_angle += angle
        y_position += 20  # Increment y position for next legend text
