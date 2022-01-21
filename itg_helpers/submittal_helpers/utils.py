import os
import re


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


def getNumberTail(fileName):
    """

    :param fileName:
    :return:
    """
    _fileName, _ = os.path.splitext(fileName)

    return int(_fileName.split('---')[-1])


def getNumberHead(fileName):
    """

    :param fileName:
    :return:
    """
    idx1 = idx2 = idx3 = idx4 = 0

    match = re.search(r'([0-9]+)\.*([0-9]+)*\.*([0-9]+)*\.*([0-9]+)*', fileName)

    if match:
        idx1, idx2, idx3, idx4 = match.group(1), match.group(2), match.group(3), match.group(4)
        if idx4 is None:
            idx4 = 0
        return int(idx1), int(idx2), int(idx3), int(idx4)
    else:
        return int(idx1), int(idx2), int(idx3), int(idx4)


def sortFileNames(fileNames, asc=True, by=None):
    """

    :param by:
    :param fileNames:
    :param asc:
    :return:
    """
    return sorted(fileNames, key=by, reverse=not asc)


def renameFile(srcFileName, dstFileName):
    """

    :param srcFileName:
    :param dstFileName:
    :return:
    """
    os.rename(srcFileName, dstFileName)


def rename_files(srcDirName: str, newNames: list):
    fileNames = sortFileNames(getLocalFileNames(srcDirName), by=getNumberTail)

    if len(fileNames) == len(newNames):
        for i in range(len(fileNames)):
            _dir, _file = os.path.split(fileNames[i])
            _, _ext = os.path.splitext(_file)

            renameFile(fileNames[i], os.path.join(_dir, newNames[i] + _ext))
    else:
        print(f"files and names lengths don't match")

    os.startfile(srcDirName)


if __name__ == '__main__':
    # fileName = 'C:\\Users\\cmolina\\Downloads\\test spreadsheet.xlsx'
    # dirName, _ = os.path.split(fileName)
    dirName = 'C:\\Users\\cmolina\\Downloads\\submittal\\'

    files = getLocalFileNames(dirName)
    sortedFiles = sortFileNames(files, by=getNumberHead)

    for f in sortedFiles:
        print(f)
