# 🔐 Secure Text Hiding in Images using Python and OpenCV

This project implements a basic **steganography system** that allows you to hide secret text messages inside an image using XOR encryption and extract them later using the same key. It uses Python and OpenCV for pixel manipulation and works inside Google Colab or any local Python environment.

---

## 🎯 Objective

To securely hide and extract secret text messages inside image files by modifying pixel values, using a user-defined key.

---

## 🛠️ Technologies & Libraries Used

- Python
- OpenCV (`cv2`)
- Google Colab (for cloud-based execution)
- XOR-based encryption logic

---

## 🚀 Features

- Hides any text inside a given image using a key
- Uses RGB pixel values and XOR for basic encryption
- Saves encrypted image to disk (`makeup_encrypted.jpg`)
- Allows secure extraction of the message with the correct key
- Works with `.jpg` or `.png` files

---

## 🧪 How It Works

1. User selects an image and enters a text message to hide
2. Each character is encoded using XOR with a key character
3. Encoded characters are inserted into pixel channels (R/G/B)
4. The modified image is saved and looks visually unchanged
5. The same key can later be used to decrypt and extract the original message

---
## 💡 Example Usage (Colab)

1. Upload `makeup.jpg`
2. Run the code in Colab or any Python IDE
3. Enter a key and the message you want to hide
4. View and save the encrypted image
5. Re-enter the key to extract the hidden message
