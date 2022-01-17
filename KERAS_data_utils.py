#Author : Quagzlor (divij singh)
from keras.applications.imagenet_utils import preprocess_input as keras_preprocess_input #Used to convert the image array into a format to be used with keras
import keras.preprocessing.image as keras_preprocess_image #Used to convert the image into a compatible format

import numpy as np #Will be used to store the image in an array form

from tqdm import tqdm
from PIL import Image

import os

def one_hot_labeling(label_data):
    """

    Converts the label into a binary array, with the index of 1 being the label.

    """

    if label_data[0] == 0: #Rough
        hot_label = np.array([1,0,0,0,0,0])

    elif label_data[0] == 1: #Fairway
        hot_label = np.array([0,1,0,0,0,0])

    elif label_data[0] == 2: #Green
        hot_label = np.array([0,0,1,0,0,0])

    elif label_data[0] == 3: #Bunker
        hot_label = np.array([0,0,0,1,0,0])

    elif label_data[0] == 4: #Water
        hot_label = np.array([0,0,0,0,1,0])

    else: #Not on map
        hot_label = np.array([0,0,0,0,0,0])

    return hot_label

def dict_splitter(label_dict): #Used to split the tile arrays into subtiles
    
    final_data = {}

    for key,value in  tqdm(label_dict.items()):
        for i in range(0,4,1):
            if value[i] != -1:
                key_name = str(str(key) + "_" + str(i)) #Builds the name as tile_subtile
                final_data.setdefault(key_name,[]).extend([value[i]])
    
    return (final_data)


def IMG_add_black(directory): #Adding sampel black/clear images for the background of the course
    image = Image.open(directory)
    image = keras_preprocess_image.img_to_array(image.convert('RGB'))
    image = image.reshape(3,32,32)
    image = np.expand_dims(image, axis=0)
    image = keras_preprocess_input(image)

    black_data = []

    for i in range(0,1000,1):
        black_data.append([np.array(image),np.array([0,0,0,0,0,1])])
    return black_data

def IMG_to_numpy_array_one(image_path):
    image = Image.open(image_path)
    image = keras_preprocess_image.img_to_array(image.convert('RGB'))
    image = image.reshape(3,32,32)
    image = np.expand_dims(image, axis=0)
    image = keras_preprocess_input(image)

    return image
    
def IMG_to_numpy_array(directory_to_iterate,label_dict):
    """

    This method will go over the 16x16 images, and then convert them into numpy arrays.
    It'll use keras's own preprocessing tools to ensure that the format fits.

    !!!! Check the performance of this when running with numerous data files, to ensure it does not keep loading keras individually. That'll slow down the program!!!!

    """
    training_data = []
    
    for label in tqdm(label_dict): #Converts the image to numpy format, and sets the appropriate label to the right array.

        image = Image.open(os.path.join(directory_to_iterate,label+'.png')) #Only opens images which are tagged
        
        #image = keras_preprocess_image.img_to_array(image) #converting the image data to work with keras
        image = keras_preprocess_image.img_to_array(image.convert('RGB'))
        image = image.reshape(3,32,32)
        image = np.expand_dims(image, axis=0)
        image = keras_preprocess_input(image)

        training_data.append([np.array(image),one_hot_labeling(label_dict[label])]) #Appends the numpy array with image data, and the one hot label
    return training_data