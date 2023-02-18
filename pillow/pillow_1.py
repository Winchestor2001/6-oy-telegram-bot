from PIL import Image, ImageDraw, ImageFont, ImageFilter

img = Image.open('../photos/3. Леопард.jpg')
img2 = Image.open('../photos/10. Цветы.jpg')
img3 = Image.open('../photos/9. Пустыня.jpg')
# print(dir(img))
# print(img.format)
# print(img.size)
# print(img.mode)
# print(img.show())

# draw = ImageDraw.Draw(img)
# text = "Leopard"
# font = ImageFont.truetype('BebasNeue-Regular.ttf', 100)
# draw.text((800, 10), text, font=font, fill='#6EBF26')

# filter_img1 = img.filter(ImageFilter.BLUR)
# filter_img2 = img2.filter(ImageFilter.BoxBlur(100))
# filter_img3 = img.filter(ImageFilter.CONTOUR)
# filter_img4 = img.filter(ImageFilter.DETAIL)
# filter_img5 = img3.filter(ImageFilter.EDGE_ENHANCE)
# filter_img6 = img3.filter(ImageFilter.EDGE_ENHANCE_MORE)
# filter_img7 = img.filter(ImageFilter.EMBOSS)
# filter_img8 = img2.filter(ImageFilter.FIND_EDGES)
# filter_img9 = img.filter(ImageFilter.SHARPEN)
# filter_img10 = img3.filter(ImageFilter.SMOOTH)
# filter_img11 = img.filter(ImageFilter.SMOOTH_MORE)

filter1 = img.filter(ImageFilter.EDGE_ENHANCE)
filter2 = filter1.filter(ImageFilter.EMBOSS)

filter1.show()
filter2.show()

# img.show()
# filter_img5.show()












