
# Load shortcuts_2.csv using inbuilt function
# Path: extra\fix.py

from csv import reader

with open("shortcuts_2.csv") as file:
    csv_reader = reader(file, delimiter=",")
    # Skip the first line
    next(csv_reader)

    shortcuts = {}
    for row in csv_reader:
        source = row[0][:-1].strip(" ")
        target = row[1][:-1].strip(" ")
        distance = row[2]

        # check if the source exists in the dictionary
        if source in shortcuts:
            # check if the target exists in the dictionary
            if target in shortcuts[source]:
                # check if the distance is smaller than the current one
                if distance < shortcuts[source][target]:
                    shortcuts[source][target] = distance
            else:
                shortcuts[source][target] = distance
        else:
            shortcuts[source] = {target: distance}

    # print shortcuts with format
    # write shortcuts to a file
    with open("shortcuts_3.csv", "w") as file:
        file.write("Source, Destination, Distance\r")
        for source in shortcuts:
            for target in shortcuts[source]:
                if source == target:
                    continue

                print(f"{source} -> {target}: {shortcuts[source][target]}")
                # write source,target,distance to file
                file.write(f"{source},{target},{float(shortcuts[source][target])/2}\r")


