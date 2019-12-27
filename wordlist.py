from itertools import combinations, permutations

name = input('Name of victim : ')
DOB = input('DOB of victim (DD MM YYYY): ')
player = input("victim's favourite player: ")
number = input("victim's favourite number : ")
nick = input("any nicknames? : ")
extra = input("keywords you will like to add about victim (give spaces eg. coffee gym space) : ")
ask = input('Include 1337 mode(Y/n) : ')
if ask == 'y' or ask == 'Y':
    mode1337=True
else :
    mode1337=False

key = {'B':'|3','D' : '|)', 'E' : '3', 'H':'|-|', 'L':'|_', 'O':'0', 'S':'$'}
letters =['B', 'D', 'E', 'H', 'L', 'O', 'S']

comb = list(combinations(DOB.split(" ") + name.split(' ') + player.split(" ") + extra.split(" ") + number.split(" ") + nick.split(" ") , 2))
comb = list(comb) + list(combinations(DOB.split(" ") + name.split(' ') + player.split(" ") + extra.split(" ") + number.split(" ") + nick.split(" "), 3))


def listtostring(list):
    string = " "
    return string.join(list)


wordlist = []
for i in comb:
    perm = permutations(i)
    for p in perm:
        wordlist.append(listtostring(p).replace(" ", ""))


new_list=[]
j = ''


def check(k):
    for i in k:
        if i.upper() in letters:
            return True


if mode1337 :
    for w in wordlist:
        j = w
        if j.isdigit() == False and check(j):
            for k, v in key.items():
                j = j.replace(k.lower(), v)
            new_list.append(j)


wordlist += new_list

with open('passwords', 'a') as file_object:
    for o in wordlist:
        file_object.write(o+"\n")

print('passwords written to passwords file..')
