from selenium import webdriver                                     #ne ajuta sa deschidem pagina si sa parsam info
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())        #in var browser citesc driverul
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')                     #o lista cu toate elem
#print(lista)

header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')         #transf headerul intr-o lista
dictionar = {i: [] for i in header}                #cheia e fiecare elem din header
#print(dictionar)
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):       #de la inceputul randului, adica header+int(j) pana la toata lista cu un pas de nr de elem de pe rand
        dictionar[header[int(j)]].append(lista[i])                     #cheia e header[j]
print(dictionar)

df = pd.DataFrame(dictionar)
df.to_csv("BNR_ALL_DATA.csv")

time.sleep(5)