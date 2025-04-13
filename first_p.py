# -*- coding: utf-8 -*-

def caesar_decrypt(ciphertext):
  """
  Decrypts a Caesar cipher encrypted text by trying all possible keys (0-25).

  Args:
    ciphertext: The encrypted text to decrypt (String).

  Returns:
    A dictionary containing the potential key (int) and the corresponding decrypted text (String).
  """
  possible_plaintexts = {} # Dictionary to store possible results
  ALPHABET_SIZE = 26     # English alphabet size

  # Iterate through all possible shift keys (0 to 25)
  # Note: A key of 0 means no shift, resulting in the original ciphertext.
  # Keys 1-25 represent actual shifts.
  for key in range(ALPHABET_SIZE):
    plaintext = "" # The decrypted text for this key
    # Iterate through each character in the ciphertext
    for char in ciphertext:
      if char.isalpha(): # Check if the character is alphabetic
        # Determine the base ('A' for uppercase, 'a' for lowercase)
        start = ord('A') if char.isupper() else ord('a')
        # Calculate the original character before the shift
        # We use % to handle wrapping around the alphabet
        # (ord(char) - start) gets 0-25 position
        # (- key) shifts it back
        # (% ALPHABET_SIZE) handles wrap-around (e.g., 'A' shifted back by 1 becomes 'Z')
        # (+ start) converts back to ASCII code of the correct case
        original_ord = (ord(char) - start - key) % ALPHABET_SIZE + start
        plaintext += chr(original_ord) # Convert ASCII code back to character
      else:
        # If the character is not alphabetic (number, symbol, space), keep it as is
        plaintext += char
    # Store the result with the key used for decryption (which is the tested shift amount)
    possible_plaintexts[key] = plaintext

  return possible_plaintexts

# ----- Example Usage -----

# Encrypted text (Example: "Hello World" encrypted with a shift key of 3)
encrypted_text = "Khoor Zruog"

# Call the function to decrypt
decryption_results = caesar_decrypt(encrypted_text)

# Print all possible results with their keys
print(f"Encrypted text: {encrypted_text}\n")
print("Possible decryption results:")
for key, text in decryption_results.items():
  # Display the key (representing the left shift tried) and the resulting text
  # The 'key' here is the value subtracted during decryption.
  # If the original encryption key was K (shift right),
  # then trying a decryption key K (shift left) will reveal the plaintext.
  print(f"Key (shift left) = {key}: {text}")

# Look through the results for the text that seems logical (usually in English)
# In this example, you will find that key 3 gives "Hello World"