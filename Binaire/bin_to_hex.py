
def Bin_To_Hex(nb):
    hex_library = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    nb = str(nb).split(" ")
    result = ""
    for boxes in nb:
        box_list = list(boxes)
        reversed_box_list = []
        for i in range(len(box_list)):
            reversed_box_list.append(box_list[len(box_list) - i - 1])
        add = 0
        for i in range(len(reversed_box_list)):
            add += int(reversed_box_list[i]) * 2 ** i
        if add > 9:
            add = hex_library[add]
        result += str(add)
    return result
