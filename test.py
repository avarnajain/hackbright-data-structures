

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

houses = list(set(line.rstrip().split('|')[2] for line in filename if
    line.rstrip().split('|')[2] != ""))


filename = open("cohort_data.txt")
# house_dict = [house_dict[item] for item in houses house_dict[item] = item.lower().replace("'","").replace(" ","_")]
print("here", houses)
house_dict = {}

# for item in houses:
    # house_dict[item] = item.lower().replace("'","").replace(" ","_")
for item in houses:
    house_dict[item] = []


for line in filename:
    line = line.rstrip().split('|')
    last_name = line[1]
    
    for house in house_dict:
        if house == line[2]:
            sorted(house_dict[house].append(last_name))



print(house_dict)



    # return all_hogwarts