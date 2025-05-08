def encode_image(image_path, secret_message, output_path):
    from PIL import Image

    # Load the image
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size

    # Convert the secret message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    binary_message += '1111111111111110'  # Delimiter to indicate end of message

    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                pixel = list(encoded_image.getpixel((x, y)))
                # Modify the least significant bit of the red channel
                pixel[0] = pixel[0] & ~1 | int(binary_message[data_index])
                encoded_image.putpixel((x, y), tuple(pixel))
                data_index += 1
            else:
                break

    # Save the encoded image
    encoded_image.save(output_path)


def decode_image(image_path):
    from PIL import Image

    # Load the image
    image = Image.open(image_path)
    binary_message = ""
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            # Extract the least significant bit of the red channel
            binary_message += str(pixel[0] & 1)

            # Check for the delimiter
            if binary_message[-16:] == '1111111111111110':
                # Return the decoded message
                message = ""
                for i in range(0, len(binary_message) - 16, 8):
                    byte = binary_message[i:i + 8]
                    message += chr(int(byte, 2))
                return message

    return None  # No message found