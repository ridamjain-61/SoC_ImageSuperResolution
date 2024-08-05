from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt
from patchify import patchify, unpatchify
import numpy as np
import matplotlib.gridspec as gridspec
import glob as glob
import os
import cv2
SHOW_PATCHES = False
STRIDE = 14
SIZE = 32

# Function to create patches from images
# using patchify to create patches to increase the training dataset size.


def create_patches(input_path, output_hr_path, output_lr_path):
    paths=[]
    
    paths.extend(glob.glob(f"{input_path}/*"))
    # adding all the files in paths list.
    print(len(paths))

    for img_path in tqdm(paths, total=len(paths)):
        img=Image.open(img_path)
        name = img_path.split(os.path.sep)[-1].split('.')[0]
        w,h=img.size
        patches =patchify(np.array(img), (32, 32, 3), STRIDE)
        
        # print(patches.shape)
        
        counter=0
        
        for i in range(patches.shape[0]):
            for j in range(patches.shape[1]):
                counter+=1
                patch=patches[i,j,0,:,:,:]
                patch=cv2.cvtColor(patch, cv2.COLOR_RGB2BGR)
                cv2.imwrite(f'{output_hr_path}/{name}_{counter}.png',patch)

                h, w, _ = patch.shape
                low_res_img = cv2.resize(patch, (int(w*0.5), int(h*0.5)), 
                                        interpolation=cv2.INTER_CUBIC)
                # Now upscale using BICUBIC.
                high_res_upscale = cv2.resize(low_res_img, (w, h), 
                                            interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(
                    f"{output_lr_path}/{name}_{counter}.png",
                    high_res_upscale
                )



create_patches('input/T91','input/91_hr','input/91_lr')
