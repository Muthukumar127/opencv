import cv2
import matplotlib.pyplot as plt
image_path = "cat.jpg"
image = cv2.imread(image_path)
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
scale_factor = 0.8
for i in range(6):
    position = [1, 2, 3, 4, 5, 7][i]
    new_width = int(rgb_img.shape[1] * scale_factor ** i)
    new_height = int(rgb_img.shape[0] * scale_factor ** i)
    resized_image = cv2.resize(rgb_img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    plt.subplot(3, 3, position)
    plt.imshow(resized_image)
    plt.axis("off")
plt.tight_layout()
plt.show()
