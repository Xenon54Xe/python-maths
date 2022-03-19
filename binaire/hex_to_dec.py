
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