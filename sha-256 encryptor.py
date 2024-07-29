import hashlib

def sha256_encrypt(text):
    #   Creating a SHA-256 hash object.
    sha256_hash = hashlib.sha256()
    #   Updating the hash object with the bytes of the text.
    sha256_hash.update(text.encode('utf-8'))
    #   Getting the hexadecimal representation of the hash.
    encrypted_text = sha256_hash.hexdigest()
    return encrypted_text

if __name__ == "__main__":
    text_to_encrypt = "Enter your raw data to encryption here."
    encrtpted_text = sha256_encrypt(text_to_encrypt)
    print(f"Original text: {text_to_encrypt}")
    print(f"SHA-256 encrypted text: {encrtpted_text}")