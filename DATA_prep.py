#Author : Quagzlor (divij singh)
import numpy as np
import os
import time
import pickle
from random import shuffle
from tqdm import tqdm

from tkinter.filedialog import askdirectory #GUI to make life simpler

import JSON_utils as jason #Sounds like it, so why not?
import IMG_utils as mage #Naming it image might lead to confusion
import KERAS_data_utils as karen #Dangit it Karen, why'd you leave me?

def JSON_func(folder_path,file_name): #Reads all the json file in a folder, and returns an array with the data
    JSON_data = jason.JSON_read(os.path.join(folder_path,file_name))
    JSON_data = jason.JSON_data_clean(JSON_data)
    JSON_data = jason.JSON_full_tile(JSON_data)
    #JSON_data = karen.dict_splitter(JSON_data)

    return JSON_data

def IMG_func(folder_path,file_name): #Runs the image slicing
    
    IMG_data = mage.IMG_32_tile(os.path.join(folder_path,file_name))
    #IMG_data = mage.IMG_16_tile((os.path.join(os.getcwd()+'/sliced_32'))) (working with 32x32 images now)

    return  IMG_data

def INFO_dump(data_to_dump,filename_1,filename_2): #Writes the training and test data to the JSON file
    
    split_point = int(len(data_to_dump)/10) #10% of the Data is taken as validation
    split_point = len(data_to_dump) - split_point

    data_1 = data_to_dump[:split_point]
    data_2 = data_to_dump[split_point:]

    outfile = open(filename_1,'wb')
    pickle.dump(data_1,outfile)
    outfile.close()

    outfile = open(filename_2,'wb')
    pickle.dump(data_2,outfile)
    outfile.close()

def IN_dir(dir_path,filetype): #Returns a list of files/folders in a directory
    file_list = []

    for filename in os.listdir(dir_path):
        if (filename.endswith(filetype)):
            file_list.append(os.path.join(dir_path,filename))
    
    return file_list

def main(file_to_save_to_1,file_to_save_to_2):
    """

    Where to begin...

    Basically, it takes one main folder. Then it goes through the subfolders.
    For a subfolder, it first converts all JSON data, then, image by image, it converts them to numpy arrays and affixes the appropriate label.
    Finally, it writes it all to a file.

    """

    FINAL_test_data = []
    IMG_sliced_folder_path = os.path.join(os.getcwd()+'/sliced_32')

    print ("Select the main folder with the JSON data") #Select the main folder with the JSON data subfolders
    time.sleep(2)
    JSON_main_path = 'C:/Users/Quagzlor/Desktop/temp/JSON and IMG data/Master JSON Data' #askdirectory()
    JSON_folders = IN_dir(JSON_main_path,"")

    print ("Select the main folder with the images") #Select the main folder with the image subfolders
    time.sleep(2)
    IMG_main_path = 'C:/Users/Quagzlor/Desktop/temp/JSON and IMG data/Master IMG Data' #askdirectory()
    IMG_folders = IN_dir(IMG_main_path,"")
    for i in tqdm(range(len(IMG_folders))):

        JSON_data_path = JSON_folders[i] #Folder path for the JSON file
        JSON_files = IN_dir(JSON_data_path,".json")

        IMG_data_path = IMG_folders[i] #Folder path for the image file
        IMG_files = IN_dir(IMG_data_path,".png")
        
        for i in tqdm(range(len(IMG_files))): #Matches up the course map with the JSON file
            IMG_split = IMG_func(IMG_data_path,IMG_files[i])
            JSON_data = JSON_func(JSON_data_path,JSON_files[i]) #Array with each of the JSON data files' contents

            if IMG_split:
                FINAL_test_data = FINAL_test_data + karen.IMG_to_numpy_array(IMG_sliced_folder_path, JSON_data)
    black_data = karen.IMG_add_black(os.path.join(os.getcwd(),'black.png'))
    FINAL_test_data = FINAL_test_data + black_data
    shuffle(FINAL_test_data)
    INFO_dump(FINAL_test_data,file_to_save_to_1,file_to_save_to_2)
#main("training","testing")