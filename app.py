from utils.steganography import encode_image, decode_image

def main():
    print("Welcome to the Image Steganography Application!")
    choice = input("Would you like to (e)ncode a message or (d)ecode a message? ")

    if choice.lower() == 'e':
        image_path = input("Enter the path to the image: ")
        secret_message = input("Enter the secret message: ")
        encode_image(image_path, secret_message)
        print("Message encoded successfully!")
    elif choice.lower() == 'd':
        image_path = input("Enter the path to the steganographed image: ")
        secret_message = decode_image(image_path)
        print("Decoded message:", secret_message)
    else:
        print("Invalid choice. Please select 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    main()