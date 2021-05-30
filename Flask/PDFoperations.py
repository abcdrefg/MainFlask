from PyPDF2 import PdfFileReader, PdfFileWriter ,PdfFileMerger
from pathlib import Path
import os

rootDir= os.path.dirname(os.path.abspath(__file__))
uploadPath = rootDir +'\\uploadedfiles'


def deletePages(fileID, pageNum):
    infile = PdfFileReader(uploadPath+"\\" + str(fileID) + '.pdf','rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if i != int(pageNum-1):
            p = infile.getPage(i)
            output.addPage(p)

    with open(uploadPath+'\\'+str(fileID)+'.pdf', 'wb') as f:
        output.write(f)

    return "done"

def rotatePages(fileID, pageNum):
    infile = PdfFileReader(uploadPath + "\\" + str(fileID) + '.pdf', 'rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if i != int(pageNum-1):
            p = infile.getPage(i)
            output.addPage(p)
        if i == int(pageNum-1):
            page = infile.getPage(i).rotateClockwise(90)
            output.addPage(page)

    with open(uploadPath+'\\'+str(fileID)+'.pdf', 'wb') as f:
        output.write(f)

    return "done"

def checkNumOfPages(fileID):

    infile = PdfFileReader(uploadPath + "\\" + str(fileID) + '.pdf', 'rb')

    return infile.getNumPages()



