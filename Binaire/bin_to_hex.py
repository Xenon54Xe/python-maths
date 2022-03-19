
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