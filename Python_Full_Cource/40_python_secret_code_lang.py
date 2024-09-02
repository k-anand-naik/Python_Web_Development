import random
import string

def encode_word(word):
    if len(word) >= 3:
        # Remove the first letter and append it to the end
        encoded = word[1:] + word[0]
        # Append three random characters at the start
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        encoded = random_chars + encoded
        return encoded
    else:
        # Reverse the string if it has less than 3 characters
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        # Reverse the string if it has less than 3 characters
        return word[::-1]
    else:
        # Remove the first three random characters
        decoded = word[3:]
        # Remove the last letter and move it to the beginning
        decoded = decoded[-1] + decoded[:-1]
        return decoded

def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

# Example usage
message = "hello world"
encoded_message = encode_message(message)
decoded_message = decode_message(encoded_message)

print("Original Message:", message)
print("Encoded Message:", encoded_message)
print("Decoded Message:", decoded_message)
