from PIL import ImageColor
from PIL import Image

print ImageColor.getcolor('red', 'RGBA')

catIm = Image.open('zophie.png')
# print catIm.size
# print catIm.filename
# print catIm.format
# print catIm.format_description
# catIm.save('zophie.jpg')
# catIm.rotate(90).save('rotated90.png')
#
# croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')

catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560))
print faceIm.size
#
# catCopyIm.paste(faceIm, (0, 0))
# catCopyIm.paste(faceIm, (400, 500))
# catCopyIm.save('pasted.png')

# catImWidth, catImHeight = catIm.size
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()
# for left in range(0, catImWidth, faceImWidth):
#     for top in range(0, catImHeight, faceImHeight):
#         print(left, top)
#         catCopyTwo.paste(faceIm, (left, top))
# catCopyTwo.save('tiled.png')

# catIm.rotate(6).save('rotated6.png')
# catIm.rotate(6, expand=True).save('rotated6_ _expanded.png')
#
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_ _flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_ _flip.png')

im = Image.new('RGBA', (100, 100))
print im.getpixel((0, 0))

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))
from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
print im.getpixel((0, 0))

print im.getpixel((0, 50))

im.save('putPixel.png')
