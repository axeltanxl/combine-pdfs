import PyPDF2
import os

#Change directory to the folder where the PDFs are located (edit folder path)
os.chdir('/home/username/folder')

#Opening the files using PyPDF2 (edit the PDF file names)
pdfFile1 = open('pdf1.pdf','rb')
pdfFile2 = open('pdf2.pdf','rb')
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)
writer = PyPDF2.PdfFileWriter()

#Adding the pages together
for pageNum in range(reader1.numPages):
     page = reader1.getPage(pageNum)
     writer.addPage(page)
 
for pageNum in range(reader2.numPages):
     page = reader2.getPage(pageNum)
     writer.addPage(page)
 
#Creating a new PDF containing the combined PDFs (edit the PDF file name)
outputFile = open('combined.pdf','wb')
writer.write(outputFile)

#Closing the opened files
outputFile.close()
pdfFile1.close()
pdfFile2.close()