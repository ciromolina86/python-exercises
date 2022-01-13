import os.path
import time

from PyPDF4 import PdfFileReader, PdfFileWriter
from utils import *
from excelHandler import *


def merge_pdfs(srcFileNames, dstFileName):
    pdf_writer = PdfFileWriter()

    for path in srcFileNames:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(dstFileName, 'wb') as out:
        pdf_writer.write(out)

    os.startfile(dstFileName)


def split_pdf(fileName, dstDirName):
    if not isDirectory(dstDirName):
        createDirectory(dstDirName)

    _dir, _file = os.path.split(fileName)
    _file, _ext = os.path.splitext(_file)

    pdf_reader = PdfFileReader(fileName)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(fileName)

        # Add each page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
        with open(f'{dstDirName}\\{_file}---{page}{_ext}', 'wb') as out:
            pdf_writer.write(out)

    os.startfile(dstDirName)


def rename_pdfs(srcDirName: str, newNames: list):
    fileNames = sortFileNames(getLocalFileNames(srcDirName), by=getNumberTail)

    if len(fileNames) == len(newNames):
        for i in range(len(fileNames)):
            _dir, _file = os.path.split(fileNames[i])
            _, _ext = os.path.splitext(_file)

            renameFile(fileNames[i], os.path.join(_dir, newNames[i]+_ext))
    else:
        print(f"files and names lengths don't match")

    os.startfile(dstDirName)


if __name__ == '__main__':
    coverSheetsPath = 'C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet'
    submittalPath = 'C:\\Users\\cmolina\\Downloads\\submittal'

    # merge_pdfs(srcFileNames=sortFileNames(fileNames=getLocalFileNames(coverSheetsPath),
    #                                       by=getNumberHead),
    #            dstFileName=f'{submittalPath}\\cover sheets merged.pdf')

    # split_pdf(fileName='C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet-PLC3-network.pdf',
    #           dstDirName='C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet')

    # print(getSheetNames('C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet-PLC3-network.xlsx'))

