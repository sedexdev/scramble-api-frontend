
[![Build Status](https://travis-ci.com/sedexdev/scramble-api-frontend.svg?branch=main)](https://travis-ci.com/sedexdev/scramble-api-frontend)

# Scramble

This repo contains the frontend application code for the Scramble API. 
The API allows you to encrypt text and files quickly and easily. You can 
share encrypted files and text with others by sharing decryption keys to
encrypted content. You can also create key pairs for personal encryption
as well as creating hash digests for passwords and sensitive data. 

# Supported Encryption Methods

<h2>Simple Substitution Cipher</h2>

Either select a shift value for the substitution or ask for a random and
the API will return the shifted plaintext as well as the key mapping for 
decrypting it

<h2>Encryption</h2>

- RSA
- AES

<h2>Hashing</h2>

- MD5*
- BLAKE2b
- BLAKE2s
- PBKDF2-HMAC
- SHA-1*
- SHA-224
- SHA-256
- SHA-384
- SHA-512
- SHA3-224
- SHA3-256
- SHA3-384
- SHA3-512
- SHAKE-128
- SHAKE-256

\* algorithm is deprecated but available for educational purposes

# License

<a href="https://github.com/sedexdev/scramble-api-frontend/blob/main/LICENSE">MIT</a>