import matplotlib.pyplot as plt
from PIL import Image
plt.style.use('ggplot')
images=[]

# displaying the before and after images after our regeneration.

fig, axs = plt.subplots(5, 5)
for i in range(5):

    path1=f'outputs/valid_results/val_sr_{50*i+25}_3.png'
    path2=f'outputs/valid_results/val_sr_{50*i+25}_7.png'
    path3=f'outputs/valid_results/val_sr_{50*i+25}_8.png'
    path4=f'outputs/valid_results/val_sr_{50*i+25}_9.png'
    path5=f'outputs/valid_results/val_sr_{50*i+25}_14.png'

    img1=Image.open(path1)
    img2=Image.open(path2)
    img3=Image.open(path3)
    img4=Image.open(path4)
    img5=Image.open(path5)
    images.append(img1)
    images.append(img2)
    images.append(img3)
    images.append(img4)
    images.append(img5)
    # plt.imshow(img1)
    # plt.imshow(img2)
    # plt.imshow(img3)
    # plt.imshow(img4)
    # plt.imshow(img5)

# improved the clarity of images.

for ax, img in zip(axs.flat, images):
    ax.imshow(img, cmap='gray')  # Display the image in grayscale
    ax.axis('off')  # Hide the axis

plt.tight_layout()

plt.savefig('outputs/collage.png')
plt.show()
