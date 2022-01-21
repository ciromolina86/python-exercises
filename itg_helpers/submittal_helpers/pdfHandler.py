import os
import time

from PyPDF4 import PdfFileReader, PdfFileWriter, PdfFileMerger
from utils import *
from excelHandler import *


def merge_pdfs2(srcFileNames, dstFileName):
    pdf_merger = PdfFileMerger()

    for path in srcFileNames:
        _, fileName = os.path.split(path)
        fileName, _ = os.path.splitext(fileName)
        fileName = ' '.join(fileName.split()[1:])

        pdf_merger.append(fileobj=path, bookmark=fileName, pages=None, import_bookmarks=False)

    # Write out the merged PDF
    with open(dstFileName, 'wb') as out:
        pdf_merger.write(out)


def merge_pdfs(srcFileNames, dstFileName):
    pdf_writer = PdfFileWriter()

    for path in srcFileNames:
        _, fileName = os.path.split(path)
        fileName, _ = os.path.splitext(fileName)

        pdf_reader = PdfFileReader(path)

        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

        # if 'coversheet' in fileName.lower():
        fileName = ' '.join(fileName.split()[1:])
        pdf_writer.addBookmark(title=fileName, pagenum=pdf_writer.getNumPages() - 1, parent=None)

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


def add_pdf_bookmark():
    pass


if __name__ == '__main__':
    coverSheetsPath = 'C:\\Users\\cmolina\\Downloads\\submittal\\'
    submittalPath = 'C:\\Users\\cmolina\\Downloads\\submittal\\'

    merge_pdfs2(srcFileNames=sortFileNames(fileNames=getLocalFileNames(coverSheetsPath),
                                           by=getNumberHead),
                dstFileName=f'{submittalPath}bookmark test.pdf')

    # split_pdf(fileName='C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet-PLC3-network.pdf',
    #           dstDirName='C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet')

    # print(getSheetNames('C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet-PLC3-network.xlsx'))
