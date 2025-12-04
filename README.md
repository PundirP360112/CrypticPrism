# CrypticPrism 

**CrypticPrism** is a web-based image encryption tool featuring a cyberpunk terminal interface. It uses pixel manipulation algorithms to scramble image data into unrecognizable noise based on a numeric security key, allowing users to securely "lock" and "unlock" visual data.

---

## ⚡ Features

* **Dual-Layer Obfuscation:** Combines bitwise XOR operations with pixel shuffling.
* **Symmetric Key System:** Uses a numeric PIN (seed) to generate deterministic random patterns for encryption and decryption.
* **Web Interface:** A responsive, dark-mode "terminal" style UI built with HTML/CSS.
* **Local Processing:** No external databases required; all file processing happens locally on your machine.
* **Instant Download:** Automatically downloads the processed `.png` file upon completion.

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Image Processing:** NumPy, Pillow (PIL)
* **Frontend:** HTML5, CSS3 (Embedded in Python)

## 📋 Prerequisites

Ensure you have **Python 3.x** installed. You will need the following libraries:

* Flask
* NumPy
* Pillow

## 🚀 Installation & Setup

1.  **Clone the repository** (or download the script):
    ```bash
    git clone [https://github.com/yourusername/cryptic-prism.git](https://github.com/yourusername/cryptic-prism.git)
    cd cryptic-prism
    ```

2.  **Install dependencies**:
    ```bash
    pip install flask numpy pillow
    ```

3.  **Run the application**:
    ```bash
    python app.py
    ```

4.  **Access the Interface**:
    Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

## 📖 How to Use

### 🔒 To Encrypt an Image
1.  Click **Choose File** and select an image (JPG, PNG, etc.).
2.  Enter a numeric **Security Key** (e.g., `1234`, `99999`). *Remember this key!*
3.  Click the red **🔒 ENCRYPT** button.
4.  The system will download a scrambled file named `filename_encrypted.png`.

### 🔓 To Decrypt an Image
1.  Upload the previously encrypted image.
2.  Enter the **exact same Security Key** used during encryption.
3.  Click the green **🔓 DECRYPT** button.
4.  The system will reconstruct the original image and download it as `filename_decrypted.png`.

## 🧠 How the Algorithm Works

The system uses `NumPy` for matrix manipulation to perform the following steps:

1.  **Flatten:** The image is converted into a 1D array of pixels.
2.  **Seed:** The numeric user key is used to seed `np.random`, ensuring the "random" pattern is reproducible.
3.  **Shuffle:** A random index array is generated to shuffle the position of every pixel.
4.  **XOR:** Pixel color values are modified using a bitwise XOR operation against the key.

*Decryption simply performs these steps in reverse order to reconstruct the original data.*

## 📂 Directory Structure

When you run the app, it automatically creates two folders in the root directory:
* `/chroma_uploads`: Temporarily stores uploaded files.
* `/chroma_downloads`: Stores the processed images ready for download.

## ⚠️ Disclaimer

This tool is a **visual steganography/obfuscation tool** designed for educational and hobbyist purposes. While the shuffling makes images unreadable to the human eye, it is not a substitute for military-grade cryptographic standards (like AES). Do not use this to secure critical sensitive data (e.g., banking info, passwords).

---

**System Status: ONLINE** // *Session ID: ACTIVE*
