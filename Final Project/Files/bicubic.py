import os
import glob as glob
from PIL import Image
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# creating low resolution images from high resolution images

paths=['input/Set5/original','input/Set14/original']
imgs=[]

for path in paths:
    imgs.extend(glob.glob(f'{path}/*.png'))
print(len(imgs))

# making directory paths
scale_fac=0.5
os.makedirs('input/test_bicubic_rgb_2x', exist_ok=True)
save_path_lr = 'input/test_bicubic_rgb_2x'
os.makedirs('input/test_hr', exist_ok=True)
save_path_hr = 'input/test_hr'

# creating low resolution images from high resolution images
fig, axs=plt.subplots(2, 10, figsize=(20, 20))

i=0
images=[]
for image in imgs:
    i+=1
    if (i<=10):
        orig_img = Image.open(image)
        image_name = image.split(os.path.sep)[-1]
        w, h = orig_img.size[:]
        print(f"Original image dimensions: {w}, {h}")
        # orig_img.save(f"{save_path_hr}/{image_name}")
        low_res_img = orig_img.resize((int(w*scale_fac), int(h*scale_fac)), Image.BICUBIC)
        # Upscale using BICUBIC.
        high_res_upscale = low_res_img.resize((w, h), Image.BICUBIC)
        # high_res_upscale.save(f"{save_path_lr}/{image_name}")
        
        images.extend([orig_img, low_res_img])
    else :
        break

# comparing the low and high res images.
# these will be later tested.

# displaying the images using matplotlib

for ax, img in zip(axs.flat, images):
    ax.imshow(img, cmap='gray')  # Display the image in grayscale
    ax.axis('off')  # Hide the axis

plt.tight_layout()
plt.savefig('outputs/degraded_images.png')
plt.show()