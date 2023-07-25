# RSA Encrypter/Decrypter

This program mostly useful for who studies computer engineering or computer science. I used this program at my discrete math midterm. I thought it might be useful for anyone. Feel free to use my code.

If you dont have an idea about RSA Encrypt or Decryption, check this link https://en.wikipedia.org/wiki/RSA_(cryptosystem)

# Instructions
For encryption:

- Choose a 4-letter word (like HELP [doesn't matter if you type with upper or lowercase])
- Choose two distinct prime numbers (p and q [like 59 and 43])
- Compute n Key = p*q (2537)
- Choose a number between 1 and lcm((p-1), (q-1)) that coprime to lcm((p-1), (q-1)) (like 13) 
- Enter the word and all these numbers to the program
- After pressed Encrypt button you'll see the Encrypted Text below the button


![image](https://github.com/Metrohan/RSA-EncrypterDecrypter/assets/54481595/982f20c4-38c2-44d3-b5e3-e19e1b4c553a)


For decryption:

- Enter encrypted word
- Enter the numbers same as encryption part
- After pressed Decrypt button you'll see the Decrypted Text below the button


![image](https://github.com/Metrohan/RSA-EncrypterDecrypter/assets/54481595/33ce92bb-ce7f-4154-b6d1-ced434112a42)


# Notes

Unfortunately, this program supports max 4-letter words. After entering longer than 4-letter words, program doesn't correctly encrypt your word.


