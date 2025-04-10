from PIL import Image, ImageCms
from glob import glob
import os
# # Open the CMYK image

# images = glob('structures_2_cmyk_1024\\structures_2_cmyk_1024\*')

# print(images)

# for image in images:
#     cmyk_image = Image.open(image)

#     image_name = image.split("\\")[-1][:-5]

#     # Define the path to the ICC profiles
#     cmyk_profile_path = "CMYK\\USWebUncoated.icc"  # CMYK profile
#     rgb_profile_path = "sRGB Color Space Profile.icm"  # RGB profile

#     # Build the transform from CMYK to RGB using ICC profiles
#     cmyk_to_rgb_transform = ImageCms.buildTransform(cmyk_profile_path, rgb_profile_path, 'CMYK', 'RGB')

#     # Apply the ICC profile conversion
#     rgb_image = ImageCms.applyTransform(cmyk_image, cmyk_to_rgb_transform)

#     # Save the converted image
#     rgb_image.save(f"structures_2_rgb_1024\\{image_name}.jpg")


## portrait
folder_base = "portrait"
os.makedirs(f"portrait_converted", exist_ok = True)


image_size = (250, 250)
grid_size = (5, 5)
spacing = 50
background_color = (0, 0, 0)
# Calculate final image size
grid_width = grid_size[0] * image_size[0] + (grid_size[0] + 1) * spacing
grid_height = grid_size[1] * image_size[1] + (grid_size[1] + 1) * spacing


for n in range(1800):

    final_image = Image.new("RGB", (grid_width, grid_height), background_color)

    for i,N in enumerate(range(10, 60, 10)):
        for j,L in enumerate(range(10, 60, 10)):

            x = spacing + i * (image_size[0] + spacing)
            y = spacing + j * (image_size[1] + spacing)
            prefix = str(n)
            prefix_size = len(prefix)

            filename = "".join(["0" for j in range( 5 - prefix_size )] + [str(n)] )

            image_path = f"{folder_base}/{N}_{L}/{filename}.jpeg"
            with Image.open(image_path) as img:
                img = img.resize(image_size)
                final_image.paste(img, (x, y))
            
    final_image.save(f"portrait_converted/{filename}.jpeg")