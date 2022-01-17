#Author : Quagzlor (divij singh)
from PIL import Image #Used for general image manipulation
import os
from tqdm import tqdm

def IMG_32_tile(image_name):
    """

    Slices the image into 32x32 pixel tiles. Saves to the folder 'sliced_32'.
    Make sure the folder exists in the same folder as the script.

    """

    img_to_slice = Image.open(image_name)
    img_width,img_height = img_to_slice.size #Saves the dimensions of the image

    tile_count=0 #This will set the tile number.
    # !!!! Make sure the above matches up with the divison of tiles from Tiled !!!!

    for i in tqdm(range(0,1792,32)): #Nested loop to slice up the image
        for j in range(0,1184,32):

            box = (j, i, j+32, i+32) #Tuple to save the co-ordinates to crop

            save_path = os.path.join(os.getcwd()+'/sliced_32',str(tile_count)+".png") #Where the image will be saved, as well as the image name.
            img_crop = img_to_slice.crop(box) #Make sure to use a separate variable just for this, or the image will be overwritten.
            img_crop.save(save_path,"PNG") #Save path with image name, and the file format. PNG is better than JPEG
            tile_count = tile_count + 1
    
    return True #Optional, but I've added this to make sure the images are saved before it continues

def IMG_32_map(image_name):
    """

    Slices the image into 32x32 pixel tiles. Saves to the folder 'sliced_32'.
    Make sure the folder exists in the same folder as the script.

    """

    img_to_slice = Image.open(image_name)
    img_width,img_height = img_to_slice.size #Saves the dimensions of the image

    tile_count=0 #This will set the tile number.
    # !!!! Make sure the above matches up with the divison of tiles from Tiled !!!!

    for i in tqdm(range(0,1792,32)): #Nested loop to slice up the image
        for j in range(0,1184,32):

            box = (j, i, j+32, i+32) #Tuple to save the co-ordinates to crop

            save_path = os.path.join(os.getcwd()+'/map_32',str(tile_count)+".png") #Where the image will be saved, as well as the image name.
            img_crop = img_to_slice.crop(box) #Make sure to use a separate variable just for this, or the image will be overwritten.
            img_crop.save(save_path,"PNG") #Save path with image name, and the file format. PNG is better than JPEG
            tile_count = tile_count + 1
    
    return True #Optional, but I've added this to make sure the images are saved before it continues

def IMG_16_tile(directory_to_iterate):
    """

    This method will go over the 32x32 image folder produced by IMG_32_tile in IMG_utils.py
    It'll slice those images further into 16x16 chunks, and save them.
    Make sure the images are 32x32, as there's a triply nested loop in there, and that scares me

    """
    tile_count = 0
    
    for file_name in tqdm(os.listdir(directory_to_iterate)): #Will go through all the files in the folder
        
        if file_name.endswith(".png"): #Make sure that the files are in png format. can change the code if want to pass image type parameters
            img_to_slice = Image.open(os.path.join(directory_to_iterate,file_name))
            img_width,img_height = img_to_slice.size
            
            subtile_count = 0

            for i in range(0,1792,16): #Oof, triply nested loops. Still, this should be very small
                for j in range(0,1184,16):

                    save_path = os.path.join(os.getcwd()+'/sliced_16',str(tile_count)+"_"+str(subtile_count)+".png") #Where the image will be saved, as well as the image name.
                    box = (j, i, j+16, i+16) #Tuple to save the co-ordinates to crop

                    img_crop = img_to_slice.crop(box) #Make sure to use a separate variable just for this, or the image will be overwritten.
                    img_crop.save(save_path,"PNG") #Save path with image name, and the file format. PNG is better than JPEG

                    subtile_count = subtile_count + 1
        
        else:
            continue

        tile_count = tile_count + 1     

    return True #Optional, but I've added this to make sure the images are saved before it continues

#IMG_32_tile("1.png") #for testing
#IMG_16_tile((os.path.join(os.getcwd()+'/sliced_32'))) #for testing