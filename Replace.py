from PIL import Image
import os, glob

def resize_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # input(dir_path)
    path = dir_path + '/CardImages/'
    path2 = dir_path + '/ResizedImages/'
    bigpath = dir_path + '/ResizedImages/LargerResizedImages/'
    planet_path = dir_path + '/PlanetImages/'
    damage_tokens_path = dir_path + '/damagetokens/'
    damage_tokens_400x400_path = dir_path + '/400x400damagetokens/'
    # input(path)
    # input(path2)
    dirs = os.listdir(path)
    image_list = []
    planet_image_list = []
    resized_images = []
    resized_damage_images = []
    big_resized_images = []
    filenames = []
    damage_token_names = []
    big_ratio = 0.4
    ratio = 0.17

    playmat_image = Image.open(dir_path + '/Playmat.png')
    playmat_image = playmat_image.resize((1200, 500))
    playmat_image.save('{}{}'.format(dir_path + '/Playmat', '.png'))

    imperial_image = Image.open(dir_path + '/ImperialAquila.jpg')
    imperial_image = imperial_image.resize((1200, 700))
    imperial_image.save('{}{}'.format(dir_path + '/ImperialAquila', '.jpg'))

    resources_image = Image.open(dir_path + '/Netrunner_credit.png')
    resources_image = resources_image.resize((50, 50))
    resources_image.save('{}{}'.format(dir_path + '/Netrunner_credit', '.png'))

    for token in glob.glob(damage_tokens_400x400_path+'*.png'):
        print(token)
        base_name = os.path.basename(token)
        name, ext = os.path.splitext(base_name)
        damage_token_names.append(name)
        img = Image.open(token)
        img = img.convert("RGB")
        img = img.resize((int(30), int(30)))
        resized_damage_images.append(img)


    for (a, new) in enumerate(resized_damage_images):
        new.save('{}{}'.format(damage_tokens_path + damage_token_names[a], '.png'))

    for filename in glob.glob(path+'*.webp'):
        print(filename)
        base_name = os.path.basename(filename)
        name, ext = os.path.splitext(base_name)
        filenames.append(name)
        img = Image.open(filename)
        img = img.convert("RGB")
        image_list.append(img)

    for image in image_list:
        small_image = image.resize((int(365 * ratio), int(520 * ratio)))
        resized_images.append(small_image)
        bigger_image = image.resize((int(365 * big_ratio), int(520 * big_ratio)))
        big_resized_images.append(bigger_image)

    for planet_filename in glob.glob(planet_path+'*.webp'):
        print(planet_filename)
        base_name = os.path.basename(planet_filename)
        name, ext = os.path.splitext(base_name)
        filenames.append(name)
        img = Image.open(planet_filename)
        img = img.convert("RGB")
        planet_image_list.append(img)

    for image in planet_image_list:
        image = image.resize((int(520 * ratio), int(365 * ratio)))
        resized_images.append(image)

    for (a, new) in enumerate(resized_images):
        new.save('{}{}{}'.format(path2, filenames[a], '.jpg'))
    for (a, new) in enumerate(big_resized_images):
        new.save('{}{}{}'.format(bigpath, filenames[a], '.jpg'))
