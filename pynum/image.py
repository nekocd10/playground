import numpy as np
from PIL import Image
import random

# 1. Define image dimensions
width = 512
height = 512

# 2. Generate a 3D NumPy array with random integer values between 0 and 255
# The shape is (height, width, 3) for the R, G, B channels
random_array = np.random.randint(low=0, high=256, size=(height, width, 3), dtype=np.uint8)

# 3. Convert the NumPy array to a Pillow Image object
random_image = Image.fromarray(random_array, 'RGB')

# 4. Save the image to a file
output_filename = "random_image.png"
random_image.save(output_filename, "PNG")

print(f"Random image saved as {output_filename}")

# Optional: display the image
random_image.show()
