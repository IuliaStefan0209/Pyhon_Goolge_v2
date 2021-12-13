from pandas import ExcelWriter
from openpyxl.workbook import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


def pad_dict_list(dict_list, padel):
    lmax=0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if ll < lmax:
            dict_list[lname] += [padel] * (lmax-ll)
    return dict_list


browser = webdriver.Chrome(ChromeDriverManager().install())

for day in range(20, 27):
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-noiembrie-ora-13-00-2/")

    table = browser.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr/td')
    table_list = []

    for item in table:
        table_list.append(item.text)
    print(table_list)

    header = browser.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td')
    header_list = []

    for item in header:
        header_list.append(item.text)
    print(header_list)

    dict = {i: [] for i in header_list}

    for i in range(0, len(header_list)):
        for j in range(len(header_list) + int(i), len(table_list), len(header_list)):
            dict[header_list[int(i)]].append(table_list[j])
    print(dict)

    final_dict = pad_dict_list(dict, ' ')
    print(final_dict)

    df = pd.DataFrame(final_dict)

    if day == 20:
        df.to_excel('Covid_20-27_noiembrie.xlsx')
    else:
        with ExcelWriter('Covid_20-27_noiembrie.xlsx', mode='a', engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=f'Sheet{day}')

    time.sleep(3)
