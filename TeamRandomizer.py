import random

names1 = ["Tahlee", "Khalaya", "Erica", "Jackson", "Emir"]

names2 = ["", "", "", "", ""]

chosen = []

for i in range(0, 5):
    if i == 0:
        num = random.randint(0, 4)
        chosen.append(num)
    else:
        while num in chosen:
            num = random.randint(0, 4)

    names2[num] = names1[i]
    chosen.append(num)

teamname = ["Shapes and Colors", "Colors and Shapes"]

team1 = []
team2 = []
teams = [team1, team2]

count1 = 0
count2 = 0

for i in range(0, 5):
    num = 0
    while (count1 < 4 and count2 < 3) or (count1 < 3 and count2 < 4):
        num = random.randint(1, 2)
        if num == 1 and ((count1 + 1 < 4 and count2 < 3) or (count1 + 1 < 3 and count2 < 4)):
            count1 += 1
            team1.append(names2[i])
            break
        elif num == 2 and ((count2 + 1 < 4 and count1 < 3) or (count2 + 1 < 3 and count1 < 4)):
            count2 += 1
            team2.append(names2[i])
            break
        else:
            continue

other = []
ran = random.randint(0, 1)
while (ran in other):
    ran = random.randint(0, 1)
other.append(ran)
otheran = random.randint(0, 1)

print("\n" + teamname[otheran])
print(teams[ran])
teams.remove(teams[ran])
teamname.remove(teamname[otheran])
print("\n" + teamname[0])
print(teams[0])
