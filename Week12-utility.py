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
