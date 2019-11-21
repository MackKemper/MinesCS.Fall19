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
