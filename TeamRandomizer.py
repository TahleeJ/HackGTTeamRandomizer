import random

#Original name list
names1 = ["Tahlee", "Khalaya", "Erica", "Jackson", "Emir"]

#Randomized name list
names2 = ["", "", "", "", ""]

#List of names from original name list already chosen
chosen = []

#Randomizes names from original list
for i in range(0, 5):
    if i == 0: #Randomly adds first name into randomized list
        num = random.randint(0, 4)
        chosen.append(num)
    else: #Adds all other names into randomized list given that the randomly selected index has not already been chosen
        while num in chosen:
            num = random.randint(0, 4)

    names2[num] = names1[i]
    chosen.append(num)

teamname = ["Shapes and Colors", "Colors and Shapes"]

team1 = []
team2 = []
teams = [team1, team2]

#Number of people assigned to each team, max 3 and 2
count1 = 0
count2 = 0

#Assigns each person from randomized list into a randomly selected team
for i in range(0, 5):
    num = 0 #Randomly selected team
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

#Randomly assigns a team name to a randomly selected team
other = [] #Random team
ran = random.randint(0, 1)
# while (ran in other):
#     ran = random.randint(0, 1)  #never actually runs...
other.append(ran)
otheran = random.randint(0, 1) #Random team name

print("\n" + teamname[otheran])
print(teams[ran])
teams.remove(teams[ran])
teamname.remove(teamname[otheran])
print("\n" + teamname[0])
print(teams[0])
