#Author : Quagzlor (divij singh)
import json
from tqdm import tqdm

def JSON_write(data,filename):
    outfile = open(filename,'w')
    json.dump(data,outfile)

def JSON_read(file_name): #Reads the data from the file. straightforward
    read_file = open(file_name,"r")
    json_file_data = json.load(read_file)

    return (json_file_data)

def DICT_order(to_check,check_array): #Returns the new number for whatever value is passed
    to_return = 0
    for i in range(0,len(check_array)):
        if to_check == check_array[i][1]:
            to_return = check_array[i][0]
    return to_return

def JSON_full_tile(data_array):
    final_data = {}
    for key,value in tqdm(data_array.items()):
        for i in range(0,4,1):
            if value[i] != -1:
                if value.count(value[0] == len(value)):
                    key_name = str(key)
                    final_data.setdefault(key_name,[]).extend([value[0]])
    return (final_data)

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
     0 - "right"
     1 - "fairway"
     2 - "green"
     3 - "bunker"
     4 - "water"

    """

    for i in tqdm(range(0,len(json_data["terrains"]))):
        
        if 'left' in json_data["terrains"][i]['name']:
            num_to_append = (0,i)

        elif 'right' in json_data["terrains"][i]['name']:
            num_to_append = (0,i)

        elif 'fairway' in json_data["terrains"][i]['name']:
            num_to_append = (1,i)

        elif 'green' in json_data["terrains"][i]['name']:
            num_to_append = (2,i)

        elif 'bunker' in json_data["terrains"][i]['name']:
            num_to_append = (3,i)
        
        elif 'water' in json_data["terrains"][i]['name']:
            num_to_append = (4,i)

        elif 'LEFT' in json_data["terrains"][i]['name']:
            num_to_append = (0,i)

        elif 'RIGHT' in json_data["terrains"][i]['name']:
            num_to_append = (0,i)

        elif 'FAIRWAY' in json_data["terrains"][i]['name']:
            num_to_append = (1,i)

        elif 'GREEN' in json_data["terrains"][i]['name']:
            num_to_append = (2,i)

        elif 'BUNKER' in json_data["terrains"][i]['name']:
            num_to_append = (3,i)
        
        elif 'WATER' in json_data["terrains"][i]['name']:
            num_to_append = (4,i)
        else:
            num_to_append = (-1,i)

        file_terrain_order.append(num_to_append)

    """
    
    This converts all the numbers to the appropriate test data format.

    """
    holder_array = [0]*4 #Holds the converted tile values
    final_data  ={}  #Dictionary to store final values to return

    for i in tqdm(json_data["tiles"]):
 
        for j in range(0,4):

            holder_val = DICT_order(json_data["tiles"][i]["terrain"][j],file_terrain_order)
            holder_array[j] = holder_val
            
        temp_dict = {} #Dictionaries are a pain to work with. this comment has no importance
        temp_dict[i] = holder_array

        for key, value in temp_dict.items(): #You NEED to do this to add to the main dictionary. Otherwise all the values in the dictionary get set to the last array added.
            final_data.setdefault(key,[]).extend(value)
    return (final_data)

#x = JSON_read("og1.json") #for testing
#y = JSON_data_clean(x) #for testing

#print (y) #for testing