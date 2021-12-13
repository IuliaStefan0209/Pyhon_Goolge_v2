#info pe ultimile 7 zile

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://bnr.ro/Cursul-de-schimb--7372.aspx")     #r e variabila care ne-a realizat requestul
link = BeautifulSoup(r.text, "html.parser")                        #imi parseaza pagina
#print(link)

title = link.find_all('div', attrs={'class': 'contentDiv'})[0]            #cu find_all cautam un elem
header = []
dataset = []                                                              #se umple cand iesim din al treilea for pt ca acp;p avem un alt rand
for tr_index in title.find_all('table'):                                  #cautam toate tag-urile de table
    for td_index in tr_index.find_all('tr'):
       td_list = []
       if td_index.find_all('th'):                                         #pt denumirea fiecarei coloane
           header = [th_index.get_text() for th_index in td_index.find_all('th')]                    #le pun intr-o lista
       for index, td_value in enumerate(td_index.find_all('td')):       #parcurgere td-uri si extragere si index si td cu enumerate
            print(index, td_value)                                      #ma intereseaza doar textul
            if index == 0:                                              #index 0, adica urmat linie din tabel
                td_list.append(td_value.get_text())
            else:
                td_list.append(float(td_value.get_text().lstrip('   ').replace(',', '.')))    #eliminare spatiu de la stanga cu lstrip si inlocuire , cu .
       dataset.append(td_list)                                          #lista de liste

print(dataset)

#mutam totul in pandas
df = pd.DataFrame(dataset, columns=header)                     #dataframe - lista de liste
df.to_csv("CursBNR.csv", header=header)
