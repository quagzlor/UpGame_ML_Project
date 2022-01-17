import IMG_utils as mage
import NN_main as nunu
import JSON_utils as jason
import KERAS_data_utils as karen

import os

from tqdm import tqdm

def IMG_array(img_path,save_path):
        data_array = []
        tile_count = 0

        if mage.IMG_32_map(img_path):
                for file in tqdm(os.listdir(save_path)):
                        data_array.append([karen.IMG_to_numpy_array_one(os.path.join(save_path,file)),tile_count]) #Image data array , tile number
                        tile_count = tile_count + 1

        return data_array

def IMG_map_build(data_array):
        classified_info = []
        for i in tqdm(range(len(data_array))):
                classified_info.append([data_array[i][1],nunu.TEST_network(data_array[i][0])])
        
        cleaned_array = []

        for i in tqdm(range(len(classified_info))): #Data array is a list of tuples of (tile number, classification)
                if classified_info[i][1] != 5:
                        cleaned_array.append(classified_info[i])
        return cleaned_array

def DICT_builder(data_array, map_name, image_name):
        tile_props = {}
        tile_proptypes = {}
        tile_class = {}

        for i in tqdm(range(len(data_array))):

                tile_name = str(data_array[i][0])

                tile_props.setdefault(tile_name,[]).extend("rough")
                tile_props[tile_name] = ({"rough":True})

                tile_proptypes.setdefault(tile_name,[]).extend("rough")
                tile_proptypes[tile_name] = ({"rough":"bool"})

                x = data_array[i][1]
                data_list = [x,x,x,x]
                tile_class.setdefault(tile_name,[]).extend("terrain")
                tile_class[tile_name] = ({"terrain":data_list})
        
        info_dict={
                "columns":37,
                "image":image_name,
                "imageheight":1800,
                "imagewidth":1200,
                "margin":0,
                "name":map_name,
                "spacing":0,
                "terrains":[
                        {
                                "name":"rough",
                                "properties":{
                                        "rough":True
                                },
                                "propertytypes":{
                                        "rough":"bool"
                                },
                                "tile":0
                        },
                        {
                                "name":"fairway",
                                "properties":{
                                        "fairway":True
                                },
                                "propertytypes":{
                                        "fairway":"bool"
                                },
                                "tile":0
                        },
                        {
                                "name":"green",
                                "properties":{
                                        "green":True
                                },
                                "propertytypes":{
                                        "green":"bool"
                                },
                                "tile":0
                        },
                        {
                                "name":"bunker",
                                "properties":{
                                        "bunker":True
                                },
                                "propertytypes":{
                                        "bunker":"bool"
                                },
                                "tile":0
                        },
                        {
                                "name":"water",
                                "properties":{
                                        "water":True
                                },
                                "propertytypes":{
                                        "water":"bool"
                                },
                                "tile":0
                        }
                ],
                "tilecount":2109,
                "tileheight":32,
                "tileproperties": tile_props,
                "tilepropertytypes": tile_proptypes,
                "tiles":tile_class,
                "tilewidth":32,
                "type":"tileset"

                }
        return info_dict

def main():
        img_path = os.path.join(os.getcwd(),"to_map.png")
        save_path = os.path.join(os.getcwd(),'map_32')

        x = IMG_array(img_path,save_path)
        x = IMG_map_build(x)
        
        y = DICT_builder(x,"test_map",img_path)
        jason.JSON_write(y,"test_map.json")
main()