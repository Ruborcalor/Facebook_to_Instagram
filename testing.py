#!/usr/bin/env python3
import math
from wand.image import Image
from wand.color import Color


photo_path = "gogo.jpg"

with Image(filename=photo_path) as img:
    image_size = str(img.size)
    aspects = str(image_size[image_size.find("(") + 1: image_size.find(")")]).split(",")
    aspects = [float(aspect) for aspect in aspects]
    aspect_ratio = (aspects[0]) / (aspects[1])

    if aspect_ratio < 0.8:
        #img.transform(resize="{0}x{1}".format(int(0.8 * aspects[1]), aspects[1]))

        #crop_height = int(aspects[1] - math.ceil(aspects[0] / 0.8))
        w_bor = int(math.ceil(aspects[1] * 0.8) - aspects[0])
        #img.crop(0, math.ceil(crop_height / 2), int(aspects[0]), int(aspects[1] - math.ceil(crop_height / 2) - 1))
        print(w_bor)

        img.border(color=Color('transparent'), width=w_bor, height=0)


        #img.save(filename=photo_path)
        img.save(filename="new_photo")



    if aspect_ratio > 1.91:
        img.transform(resize="{0}x{1}".format(aspects[0], int(aspects[0] / 1.91)))
        #crop_width = int(aspects[0] - math.ceil(aspects[1] * 1.91))
        h_bor = int((math.ceil(aspects[0] / 1.91) - aspects[1]) / 2)
        #img.crop(math.ceil(crop_width / 2), 0, int(aspects[0] - math.ceil(crop_width / 2) - 1), int(aspects[1]))

        print(h_bor)
        img.border(color=Color('transparent'), width=0, height=h_bor)

        #img.save(filename=photo_path)
        img.save(filename="new_photo")

        if aspect_ratio < 0.8:
            crop_height = int(aspects[1] - math.ceil(aspects[0] / 0.8))
            w_bor = int(math.ceil(aspects[0] * 0.8) - aspects[1])
            #img.crop(0, math.ceil(crop_height / 2), int(aspects[0]), int(aspects[1] - math.ceil(crop_height / 2) - 1))

            img.border(color=Color('transparent'), width=w_bor, height=0)


            img.save(filename=photo_path)



        if aspect_ratio > 1.91:
            crop_width = int(aspects[0] - math.ceil(aspects[1] * 1.91))
            h_bor = int((math.ceil(aspects[0] / 1.91) - aspects[1]) / 2)
            #img.crop(math.ceil(crop_width / 2), 0, int(aspects[0] - math.ceil(crop_width / 2) - 1), int(aspects[1]))
            img.border(color=Color('transparent'), width=0, height=h_bor)

            img.save(filename=photo_path)

#def adjust_ratio(img, w_dst, h_dst):
#
#    img.transform(resize="{0}x{1}".format(w_dst,h_dst))
#
#    w_bor = (w_dst - self.img.width) / 2
#    h_bor = (h_dst - self.img.height) / 2
#
#    if w_bor > 0:
#        img.border(color=Color('transparent'),width=w_bor,height=0)
#    else:
#        img.border(color=Color('transparent'),width=0,height=h_bor)
#
#with Image(filename=in_file) as foreground:
#    foreground.transform(resize="{0}x{1}".format(width, height))
#    with Image(width=width, height=height, background=Color('white')) as out:
#        left = (width - foreground.size[0]) / 2 
#        top = (height - foreground.size[1]) / 2 
#        out.composite(foreground, left=left, top=top) 
#        out.save(filename=out_file) 



