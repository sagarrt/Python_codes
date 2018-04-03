
## convert image files of directory in binary and save in xls file

import base64
import xlsxwriter
import os, os.path

def save_img_file():
        imgs = []
        path = "."
        valid_images = [".jpg",".gif",".png",".tga"]

        workbook = xlsxwriter.Workbook('Expenses01.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(0,0,'File Name')
        worksheet.write(0,1,'Binary data')

        for f in os.listdir(path):
                ext = os.path.splitext(f)[1]
                if ext.lower() in valid_images:
                        imgs.append(os.path.join(path,f))

        row=1
        for img_file in imgs:
                with open(img_file, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        worksheet.write(row,0,img_file)
                        worksheet.write(row,1,str(encoded_string))
                        row +=1
        workbook.close()


save_img_file()
