from PIL import Image
import os, glob

def resize_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # input(dir_path)
    path = dir_path + '/CardImages/'
    path2 = dir_path + '/ResizedImages/'
    planet_path = dir_path + '/PlanetImages/'
    # input(path)
    # input(path2)
    dirs = os.listdir(path)
    image_list = []
    planet_image_list = []
    resized_images = []
    filenames = []
    ratio = 0.17

    playmat_image = Image.open(dir_path + '/Playmat.png')
    playmat_image = playmat_image.resize((1200, 500))
    playmat_image.save('{}{}'.format(dir_path + '/Playmat', '.png'))

    for filename in glob.glob(path+'*.webp'):
        print(filename)
        base_name = os.path.basename(filename)
        name, ext = os.path.splitext(base_name)
        filenames.append(name)
        img = Image.open(filename)
        image_list.append(img)

    for image in image_list:
        image = image.resize((int(365 * ratio), int(520 * ratio)))
        resized_images.append(image)

    for planet_filename in glob.glob(planet_path+'*.webp'):
        print(planet_filename)
        base_name = os.path.basename(planet_filename)
        name, ext = os.path.splitext(base_name)
        filenames.append(name)
        img = Image.open(planet_filename)
        planet_image_list.append(img)

    for image in planet_image_list:
        image = image.resize((int(520 * ratio), int(365 * ratio)))
        resized_images.append(image)

    for (a, new) in enumerate(resized_images):
        new.save('{}{}{}'.format(path2, filenames[a], '.jpg'))