def calculate_width(aspect_ratio, height):
    # Calculate width using the aspect ratio tuple (width, height) and given height
    width = (aspect_ratio[0] / aspect_ratio[1]) * height
    return width

def calculate_height(aspect_ratio, width):
    # Calculate height using the aspect ratio tuple (width, height) and given width
    height = (aspect_ratio[1] / aspect_ratio[0]) * width
    return height