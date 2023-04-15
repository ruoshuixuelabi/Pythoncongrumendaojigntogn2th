import glob
import os

from pdf2docx import Converter

dirname = "D:\pdfdata\pdfdata"
pdf_file = 'D:/25ef90547aba4d03b41bc9aa15b747ac.pdf'
docx_file = 'D:/25ef90547aba4d03b41bc9aa15b747ac111.docx'
path = r'D:\pdfdata\pdfdata\*'
file_list = glob.glob(path)

for root, dirs, files in os.walk(dirname):
    for file in files:
        path = os.path.join(root, file)
        if path.__contains__("pdfdata"):
            print(path)
            cv = Converter(path)
            cv.convert(path + ".docx")
            cv.close()

# for file in file_list:
# print(file)
# cv = Converter(file)
# cv.convert(file+".docx")
# cv.close()
# convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file)      # all pages by default
# cv.close()
