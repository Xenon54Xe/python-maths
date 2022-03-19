
def Bin_To_Hex(nb):
    nb = str(nb)
    nb = nb.replace(" ", "")

    hex_library = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    bin_list = []
    for bin in nb:
        bin_list.insert(0, bin)
    bin_list_squared = []
    bin_str = ""
    for i in range(len(bin_list)):
        if i / 4 == int(i / 4) and i != 0:
            bin_list_squared.insert(0, bin_str)
            bin_str = ""
        bin_str = bin_list[i] + bin_str
    if bin_str != "":
        bin_list_squared.insert(0, bin_str)
    hex_str = ""
    for box in bin_list_squared:
        hex = 0
        for i in range(len(box)):
            add = int(box[len(box) - i - 1]) * 2 ** i
            hex += add
        if hex > 9:
            hex_str += hex_library[hex]
        else:
            hex_str += str(hex)
    return hex_str


def Dec_To_Bin(nb):
    nb = str(nb)
    nb = nb.replace(" ", "")
    nb = int(nb)

    dividend = 1
    time = 0
    while dividend <= nb:
        dividend *= 2
        time += 1
    dividend /= 2
    time -= 1
    result_list = []
    while nb > 0:
        if nb - dividend >= 0:
            nb -= dividend
            result_list.append(1)
        else:
            result_list.append(0)
        dividend /= 2
        time -= 1
    for i in range(time + 1):
        result_list.append(0)
    result_list_2 = []
    time = 0
    for i in range(len(result_list)):
        box = result_list[len(result_list) - i - 1]
        result_list_2.append(box)
        time += 1
        if time / 4 == int(time / 4):
            result_list_2.append(" ")
    result = ""
    for boxes in result_list_2:
        result = str(boxes) + result
    return result


def Hex_To_Dec(nb):
    nb = str(nb)
    nb = nb.replace(" ", "")

    hex_library = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

    nb = list(nb)
    reversed_list = []
    for i in range(len(nb)):
        reversed_list.append(nb[len(nb) - i - 1])
    add = 0
    for i in range(len(reversed_list)):
        nb = hex_library[reversed_list[i]]
        add += nb * 16 ** i
    result = str(add)
    return result


number = str(input("Donnez un nombre à convertir: "))
num_list = list(number)

binary = True
decimal = True
hexadecimal = True

numbers_library = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

stop = False
for boxes in num_list:
    for i in range(16):
        int_nb = numbers_library[i]
        if boxes == int_nb:
            if i > 1:
                binary = False
            if i > 9:
                decimal = False
                stop = True
                break
    if stop:
        break

size = 0
sentence = ""
if binary:
    size += 1
    sentence += f"binaire({size}) "
if decimal:
    size += 1
    sentence += f"decimal({size}) "
if size > 0:
    size += 1
    sentence += f"hexadecimal({size}): "
    choice = int(input(sentence))
    choice += 3 - size
else:
    choice = 3

if choice == 1:
    hex_number = Bin_To_Hex(number)
    dec_number = Hex_To_Dec(hex_number)
    print(f"Ce nombre en Décimal vaut: {dec_number}")
    print(f"Et en Hexadécimal: {hex_number}")
elif choice == 2:
    bin_number = Dec_To_Bin(number)
    hex_number = Bin_To_Hex(bin_number)
    print(f"Ce nombre en Binaire vaut: {bin_number}")
    print(f"Et en Hexadécimal: {hex_number}")
else:
    dec_number = Hex_To_Dec(number)
    bin_number = Dec_To_Bin(dec_number)
    print(f"Ce nombre en binaire vaut: {bin_number}")
    print(f"Et en Décimal: {dec_number}")
