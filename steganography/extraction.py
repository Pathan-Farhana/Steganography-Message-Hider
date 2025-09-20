from PIL import Image

def binary_to_text(binary):
    """Converts a binary string back into a text string."""
    text = ''
    while binary:
        # Take 8 bits (one byte) at a time
        byte = binary[:8]
        # Convert to an integer and then to a character
        text += chr(int(byte, 2))
        # Remove the processed byte
        binary = binary[8:]
    return text

def extract_message(image_path):
    """Extracts a hidden message from an image."""
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image not found.")
        return

    pixels = image.load()
    width, height = image.size
    binary_message = ''
    
    # The stop signal we embedded
    stop_signal = '1111111111111110'

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            for i in range(3):
                # Extract the last bit (the LSB)
                binary_message += str(pixel[i] & 1)
                # Check for our stop signal
                if binary_message.endswith(stop_signal):
                    # Remove the stop signal and return the message
                    final_message = binary_to_text(binary_message[:-16])
                    print("Message extracted successfully!")
                    return final_message
    
    return "No message found."


if __name__ == '__main__':
    # The modified image with the hidden message
    stego_image = 'stego_image.png'
    
    extracted_message = extract_message(stego_image)
    print(f"The secret message is: {extracted_message}")