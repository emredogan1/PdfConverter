from pdf2docx import Converter


pdf_file = "nufus-kayit-ornegi.pdf"
docx_file = "nufus-kayit-ornegi.docx"


# convert pdf to docx

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

