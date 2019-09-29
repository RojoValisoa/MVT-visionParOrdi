import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir =  os.path.join(BASE_DIR, "images")

y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ","-").lower()
            print(label,path)
            # y_labels.append(label)
            # x_train.append(path)
            pil_minage  = Image.open(path).convert("L")
            image_array = np.array

