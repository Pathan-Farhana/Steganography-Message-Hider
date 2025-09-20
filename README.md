# Steganography-Message-Hider


### **Steganography Message Hider** 

A Python-based tool for hiding secret messages inside image files using Least Significant Bit (LSB) steganography.

-----

### **Project Description**

This project demonstrates a fundamental concept in **cybersecurity** and **data concealment**. It provides a simple, two-part solution to embed a hidden text message within a standard PNG image and then extract it without any noticeable change to the image's appearance.

-----

### **How It Works**

The tool uses the **Least Significant Bit (LSB)** technique. Each pixel in a color image is represented by three values (Red, Green, Blue). By slightly altering the very last bit of each of these color values, we can store our message's binary data. This change is so minute that it is imperceptible to the human eye.

-----

### **Features**

  * **Message Embedding:** Hides a text message within a carrier image.
  * **Message Extraction:** Retrieves the hidden message from the steganographic image.
  * **Simple & Effective:** Provides a clear demonstration of LSB steganography.
  * **Python-based:** Built using the popular **Pillow** library for image manipulation.

-----

### **Getting Started**

#### **Prerequisites**

  * **Python 3.x**
  * **Pillow** library. You can install it via pip:
    ```bash
    pip install Pillow
    ```

#### **Usage**

1.  **Place your image:** Put a PNG image file in the project's root directory and name it `carrier_image.png`.
2.  **Hide a message:** Run the `embedding.py` script from your terminal:
    ```bash
    python embedding.py
    ```
    This will create a new image file named `stego_image.png` containing your hidden message.
3.  **Extract the message:** Run the `extraction.py` script to reveal the secret message:
    ```bash
    python extraction.py
    ```

-----

### **File Structure**

```
steganography_project/
├── embedding.py        # Script to hide the message
├── extraction.py       # Script to extract the message
├── carrier_image.png   # Your original image file
└── README.md           # This file
```
