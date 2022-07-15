from PIL import Image, ImageFont, ImageDraw
from os import remove
class pick:
    def __init__(self):
        self.other_towns = ImageFont.truetype("arial.ttf", size = 20)
        self.main_towns = ImageFont.truetype("arial.ttf", size = 30)
        #self.hours = [i for i in range(24)]

    def create_time(self, h,min):
        #k,m,c,e,y
        try:
            #Если есть такой файл, удаляем
            remove("time.png")
        except:
            pass
        self.new_pick = Image.open("start.png")
        self.new_idraw = ImageDraw.Draw(self.new_pick)
        k = h + 5 if h <= 18 else h - 19
        self.new_idraw.text((285,80), str(k) + " : " + min, font = self.other_towns)
        m = h - 2 if h >= 2 else h + 22
        self.new_idraw.text((35,80), str(m) + " : " + min, font = self.other_towns)
        c = h - 3 if h >= 3 else h + 21
        self.new_idraw.text((35,330), str(c) + " : " + min, font = self.other_towns)
        e = h + 15 if h <= 9 else h - 9
        self.new_idraw.text((290,330), str(e) + " : " + min, font = self.other_towns)
        self.new_idraw.text((150,200),str(h) + " : " + min, font = self.main_towns)
        self.new_pick.save("time.png")

#a = pick()
#a.create_time(21,"04")
#a.img.show()
