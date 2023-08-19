# RSA Encrypter/Decrypter

This program mostly useful for who studies computer engineering or computer science. I used this program at my discrete math midterm. It might be useful for anyone I think. Feel free to use my code.

If you dont have an idea about RSA Encrypt or Decryption, check this link https://en.wikipedia.org/wiki/RSA_(cryptosystem)

# Instructions
For encryption:

- Choose a 4-letter word (like HELP [doesn't matter if you type with upper or lowercase])
- Choose two distinct prime numbers (p and q [like 59 and 43])
- Compute n Key = p*q (2537)
- Choose a number between 1 and lcm((p-1), (q-1)) that coprime to lcm((p-1), (q-1)) (like 13) 
- Enter the word and all these numbers into the program
- After pressed Encrypt button you'll see the Encrypted Text below the button


![Screenshot 2023-08-10 130328](https://github.com/Metrohan/RSA-EncrypterDecrypter/assets/54481595/0a171192-7728-4baa-960d-2196a39566ec)



For decryption:

- Enter the encrypted word
- Enter the numbers same as encryption part
- After pressed Decrypt button you'll see the Decrypted Text below the button


![Screenshot 2023-08-10 130347](https://github.com/Metrohan/RSA-EncrypterDecrypter/assets/54481595/8ccf185c-bc4c-40ff-8403-2f2d71642a48)



# Notes

Unfortunately, this program supports max 4-letter words. After entering longer than 4-letter words, the program doesn't correctly encrypt your word.


