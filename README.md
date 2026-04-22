# 🖼️ NumPy Image Processing Toolkit

## 📌 Overview

This project demonstrates basic image processing techniques using **Python and NumPy** without relying on advanced libraries like OpenCV.
It performs operations such as grayscale conversion, blurring, and edge detection using mathematical kernels.

---

## 🚀 Features

* Convert image to **Grayscale**
* Apply **Blur (Smoothing Filter)**
* Perform **Edge Detection (Kernel-based)**
* Display processed images side-by-side
* Save output images

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pillow (PIL)
* Matplotlib

---

## 📂 Project Structure

```bash
numpy-image-processing/
│── main.py
│── sample.jpg
│── gray.jpg
│── blur.jpg
│── edges.jpg
│── output.png
│── README.md
│── requirements.txt
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the program:

```bash
python main.py
```

---

## 📸 Output Screenshots

### 🔹 Application Output

![Output](output.png)

---

## ⚙️ How It Works

* Image is loaded using Pillow
* Converted into NumPy array
* Mathematical operations are applied using kernels:

  * Grayscale → weighted RGB sum
  * Blur → averaging kernel
  * Edge detection → Laplacian kernel
* Results are displayed using Matplotlib

---

## 📈 Future Improvements

* Vectorized convolution (faster performance)
* GUI-based interface
* Additional filters (sharpen, emboss)
* Real-time image processing

---

## 👨‍💻 Author Details

* **Name:** Arpan
* **Registration No:** 251302113
* **Course:** B.Tech CSE (AI & ML)
* **University:** SGT University

---

## ⭐ Note

This project is built for learning purposes to understand how image processing works internally using NumPy.

---
