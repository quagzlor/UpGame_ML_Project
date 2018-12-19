import json

def JSON_read(file_name): #reads the data from the file. straightforward
    read_file = open(file_name,"r")
    json_file_data = json.load(read_file)

    return (json_file_data)

def JSON_data_clean(json_data): 
    """
    This method is a big one.

    It looks at the ordering of the terrains, and notes the corresponding order number.

    Then, it changes that number in each corresponding terrain value to match the standard format.

    """
    file_terrain_order = []

    """
    The index is used to store what the ordering of terrain in the passed data is.
     In the index:
     0 - "left"
     1 - "right"
     2 - "fairway"
     3 - "green"
     4 - "bunker"
     5 - "water"

    """
    for i in range len(json_data["terrains"]):
        if json_data["terrains"][i]["properties"]["left"] is True:
            num_to_append = 0

        elif json_data["terrains"][i]["properties"]["right"] is True:
            num_to_append = 1

        elif json_data["terrains"][i]["properties"]["fairway"] is True:
            num_to_append = 2

        elif json_data["terrains"][i]["properties"]["green"] is True:
            num_to_append = 3

        elif json_data["terrains"][i]["properties"]["bunker"] is True:
            num_to_append = 4
        
        else:
            num_to_append = 5

        file_terrain_order.append(num_to_append)

    """
    This converts all the numbers to the appropriate test data format.

    """

    for i in json_data["tiles"]:
        for j in range 4:
            if i["terrain"][0] = 

