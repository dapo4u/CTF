import base64

def decode_base64(data):
    """Decode a Base64 encoded string."""
    decoded_data = base64.b64decode(data).decode('utf-8')
    return decoded_data

def decode_file(file_path):
    """Read and decode a Base64 encoded file."""
    with open(file_path, 'r') as file:
        data = file.read()

    iteration = 0
    while True:
        try:
            print(f"Decoding iteration: {iteration}")
            decoded_data = decode_base64(data)
            data = decoded_data
            iteration += 1
        except Exception as e:
            print("Decoding complete or an error occurred.")
            break

    print("Final Decoded Data:\n", data)

if __name__ == "__main__":
    file_path = 'enc_flag'  # Replace with your file path if different
    decode_file(file_path)



