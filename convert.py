from PIL import Image

# ASCII characters to represent different shades of gray
ASCII_CHARS = "@%#*+=-:. "

# Resize the image to a smaller width for better ASCII representation
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert a pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert grayscale pixels to ASCII characters
def pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        # Scale the pixel value to fit within the range of ASCII_CHARS
        ascii_str += ascii_chars[pixel_value * (len(ascii_chars) - 1) // 255]
    return ascii_str


# Main function to convert an image to ASCII art
def image_to_ascii(image_path, output_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width=output_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Create a list of strings to represent the ASCII art
    ascii_lines = [ascii_str[index:index+output_width] for index in range(0, len(ascii_str), output_width)]
    ascii_art = "\n".join(ascii_lines)
    
    return ascii_art

if __name__ == "__main__":
    input_image_path = "your_image.jpg"  # Replace with the path to your image
    output_width = 100  # Adjust this value to change the width of the ASCII art

    ascii_art = image_to_ascii(input_image_path, output_width)
    print(ascii_art)
