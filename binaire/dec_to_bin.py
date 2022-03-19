
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