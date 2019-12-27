import PyPDF2

# read file pdf binary
template = PyPDF2.PdfFileReader(open('Nama.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output file
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('Nama2.pdf', 'wb') as file:
    output.write(file)
