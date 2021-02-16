from PIL import Image, ImageDraw
import math

width = 400
height = 400

image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)

draw.line([(0,0),(150,150), (300,0)], 'black')
draw.rectangle([(130,150), (170,190)], outline='black')
draw.text((150,170), "& | ~", fill='black')
draw.ellipse((100, 100, 150, 200), fill='white', outline='black')

image.save("test.jpg")
