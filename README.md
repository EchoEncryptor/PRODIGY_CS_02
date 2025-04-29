Here's a complete **`README.md`** and project description for your Image Encryption/Decryption Tool using permutation and key-based transformation, which also includes a GUI built with Tkinter:

---

# 🖼️ Image Encryption & Decryption Tool (Python GUI)

## 🔐 Description

This Python project provides a secure and intuitive tool for **image encryption and decryption** using a custom permutation-based algorithm and a user-specified integer key. With a graphical user interface (GUI) built using **Tkinter**, users can easily encrypt or decrypt image files without needing command-line experience.

Encryption is done by:
- Shuffling pixel data using a pseudo-random permutation (seeded with the key),
- Adding the key to pixel values (modulo 256) to further obscure the image.

Decryption reverses the process using the same key.

---

## 🧰 Features

- 📁 **File browser** for selecting input and output image paths.
- 🔑 **Key-based encryption** using integer values.
- 🔄 **Permutation logic** based on seeded pseudo-random number generation.
- 🖼️ Supports **common image formats**: `.png`, `.jpg`, `.jpeg`, `.bmp`
- 🖥️ Clean, responsive **Tkinter GUI**.
- ✅ Non-destructive decryption (restores original image if correct key is used).

---

## 📸 Demo

| Encrypt | Decrypt |
|--------|---------|
| ![Encryption](https://via.placeholder.com/200x150.png?text=Encrypted) | ![Decryption](https://via.placeholder.com/200x150.png?text=Decrypted) |

---

## 🚀 How to Run

### ✅ Requirements

- Python 3.x
- Required packages:
  ```bash
  pip install pillow numpy
  ```

### ▶️ Run the Tool

```bash
python image_cipher_gui.py
```

This will launch a GUI window where you can:
1. Select an image to encrypt or decrypt.
2. Provide an output path for the result.
3. Enter a numeric key.
4. Choose the operation mode (Encrypt or Decrypt).
5. Click **Run** to process the image.

---

## 🧪 How It Works

### 🔐 Encryption Logic:
- Flatten image pixels into a 1D array.
- Generate a permutation using the given key.
- Shuffle the pixels based on this permutation.
- Add the key to pixel values modulo 256.

### 🔓 Decryption Logic:
- Subtract the key from pixel values modulo 256.
- Apply the inverse of the permutation to restore the original order.

---

## 🗂️ File Structure

```
image_cipher_gui.py     # Main script with GUI and logic
```

---

## ⚠️ Notes

- The same key used for encryption **must be used** for decryption.
- Large keys (within 32-bit signed int range) are supported.
- Incorrect keys will result in a distorted image upon decryption.
- This tool is for educational and lightweight obfuscation purposes, not for industrial-grade security.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

Let me know if you'd like a version with **drag-and-drop functionality**, **CLI support**, or integration with other image formats like `.tiff` or `.webp`.
