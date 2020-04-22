from PIL import Image, ImageFilter

img = Image.open('.\pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("blur.png", 'png')

filtered_img.show()