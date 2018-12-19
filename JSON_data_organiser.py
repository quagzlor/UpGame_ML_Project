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
    
    for i in range(0,len(json_data["terrains"])):
        if 'left' in json_data["terrains"][i]["properties"]:
            num_to_append = 0

        elif 'right' in json_data["terrains"][i]["properties"]:
            num_to_append = 1

        elif 'fairway' in json_data["terrains"][i]["properties"]:
            num_to_append = 2

        elif 'green' in json_data["terrains"][i]["properties"]:
            num_to_append = 3

        elif 'bunker' in json_data["terrains"][i]["properties"]:
            num_to_append = 4
        
        elif 'water' in json_data["terrains"][i]["properties"]:
            num_to_append = 5

        file_terrain_order.append(num_to_append)

    """
    This converts all the numbers to the appropriate test data format.

    """
    holder_array = [0]*4 #holds the converted tile values
    final_data={}  #dictionary to store final values to return

    for i in json_data["tiles"]:
 
        for j in range(0,4):

            if json_data["tiles"][i]["terrain"][j] == 0 :
                holder_array[j] = file_terrain_order[0]

            elif json_data["tiles"][i]["terrain"][j] == 1 :
                holder_array[j] = file_terrain_order[1]
            
            elif json_data["tiles"][i]["terrain"][j] == 2 :
                holder_array[j] = file_terrain_order[2]
            
            elif json_data["tiles"][i]["terrain"][j] == 3 :
                holder_array[j] = file_terrain_order[3]
            
            elif json_data["tiles"][i]["terrain"][j] == 4 :
                holder_array[j] = file_terrain_order[4]
            
            elif json_data["tiles"][i]["terrain"][j] == 5:
                holder_array[j] = file_terrain_order[5]

            else:
                holder_array[j] = -1

        temp_dict = {} #dictionaries are a pain to work with
        temp_dict[i] = holder_array
        print (temp_dict)

        for key, value in temp_dict.items():
            final_data.setdefault(key,[]).extend(value)

    return (final_data)

x = JSON_read("dcgc1.json")
y = JSON_data_clean(x)

print (y)