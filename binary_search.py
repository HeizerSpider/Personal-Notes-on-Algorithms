def binarySearch(item, itemList):
    listsize = len(itemList)-1

    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:

        midPt = (upperIdx+lowerIdx) // 2

        if itemList[midPt] == item:
            return midPt

        if item > itemList[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None





#ordered list
list = [1, 11, 20, 29, 46, 53, 64, 77, 81, 84, 84, 86, 95, 103, 106, 139, 141, 143, 158, 158, 164, 176, 176, 205, 244, 246, 264, 284, 291, 302, 304, 311, 311, 317, 327, 335, 349, 352, 364, 369, 369, 390, 398, 400, 405, 441, 463, 486, 504, 506, 514, 520, 521, 542, 589, 592, 612, 619, 631, 632, 633, 637, 642, 642, 654, 699, 705, 712, 723, 728, 728, 743, 748, 756, 777, 812, 815, 829, 842, 865, 865, 880, 882, 888, 896, 903, 921, 941, 942, 951, 962, 965, 970, 980, 986, 992, 992, 994, 997, 999]
print(binarySearch(103, list))