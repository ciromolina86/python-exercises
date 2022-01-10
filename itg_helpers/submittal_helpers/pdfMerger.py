import PyPDF4
from utils import getLocalFileNames
from PyPDF4 import PdfFileReader, PdfFileWriter


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = getLocalFileNames('C:\\Users\\cmolina\\Downloads\\cover sheets')
    merge_pdfs(paths, output='C:\\Users\\cmolina\\Downloads\\cover sheets\\cover sheets merged.pdf')
