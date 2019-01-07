import csv
import os
import json
import math

def ReadConfig(filePath):
    with open(filePath) as json_data_file:
        data = json.load(json_data_file)
        return data

def ReadCSV(filePath):
    result = []
    with open(filePath) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            # line = {
            #     'Username': row['Username'],
            #     'Password': row['Password'],
            #     'Organisation Id': row['Organisation Id'],
            #     'Organisation Unit Id': row['Organisation Unit Id'],
            #     'Organisation Unit Name': row['Organisation Unit Name'],
            #     'Main Role Id': row['Main Role Id']
            # }
            line = {
                'Username': row['Username'],
                'Password': row['Password']
            }
            result.append(line)
    return result

def WrireCSV(filePath, data):
    with open(filePath, mode='w') as csv_file:
        #fieldnames = ['Username', 'Password', 'Organisation Id', 'Organisation Unit Id', 'Organisation Unit Name', 'Main Role Id']
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def EnsureCreateDirectory(pathDirectory):
    if not os.path.exists(pathDirectory):
        os.makedirs(pathDirectory)

def GroupList (list, numberOfGroup):
    countGroup = numberOfGroup
    it = iter(list)
    result = [[{}]]
    result_Divide = [[next(it) for _ in range(countGroup)]
              for _ in range(len(list) // countGroup)]
    for index, x in enumerate(it):
        result_Divide[index].append(x)

    result.extend(result_Divide)
    # for exclude_Divide in range((len(list) // countGroup), len(list)):
    #     #     result.append(list[exclude_Divide])
    #     # print(result)
    return result_Divide

def main():

    config = ReadConfig("config.json")
    print(config)

    inputFile = config["inputFile"] #"StudentImportTemplate.csv"
    rowPerFile = config["rowPerFile"] #500
    rootOutput = config["rootOutput"] #"D:\\test"
    startNumber = config["startNumber"] #50000
    patternDir = config["patternDir"] #"data-{0}"

    try:
        data = ReadCSV(inputFile)
        #print(data[0])
        dataCount = len(data)
        print(f"Data Count: {dataCount}")
        if dataCount > 0:
            numberOfFile = math.ceil(dataCount / rowPerFile)
            print(f"Number Of File {numberOfFile}")
            groupData = GroupList(data, rowPerFile)
            print(f"Group data count: {len(groupData)}")
            for item in range(0, numberOfFile):
                numberDir = startNumber + item
                newDir = patternDir.format(numberDir)
                newDirFullPath = os.path.join(rootOutput, newDir)
                EnsureCreateDirectory(newDirFullPath)
                destFilePath = os.path.join(newDirFullPath, inputFile)
                print(f"Write file CSV: {destFilePath}")
                WrireCSV(destFilePath, groupData[item])

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    main()
