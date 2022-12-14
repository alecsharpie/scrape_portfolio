from PIL import Image
import os

base_path = '/Users/alecsharp/me/alecsharpie-me/images/project-icons/'

file_paths = [file for file in os.listdir(base_path) if '.png' in file]

for file in file_paths:
    # Image.open() can also open other image types
    img = Image.open(base_path + file)

    # WIDTH and HEIGHT are integers
    resized_img = img.resize((300, 300), Image.ANTIALIAS)
    resized_img.save(base_path + file)
