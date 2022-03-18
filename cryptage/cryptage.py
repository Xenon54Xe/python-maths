
import os.path as path
from math import sqrt


def Is_Number(str):
    for i in range(48, 58):
        if ord(str) == i:
            return True
    return False


def Crypting(sentence, sentenceKey, mode):
    list_key = []
    mode = int(mode)
    for key in sentenceKey:
        if mode == 1:
            list_key.append(ord(key))
        else:
            list_key.append(-ord(key))

    list_letters = []
    time = 0
    for letter in sentence:
        if time > len(list_key) - 1:
            time = 0
        x = ord(letter) + list_key[time]
        if x > 255:
            x = x - 256
        elif x < 0:
            x = 256 + x
        list_letters.append(chr(x))
        time += 1

    str = ""
    for letter in list_letters:
        str += letter
    return str


mode = int(input("Donnez le mode, crypter(1) ou décrypter(2) "))

if mode == 1:
    sufix = "crypt"
else:
    sufix = "decrypt"

file_name = f"{sufix}age.txt"

if not path.isfile(file_name):
    with open(file_name, "w"):
        pass
    print("Fichier non trouvé, réessayez...")
else:
    input(f"Continuez lorsque vous aurez écrit le texte à {sufix}er dans '{file_name}'")

    if mode == 1:
        with open(file_name, "r", encoding="utf_8") as file:
            txt = file.read()
    else:
        with open(file_name, "r", encoding="utf-8") as file:
            txt = file.read()

            list_numbers = []
            case_str = ""
            for case in txt:
                if Is_Number(case):
                    case_str += case
                elif case_str != "":
                    list_numbers.append(int(case_str))
                    case_str = ""

            list_letters = []
            for number in list_numbers:
                list_letters.append(chr(number))

            txt = ""
            for letter in list_letters:
                txt += letter

    key = input(f"Donnez la clé pour {sufix}er ")

    x = Crypting(txt, key, mode)

    print(x)
    with open("result.txt", "w", encoding="utf-8") as file:
        time = 0
        for result in x:
            if time > sqrt(len(x)) and mode == 1:
                time = 0
                file.write("\n")

            if mode == 2:
                file.write(result)
            else:
                file.write(f"{ord(result)} ")
            time += 1

print("Process finished")
