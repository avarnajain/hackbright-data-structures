

filename = open("cohort_data.txt")

all_hogwarts = []
dumbledores_army = []
gryffindor = []
hufflepuff = []
ravenclaw = []
slytherin = []
ghosts = []
instructors = []

# Code goes here

houses = set(line.rstrip().split('|')[2] for line in filename if
    line.rstrip().split('|')[2] != "")

houses_dict = {}

for item in houses:
    houses_dict[item] = item.lower().strip().replace("'","")


print(houses_dict)



    # return all_hogwarts