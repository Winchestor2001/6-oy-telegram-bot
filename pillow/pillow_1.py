from PIL import Image, ImageDraw, ImageFont

img = Image.open('../photos/3. Леопард.jpg')
# print(dir(img))
# print(img.format)
# print(img.size)
# print(img.mode)
# print(img.show())

draw = ImageDraw.Draw(img)
text = "Leopard"
font = ImageFont.truetype('BebasNeue-Regular.ttf', 100)
draw.text((800, 10), text, font=font, fill='#6EBF26')
img.show()












