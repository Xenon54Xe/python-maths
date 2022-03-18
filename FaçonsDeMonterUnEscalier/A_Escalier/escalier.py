'''
Compter le nombre de façons de monter un escalier à X marches
'''
stop_script = True

print("Donnez un nombre de marches pour l'escalier.\nNous vous donnerons ensuite le nombre de facons de le monter.")
steps_amount = int(input())

while stop_script:
    if steps_amount < 0:
        print("Erreur ! vous devez donner un nombre positif ou 0")
        steps_amount = int(input())
    else:
        break

print("Voulez-vous savoir le nombre de façons de monter chaque marches d'un escalier à {} marches, ou juste savoir pour la marche n°{} (tout/une)".format(steps_amount, steps_amount))
spam = input()

while stop_script:
    if spam == "tout":
        break
    elif spam == "une":
        break
    else:
        print("Vous devez entrer 'tout' ou 'une' !")
        spam = input()

steps = 0
way_before = 1
way_before_two = 0
next_way = 0


if spam == "tout" and steps_amount == 0:
    print("Un escalier avec {} marche à {} facon de se monter (on ne monte pas)".format(steps_amount, way_before))
else:
    for x in range(steps_amount):
        steps += 1
        next_way = way_before_two + way_before
        if spam == "tout":
            if next_way == 1:
                print("{} marche --> {} façon".format(steps, next_way))
            else:
                print("{} marche --> {} façons".format(steps, next_way))
        way_before_two = way_before
        way_before = next_way

if spam == "une":
    if steps_amount == 0:
        print("Un escalier avec {} marches à {} façon de se monter (on ne monte pas)".format(steps_amount, next_way + 1))
    else:
        if next_way == 1:
            print("Un escalier avec {} marches à {} façon de se monter.".format(steps_amount, next_way))
        else:
            print("Un escalier avec {} marches à {} façons de se monter.".format(steps_amount, next_way))
