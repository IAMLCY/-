import pandas as pd

df1 = pd.read_csv("./EpidemicData/EpidemicData-2020-12-16.csv")
df2 = pd.read_csv("./EpidemicData/EpidemicData-2020-12-22.csv")
df3 = pd.read_csv("./EpidemicData/EpidemicData-2020-12-23.csv")
df4 = pd.read_csv("./EpidemicData/EpidemicData-2020-12-24.csv")
df5 = pd.read_csv("./EpidemicData/EpidemicData-2020-12-26.csv")
df6 = pd.read_csv("./EpidemicData/EpidemicData-2020-12-28.csv")

cityList = []
existingList = [[], [], [], [], [], []]
cumulativeList = [[], [], [], [], [], []]
cureList = [[], [], [], [], [], []]
deathList = [[], [], [], [], [], []]

newExisting_Data1 = [[], []]
newExisting_Data2 = [[], []]
newExisting_Data3 = [[], []]
newExisting_Data4 = [[], []]
newExisting_Data5 = [[], []]
newExisting_Data6 = [[], []]
newExisting_DataList = [newExisting_Data1, newExisting_Data2, newExisting_Data3, newExisting_Data4, newExisting_Data5,
                        newExisting_Data6]

existingSum = []


def getDataList():
    cityData = df1.groupby("累计确诊")["地区"]  # 地区

    existingData1 = df1.groupby("地区")["现有确诊"]  # 现有确诊
    # cumulativeData1 = df1.groupby("地区")["累计确诊"]  # 累计确诊
    # cureData1 = df1.groupby("地区")["治愈"]  # 治愈
    # deathData1 = df1.groupby("地区")["死亡"]  # 死亡
    existingData2 = df2.groupby("地区")["现有确诊"]
    existingData3 = df3.groupby("地区")["现有确诊"]
    existingData4 = df4.groupby("地区")["现有确诊"]
    existingData5 = df5.groupby("地区")["现有确诊"]
    existingData6 = df6.groupby("地区")["现有确诊"]

    for i in range(len(cityData)):
        cityList.append(cityData.head()[i])

        existingList[0].append(int(existingData1.head()[i]))
        # cumulativeList[0].append(int(cumulativeData1.head()[i]))
        # cureList[0].append(int(cureData1.head()[i]))
        # deathList[0].append(int(deathData1.head()[i]))
        existingList[1].append(int(existingData2.head()[i]))
        existingList[2].append(int(existingData3.head()[i]))
        existingList[3].append(int(existingData4.head()[i]))
        existingList[4].append(int(existingData5.head()[i]))
        existingList[5].append(int(existingData6.head()[i]))


getDataList()

existing_Data1 = [list(i) for i in zip(cityList, existingList[0])]  # 各地区现有确诊
# cumulative_Data5 = [list(i) for i in zip(cityList, cumulativeList[4])]  # 各地区累计确诊
# cure_Data5 = [list(i) for i in zip(cityList, cureList[4])]  # 各地区治愈
# death_Data5 = [list(i) for i in zip(cityList, deathList[4])]  # 各地区死亡
existing_Data2 = [list(i) for i in zip(cityList, existingList[1])]
existing_Data3 = [list(i) for i in zip(cityList, existingList[2])]
existing_Data4 = [list(i) for i in zip(cityList, existingList[3])]
existing_Data5 = [list(i) for i in zip(cityList, existingList[4])]
existing_Data6 = [list(i) for i in zip(cityList, existingList[5])]

existing_DataList = [existing_Data1, existing_Data2, existing_Data3, existing_Data4, existing_Data5, existing_Data6]


def getNewExistingData():
    for i in existing_DataList:
        for j in i:
            if j[1] != 0:
                newExisting_DataList[existing_DataList.index(i)][0].append(j[0])
                newExisting_DataList[existing_DataList.index(i)][1].append(j[1])


def getExistingSum():
    for i in existingList:
        sum1 = 0
        for j in i:
            sum1 += int(j)
        existingSum.append(sum1)


getNewExistingData()
getExistingSum()

addExisting_DataList = [[], [], [], [], []]


def getAddExisting_DataList():
    try:
        for i in existing_DataList:
            for j in i:
                for k in existing_DataList[existing_DataList.index(i) + 1]:
                    if j[0] == k[0]:
                        addNum = k[1] - j[1]
                        addExisting_DataList[existing_DataList.index(i)].append([j[0], addNum])
    except:
        pass


getAddExisting_DataList()
newAddExisting_DataList = [[[], []], [[], []], [[], []], [[], []], [[], []]]


def getNewAddExisting_DataList():
    for i in addExisting_DataList:
        for j in i:
            if j[1] > 1:
                newAddExisting_DataList[addExisting_DataList.index(i)][0].append(j[0])
                newAddExisting_DataList[addExisting_DataList.index(i)][1].append(j[1])


getNewAddExisting_DataList()

