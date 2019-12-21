from itertools import combinations, permutations
import re

name = input('Name of victim : ')
DOB = input('DOB of victim (DD MM YYYY): ')
player = input("victim's favourite player: ")
number = input("victim's favourite number : ")
nick = input("any nicknames? : ")
extra = input("keywords you will like to add about victim (give spaces eg. coffee gym space) : ")

key = {'A': "/\\", 'B':'|3','D' : '|)', 'E' : '3', 'H':'|-|', 'L':'|_', 'O':'0', 'S':'$', 'V':'\/' }

comb = list(combinations(DOB.split(" ") + name.split(' ') + player.split(" ") + extra.split(" ") + number.split(" ") + nick.split(" ") , 2))
comb = list(comb) + list(combinations(DOB.split(" ") + name.split(' ') + player.split(" ") + extra.split(" ") + number.split(" ") + nick.split(" "), 3))


def listtostring(list):
    string = " "
    return string.join(list)


wordlist = []
for i in comb:
    perm = permutations(i)
    for p in perm:
        print(listtostring(p).replace(" ", ""))
        wordlist.append(listtostring(p).replace(" ", ""))

for wo in wordlist:
    wo.replace('a', key['A']).replace('b', key['B']).replace('d', key['D']).replace('e', key['E']).replace('h', key['H']).replace('l', key['L']).replace('o', key['O']).replace('s', key['S']).replace('v', key['V'])
    wo.replace('A', key['A']).replace('B', key['B']).replace('D', key['D']).replace('E', key['E']).replace('H', key['H']).replace('L', key['L']).replace('O', key['O']).replace('S', key['S']).replace('V', key['V'])
    wordlist.append(wo)

with open('passwords', 'a') as file_object:
    for o in wordlist:
        file_object.write(o+"\n")

