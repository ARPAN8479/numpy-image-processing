import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# -------- FUNCTIONS --------

def to_grayscale(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])


def apply_kernel(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    pad = kh // 2

    padded = np.pad(image, pad, mode='constant')
    output = np.zeros((h, w))

    for i in range(h):
        for j in range(w):
            region = padded[i:i+kh, j:j+kw]
            output[i, j] = np.sum(region * kernel)

    return output


def blur(image):
    kernel = np.ones((3, 3)) / 9
    return apply_kernel(image, kernel)


def edge_detection(image):
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
    return apply_kernel(image, kernel)


# -------- MAIN --------

# Load image
img = Image.open("sample.jpg")
img_array = np.array(img)

# Process
gray = to_grayscale(img_array)
blurred = blur(gray)
edges = edge_detection(gray)

# Show results
plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.title("Grayscale")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Blur")
plt.imshow(blurred, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Edges")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()