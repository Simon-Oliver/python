from PyPDF4 import PdfFileReader

pdfFileObject = open('example.pdf', 'rb')
pdfReader = PdfFileReader(pdfFileObject)
count = pdfReader.numPages
for i in range(count):
    page = pdfReader.getPage(i)
    print(page.extractText())

