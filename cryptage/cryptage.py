
import os.path as path


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
            x -= 256
        elif x < 0:
            x += 256
        if ord(letter) > 255:
            print(f"Erreur avec {letter} : nb={ord(letter)}, result={x}")
            x = ord(letter) + list_key[time]
        list_letters.append(chr(x))
        time += 1

    str = ""
    for letter in list_letters:
        str += letter
    return str


mode = 0
while not 1 <= mode <= 2:
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

    with open(file_name, "r", encoding="utf_8") as file:
        txt = file.read()

    key = input(f"Donnez la clé pour {sufix}er ")

    x = Crypting(txt, key, mode)

    with open("result.txt", "w", encoding="utf-8") as file:
        for result in x:
            file.write(result)

        if mode == 1:
            file.write("\n")
        else:
            file.seek(file.tell() - 2)
            file.write(" //END")
