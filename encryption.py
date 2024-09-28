import base64


def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)
    return encoded_bytes


user_password = input("Enter password: ")
passwd = encrypt_pass(user_password)


def decode_pass(password):
    decoded_bytes = base64.b64decode(password)
    decode_data = decoded_bytes.decode()
    print(f"Decoded data: {decode_data}")


decode_pass(passwd)
