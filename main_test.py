import numpy
import os
import JSON_utils as jason
import IMG_utils as image
import KERAS_data_utils as keras_data

x = jason.JSON_read("dcgc1.json")
x = jason.JSON_data_clean(x)
x = keras_data.dict_splitter(x)

#y = image.IMG_32_tile("1.png")
#y = image.IMG_16_tile((os.path.join(os.getcwd()+'/sliced_32')))

path = os.path.join(os.getcwd()+'/sliced_16')
z = keras_data.IMG_to_numpy_array(path,x)

print (z)