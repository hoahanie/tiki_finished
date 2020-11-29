from TikiTarget import TikiTarget


def getTargetFromFile(fileName):
    TARGET_FILE ='target_list.txt'
    targetFile = open(TARGET_FILE, "r", encoding="UTF8")
    lines =targetFile.readlines()
    targetFile.close()
    targets = []
    n=len(lines)
    i=0
    while i<n:
        newTarget = TikiTarget(lines[i].strip(),lines[i+1].strip())
        # print(newTarget.info())
        targets.append(newTarget)
        i+=2
    return targets
def convertToPrice(strPrice):
    strPrice = strPrice.replace('.','')
    strPrice = strPrice.replace('đ','')
    return int(strPrice)