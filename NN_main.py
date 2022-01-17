#Author : Quagzlor (divij singh)
import numpy as np

import os
import pickle

from tqdm import tqdm

import DATA_prep

from keras.models import Sequential, load_model #Sequential model of Neural Network, i.e it goes layer by layer; load_model to read the model file
from keras.layers import Dense #Each neuron is connected to each neuron of the next layer
from keras.layers import Dropout #Can drop random data to avoid overfitting of the model
from keras.layers import Flatten #Reduces the size of the input image
from keras.layers import InputLayer

from keras.optimizers import Adam, SGD, Nadam
from keras.layers.convolutional import Conv2D, MaxPooling2D, AveragePooling2D #
from keras.utils import np_utils #Numpy utilities

from keras import backend as K #Setting the image data format
K.set_image_dim_ordering('th')

def DATA_load(filename):
    print (filename)
    infile = open(filename,'rb')
    loaded_data = pickle.load(infile)
    infile.close()

    row1 = []
    for item in loaded_data: #Splitting the data into image data
        row1.append(item[0])
    row1 = np.array(row1)
    row1 = row1.astype('float32')/255.0 #Normalise the iamge array
    row1 = np.squeeze(row1)
    
    row2 = []
    for item in loaded_data: #And label data
        row2.append(item[1])
    row2 = np.array(row2)

    return row1,row2

def MODEL_build(epochs,learning):
    model = Sequential()
    
    model.add(InputLayer(input_shape = [3,32,32])) #Input layer

    model.add(Conv2D(64, (3,3), padding = 'same', activation = 'relu')) #Convoluted Layer 1
    model.add(Conv2D(128, (3,3), padding = 'same', activation = 'relu')) #Convoluted Layer 1
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.3))
    """
    model.add(Conv2D(128, (3,3), padding = 'same', activation = 'relu')) #Convoluted Layer 1
    model.add(Conv2D(256, (3,3), padding = 'same', activation = 'relu')) #Convoluted Layer 1
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.5))
    
    model.add(Conv2D(512, (3,3), padding = 'same', activation = 'relu')) #Convoluted Layer 1
    model.add(Conv2D(512, (3,3), padding = 'same', activation = 'relu')) #Convoluted Layer 1
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Dropout(0.5))
    """

    model.add(Flatten())
    model.add(Dense(256, activation = 'relu')) #Dense NN layer
    model.add(Dropout(0.3))
    #model.add(Dense(256, activation = 'relu')) #Dense NN layer
    #model.add(Dropout(0.5))
    #model.add(Dense(512, activation = 'relu')) #Dense NN layer
    #model.add(Dropout(0.5))
    #model.add(Dense(512, activation = 'relu')) #Dense NN layer
    #model.add(Dropout(0.5))
    model.add(Dense(6, activation = 'softmax')) #5 neurons to correspond to 5 output values
    opti = SGD(lr = learning)

    model.compile(loss = 'categorical_crossentropy', optimizer = opti, metrics = ['accuracy'])

    print (model.summary())

    return model

def DATA_fit(model,xtrain,ytrain, xtest, ytest, epochs):
    model.fit(xtrain,ytrain, validation_data = (xtest, ytest), epochs = epochs, batch_size = 100)

    scores = model.evaluate(xtest,ytest,verbose = 0)

    print ("Accuracy: %.2f%%" % (scores[1]*100))

def TRAIN_network():
    xtrain, ytrain = DATA_load('training')
    xtest, ytest = DATA_load('testing')

    #model.load_weights('nn_weights.h5')

    DATA_fit(model, xtrain,ytrain,xtest,ytest,epochs)

    model.save_weights('nn_weights.h5')

def TEST_network(data_to_test):
    model.load_weights('nn_weights.h5')

    result = model.predict(data_to_test)
    final_result = int(result.argmax())

    return final_result

def train_loop(x):
    for i in range(x):
        DATA_prep.main("training","testing")
        TRAIN_network()
    
    return True

epochs = 2
learning = 0.1

model = MODEL_build(epochs,learning)

#TRAIN_network()