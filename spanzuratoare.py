#cuvant = "a _ _ a _ _ t"
#alfabet
#word = "address"

import random
from random_word import list_of_random_word

#list_of_random_word = ["papagal", "caiet", "calculator"]                 #daca am lista aici

word = random.choice(list_of_random_word)
word_list =[]
unique_letter = set(word)

for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())
        if item in unique_letter:
           unique_letter.remove(item)
word_length = len(unique_letter)
print(" ".join(word_list))                   #concatenare elem lista intr-un string
count_nr = 1
already_list_checked = []                    #lista cu litere deja incercate
new_word = " ".join(word_list)
while count_nr <= word_length:
    user_letter = input("Alege o litera: ").lower()
    if user_letter == "":
        print("Introdu o litera")
    if user_letter in word_list:
        print("Litera deja afisata pe ecran")
    elif user_letter in already_list_checked:
        print(already_list_checked)
        print(f"Litera deja a fost incercata, literele deja incercate sunt: {' '.join(already_list_checked)}")
    else:
        if user_letter in word:
            #print("Litera exista in cuvant")
            for iterator, value in enumerate(word):
                #print(f"{iterator} => {value}")
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))
        else:
            count_nr += 1
        if "_" not in "".join(word_list):
            print("Ai castigat")
            break
        elif count_nr > word_length :
            print(f"Ai pierdut! Cuvantul era {word}")
        already_list_checked.append(user_letter)
