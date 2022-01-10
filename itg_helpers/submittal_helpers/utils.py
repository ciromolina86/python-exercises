import os


def getLocalFileNames(dirName):
    """

    :param dirName:
    :return:
    """

    completeFileList = []

    for file in os.listdir(dirName):
        completePath = os.path.join(dirName, file)

        if os.path.isdir(completePath):
            completeFileList = completeFileList + getLocalFileNames(completePath)
        else:
            completeFileList.append(completePath)

    return completeFileList


def isDirectory(dirName):
    """

    :param dirName:
    :return:
    """
    if os.path.exists(dirName):
        return True
    else:
        return False


def createDirectory(dirName):
    """

    :param dirName:
    :return:
    """
    os.makedirs(dirName)


def removeFilesWith(dirName, suffix='.xlsx'):
    """

    :param dirName:
    :param suffix:
    :return:
    """
    files = getLocalFileNames(dirName)

    for file in files:
        if suffix in file:
            os.unlink(file)


def byFileName(path):
    """

    :param path:
    :return:
    """
    _, fileName = os.path.split(path)

    return fileName


def sortFileNames(fileNames, asc=True):
    """

    :param fileNames:
    :param asc:
    :return:
    """
    return sorted(fileNames, key=byFileName, reverse=not asc)


if __name__ == '__main__':
    # fileName = 'C:\\Users\\cmolina\\Downloads\\test spreadsheet.xlsx'
    # dirName, _ = os.path.split(fileName)
    dirName = 'C:\\Users\\cmolina\\Downloads\\v4'

    files = getLocalFileNames(dirName)
    sortedFiles = sortFileNames(files)
    print(sortedFiles)
