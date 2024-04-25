
"""
 projekt_1.py: první projekt do Engeto Online Python Akademie
 author: Marek Hes
 email: marekhes99@centrum.cz
 discord: marek_09805
 """

from texts import TEXTS
from copy import deepcopy
registered_users = {"bob": "123",
                    "ann": "pass123",
                    "mike": "password123",
                    "liz": "pass123"}
user = input("username:").lower()
password = input("password:").lower()

if user in registered_users.keys() and password in registered_users.values():
    print("-" * 40)
    print("Welcome to the app, " + user + "\nWe have 3 texts to be analyzed.")
    print("-" * 40)
    number_input = input("Enter a number btw. 1 and 3 to select: ")
    print("-" * 40)

    if number_input in ["1", "2", "3"]:
        text = TEXTS[int(number_input) - 1]
    
        words = text.split()
        word_count = len(words)

        title = list()
        for titles in words:
            if titles.istitle():
                title.append(titles)
        upper = list()
        for uppers in words:
            if uppers.isupper() and uppers.isalpha():
                upper.append(uppers)
        lower = list()
        for lowers in words:
            if lowers.islower():
                lower.append(lowers)
        number = list()
        for numbers in words:
            if numbers.isdigit():
                number.append(int(numbers))
        sum_for_numbers = sum(number)

        print("There are", word_count, "words in the selected text.")
        print("There are", len(title), "titlecase words.")
        print("There are", len(upper), "uppercase words.")
        print("There are", len(lower), "lowercase words.")
        print("There are", len(number), "numeric strings.")
        print("The sum of all the numbers", sum_for_numbers)

        print("-" * 40)
        print("LEN|  OCCURENCES  |NR.")
        print("-" * 40)
    
        punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        cleaned_text = deepcopy(text)
        for word in cleaned_text:
            if word in punc:
                cleaned_text = cleaned_text.replace(word, "")
        
        cleaned_words = cleaned_text.split()
        frequencies = {}
        for word in cleaned_words:
            frequencies[len(word)] = frequencies.get(len(word),0) + 1
        for key, value in sorted(frequencies.items()):
            print(f"{key:3}|{value * '*':<14}|{value}")
    else:
        print("The number You've selected is not valid, terminating the program..")
else:
    print("$ python projekt1.py\nusername:" + user + "\npassword:" + password +
"\nunregistered user, terminating the program..")

