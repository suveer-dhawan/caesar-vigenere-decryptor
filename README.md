Markdown

# Caesar and Vigenère Decryptor

---

Welcome to the **Caesar and Vigenère Decryptor**! This project is my first significant endeavor into the world of Python programming, showcasing a practical application of foundational cryptographic concepts. It's designed to decrypt messages encoded with both the classic Caesar cipher and the more advanced Vigenère cipher.

## 🌟 Features

* **Intelligent Cipher Detection:** The program automatically determines whether to use Caesar or Vigenère decryption based on the type of key provided. If the key is numeric, it's treated as a Caesar shift; if it's alphanumeric, it's used as a Vigenère keyword.
* **Caesar Cipher Decryption:** Easily decrypt messages encrypted with a Caesar cipher by providing the numerical shift key.
* **Vigenère Cipher Decryption:** Decipher messages encoded with a Vigenère cipher, requiring the original keyword.
* **Intuitive Command-Line Interface:** A user-friendly interface guides you through the decryption process, making it simple to input the necessary information.
* **Robust Error Handling:** Designed to gracefully handle invalid inputs, ensuring a smooth user experience.

## 🛠️ Technologies Used

* **Python 3:** The core language used for developing the decryption logic.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need Python 3 installed on your system. If you don't have it, you can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/suveer-dhawan/caesar-vigenere-decryptor.git](https://github.com/suveer-dhawan/caesar-vigenere-decryptor.git)
    ```

2.  **Navigate into the project directory:**

    ```bash
    cd caesar-vigenere-decryptor
    ```

### How to Run

1.  **Execute the `decryptor.py` script:**

    ```bash
    python decryptor.py
    ```

2.  **Follow the on-screen prompts:**
    * Enter your encrypted message.
    * Provide the decryption key. The program will automatically apply either Caesar or Vigenère decryption based on whether the key is numeric or a word.

## 💡 Example Usage

### Caesar Cipher Decryption (with a numerical key)

```
DECRYPT STRING
Input encrypted string: KHOOR ZRUOG
Input key: 3
The decrypted string is:
HELLOWORLD
```

### Vigenère Cipher Decryption (with a word key)

```
DECRYPT STRING
Input encrypted string: RPDQHV GDB
Input key: LEMON
The decrypted string is:
EXAMPLEONE
```

## 🧠 How it Works

The project intelligently implements the decryption algorithms for both ciphers:

* **Automatic Key Detection:** The `decrypt_cypher` function inspects the provided key. If it's purely numeric, it's converted to an integer and passed to the `caesar_cypher` function. Otherwise, it's treated as a string keyword and passed to the `vigenere_cipher` function.
* **Caesar Cipher:** Each letter in the ciphertext is shifted back a fixed number of positions down the alphabet. For example, with a shift of 3, 'D' would become 'A'.
* **Vigenère Cipher:** A polyalphabetic substitution cipher that uses a keyword. Each letter of the plaintext is encrypted using a different Caesar cipher determined by the corresponding letter of the keyword. Decryption reverses this process using the same keyword.

---

## 🤝 Contributing

As this is my first significant Python project, I'm eager for feedback and suggestions! If you have ideas for improvements, new features, or find any bugs, please feel free to:

* **Open an issue:** Describe the bug or suggest an enhancement.
* **Fork the repository:** Make your changes and submit a pull request.

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📞 Contact

Have questions or want to connect? You can reach me at:

[Suveer Dhawan](https://github.com/suveer-dhawan)
