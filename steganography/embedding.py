# from PIL import Image

# def text_to_binary(text):
#     """Converts a string of text into a binary string."""
#     return ''.join(format(ord(char), '08b') for char in text)

# def hide_message(image_path, message, output_path):
#     """Hides a message inside an image using LSB steganography."""
#     try:
#         image = Image.open(image_path)
#     except FileNotFoundError:
#         print("Error: Image not found.")
#         return

#     binary_message = text_to_binary(message)
#     # A "stop" signal is crucial for knowing when to end the extraction
#     binary_message += '1111111111111110'  # A unique 16-bit marker

#     pixels = image.load()
#     width, height = image.size
#     message_index = 0

#     for y in range(height):
#         for x in range(width):
#             if message_index < len(binary_message):
#                 pixel = list(pixels[x, y])
#                 for i in range(3):  # Iterate through R, G, B channels
#                     if message_index < len(binary_message):
#                         # Get the original color value
#                         original_value = pixel[i]
#                         # Change the LSB to match the bit from our message
#                         new_value = (original_value & 254) | int(binary_message[message_index])
#                         pixel[i] = new_value
#                         message_index += 1
#                 pixels[x, y] = tuple(pixel)
#             else:
#                 image.save(output_path)
#                 print("Message hidden successfully!")
#                 return

#     image.save(output_path)
#     print("Message hidden successfully!")


# if __name__ == '__main__':
#     # You'll need an image file in the same directory as your script
#     # Use a lossless format like PNG for best results
#     carrier_image = 'carrier_image.png'
#     secret_message = 'This is a top-secret message!'
#     output_image = 'stego_image.png'

#     hide_message(carrier_image, secret_message, output_image)


from PIL import Image

def text_to_binary(text):
    """Converts a string of text into a binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message(image_path, message, output_path):
    """Hides a message inside an image using LSB steganography."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image not found.")
        return

    # Convert the image to RGB mode to ensure it has 3 channels
    if image.mode not in ('RGB', 'RGBA'):
        image = image.convert('RGB')
    
    binary_message = text_to_binary(message)
    # Add a unique 16-bit marker to signal the end of the message
    binary_message += '1111111111111110'

    pixels = image.load()
    width, height = image.size
    message_index = 0

    for y in range(height):
        for x in range(width):
            if message_index < len(binary_message):
                pixel = list(pixels[x, y])
                for i in range(3):  # Iterate through R, G, B channels
                    if message_index < len(binary_message):
                        original_value = pixel[i]
                        # Change the LSB to match the bit from our message
                        new_value = (original_value & 254) | int(binary_message[message_index])
                        pixel[i] = new_value
                        message_index += 1
                pixels[x, y] = tuple(pixel)
            else:
                image.save(output_path)
                print("Message hidden successfully!")
                return

    image.save(output_path)
    print("Message hidden successfully!")

if __name__ == '__main__':
    carrier_image = 'carrier_image.png'
    secret_message = 'This is a top-secret message!'
    output_image = 'stego_image.png'

    hide_message(carrier_image, secret_message, output_image)