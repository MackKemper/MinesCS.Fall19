# PrintOutput
def PrintOutput(thing):
    print("OUTPUT ", thing)

# LoadFile
def LoadFile(loc):
    line_list = []
    with open(loc) as doc:
        lines = doc.readlines()
        for line in lines:
            line = line.rstrip()
            line_list.append(line)
    return(line_list)

# UpdateString
def UpdateString(string, char, index):
    string_list = list(string)
    string_list[index] = char
    new_string = "".join(string_list)
    print("OUTPUT ", new_string)

# FindWordCount
def FindWordCount(input_list, string):
    count = 0
    for i in input_list:
        split_list = i.split()
        for i in split_list:
            if i == string:
                count += 1
    return(count)

# ScoreFinder
def ScoreFinder(player_names, player_scores, player):
    done = False
    player_names_c = []
    player_c = player.upper()
    for i in player_names:
        i = i.upper()
        player_names_c.append(i)
    for players in player_names_c:
        if players == player_c:
            score_loc = player_names_c.index(player_c)
            print("OUTPUT", player, "got a score of", player_scores[score_loc])
            done = True
    if not done:
        print("OUTPUT player not found")

# Union
def Union(list1, list2):
    new_list = list1 + list2
    return(new_list)

# Intersection
def Intersection(list1, list2):
    doubles = []
    for item in list1:
        for thing in list2:
            if thing == item:
                doubles.append(thing)
    return(doubles)
