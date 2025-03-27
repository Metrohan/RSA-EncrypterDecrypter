# RSA Encrypter/Decrypter

This program is particularly useful for students studying Computer Engineering or Computer Science. I originally used it for my Discrete Mathematics midterm, and you're welcome to use or modify the code as needed.

If you're unfamiliar with RSA encryption and decryption, you can learn more here: [RSA Cryptosystem.](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

# Instructions
For encryption:

- Choose a four-letter word (e.g., "HELP" – case does not matter).
- Select two distinct prime numbers, p and q (e.g., 59 and 43).
- Compute the modulus key: n = p × q (e.g., 2537).
- Choose an encryption key, e, that is coprime to lcm(p-1, q-1) and within its range (e.g., 13).
- Enter the word along with these numbers into the program.
- Click the Encrypt button to generate the encrypted text, which will be displayed below.


![Screenshot 2023-08-10 130328](https://github.com/Metrohan/RSA-EncrypterDecrypter/assets/54481595/0a171192-7728-4baa-960d-2196a39566ec)



For decryption:

- Enter the encrypted text.
- Provide the same numbers used in the encryption process.
- Click the Decrypt button to reveal the original text.


![Screenshot 2023-08-10 130347](https://github.com/Metrohan/RSA-EncrypterDecrypter/assets/54481595/8ccf185c-bc4c-40ff-8403-2f2d71642a48)



# Notes
This program currently supports a maximum of four-letter words.
If a word longer than four letters is entered, encryption may not work correctly.

