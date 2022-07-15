from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (400,400), "black")
idraw = ImageDraw.Draw(img)
other_towns = ImageFont.truetype("arial.ttf", size = 20)
main_towns = ImageFont.truetype("arial.ttf", size = 30)

khabarovsk = "Khabarovsk"
moscow = "Moscow"
cest = "CEST"
edt = "EDT"
yekaterinburg = "Yekaterinburg"

idraw.text((260,50), khabarovsk, font = other_towns)
idraw.text((30,50), moscow, font = other_towns)
idraw.text((40,300), cest, font = other_towns)
idraw.text((300,300), edt, font = other_towns)
idraw.text((100,150), yekaterinburg, font = main_towns)
img.save("start.png")
img.show()
