def ReadFile(filePath):
    result = []
    file = open(filePath, "r")
    for line in file:
        row = line.rstrip()
        fields = row.split(" ")
        result.append(fields)
    file.close()
    return result

def WriteFile(filePath, lines, isOverride=False):
    if isOverride:
        file = open(filePath, "a")
    else:
        file = open(filePath, "w")
    for line in lines:
        file.write(line + "\n")
    file.close()
