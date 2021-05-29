from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import datetime

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://news.qq.com/zt2020/page/feiyan.htm")

listTitle = []  # ['地区', '现有确诊', '累计确诊', '治愈', '死亡', '疫情']
listData = []


def getTitle():
    tableTitle = driver.find_element_by_xpath('//*[@id="listWraper"]/table[1]')
    tableTitle_data = tableTitle.find_elements_by_xpath('./thead/tr/th')
    for title in tableTitle_data:
        listTitle.append(title.text)


def getData():
    tableData = driver.find_element_by_xpath('//*[@id="listWraper"]/table[2]')
    tbodyData = tableData.find_elements_by_xpath("./tbody")
    for trData in tbodyData:
        areaBox = trData.find_elements_by_xpath('./tr[@class="areaBox"]')
        for data in areaBox:
            listDataText = [data.find_element_by_xpath('.//span').text,
                            data.find_element_by_xpath('./td[1]/p[@class="bold"]').text,
                            data.find_element_by_xpath('./td[2]/p[@class="bold"]').text,
                            data.find_element_by_xpath('./td[3]/p[@class="bold"]').text,
                            data.find_element_by_xpath('./td[4]/p[@class="bold"]').text,
                            data.find_element_by_xpath('./td[5]/p').text,
                            ]
            listData.append(listDataText)


def saveData():
    with open("./EpidemicData/EpidemicData-{}.csv".format(datetime.datetime.now().strftime("%Y-%m-%d")), "w", newline="", encoding="utf-8") as csv_f:
        writer = csv.writer(csv_f, dialect='excel')
        writer.writerow(listTitle)
        for data in listData:
            writer.writerow(data)


if __name__ == "__main__":
    getTitle()
    getData()
    saveData()
    driver.quit()
