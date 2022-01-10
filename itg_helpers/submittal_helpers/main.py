from coverSheets2Pdf import printWorksheets
from utils import getLocalFileNames, removeFilesWith, sortFileNames
from pdfMerger import merge_pdfs


if __name__ == '__main__':
    # # step 1: print all cover sheets to pdf
    # srcFileName = 'C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet-PLC2-network.xlsx'
    dstDirName = 'C:\\Users\\cmolina\\Downloads\\submittal\\Cover-Sheet'
    # printWorksheets(srcFileName, dstDirName)

    # # step 2: remove .xlsx files
    # removeFilesWith(dstDirName)

    # # step 3: merge all pdf files into a single file
    files = getLocalFileNames('C:\\Users\\cmolina\\Downloads\\v4')
    sortedFiles = sortFileNames(files)
    merge_pdfs(sortedFiles, output='C:\\Users\\cmolina\\Downloads\\v4\\submittal v2.pdf')

