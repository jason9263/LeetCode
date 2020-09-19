import PyPDF2
import matlab.engine

# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('../mor.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(3)
# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())

pdfFileObj.close()
