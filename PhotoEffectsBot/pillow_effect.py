from PIL import Image, ImageFilter


async def make_filter_image(image, img_filter, is_filter):
    img = Image.open(image)
    filtered_img = img.filter(eval(f"ImageFilter.{img_filter}")) if is_filter else img.convert(img_filter)
    filtered_img.save(fp=image)
    return image


