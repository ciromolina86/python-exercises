from excelHandler import *
from utils import *
from pdfHandler import *

if __name__ == '__main__':
    coverSheetsPath = 'C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet'
    submittalPath = 'C:\\Users\\cmolina\\Downloads\\submittal'

    # step 1: print all cover sheets to pdf manually
    pass

    # step 2: split the cover sheets pdf file into separate pdf files
    split_pdf(fileName=f'{submittalPath}\\Cover-Sheet-PLC3-network.pdf',
              dstDirName=coverSheetsPath)

    # step 3: rename all the cover sheets pdf with sheet names
    rename_pdfs(srcDirName=coverSheetsPath,
                newNames=getSheetNames(f'{submittalPath}\\Cover-Sheet-PLC3-network.xlsx'))

    # step 4: merge all pdf files into a single file
    sortedFiles = sortFileNames(fileNames=getLocalFileNames(coverSheetsPath),
                                by=getNumberHead)
    merge_pdfs(srcFileNames=sortedFiles,
               dstFileName=f'{submittalPath}\\cover sheets merged.pdf')
