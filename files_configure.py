import os
import re
import shutil
import random

import kaggle
import yaml
from glob import glob


def dataset_load():
    # Вариант 1. Авторизуем API, скачиваем с Kaggle и распаковываем в папку data
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('brasarkaya/vehicle-color-dataset', path='.', unzip=True)

    # Вариант 2. Собственноручно скачиваем архив по ссылке, распаковываем в папку all_data
    # Dataset: https://www.kaggle.com/datasets/brasarkaya/vehicle-color-dataset/data

    return


def data_yaml_init():
    data = {
        'path': '../datasets/vehicle',
        'train': 'images/train',
        'val': 'images/val',
        'names': {
            0: 'white_car',
            1: 'red_car',
            2: 'gray_car',
            3: 'blue_car',
            4: 'black_car',
            5: 'yellow_car',
            6: 'green_car'}
    }

    with open('datasets/vehicle/vehicle.yaml', 'w') as file:
        yaml.dump(data, file)

    return


def change_class_num(names_list, back=False):
    difference = -15 if not back else 15
    for name in names_list:
        new_lines_list = []
        with open(f'all_data/{name}.txt', 'r') as file:
            for line in file:
                if line == '':
                    continue
                line = line.strip()
                class_idx, x_coord, y_coord, width, height = line.split(' ')
                class_idx = str(int(class_idx) + difference)
                new_lines_list.append(' '.join([class_idx, x_coord, y_coord, width, height]) + '\n')
        with open(f'all_data/{name}.txt', 'w') as file:
            file.writelines(new_lines_list)

    return


def dataset_organize(back_num=False):
    lpg_files_list = glob(pathname='all_data/*.jpg')
    names_list = [re.sub('\D', '', name) for name in lpg_files_list]

    change_class_num(names_list, back=back_num)

    random.shuffle(names_list)
    train_num = int(len(names_list) * 0.8)
    train_names = names_list[:train_num]
    val_names = names_list[train_num:]

    for file_name in train_names:
        shutil.move(f'all_data/{file_name}.jpg', f'datasets/vehicle/images/train/{file_name}.jpg')
        shutil.move(f'all_data/{file_name}.txt', f'datasets/vehicle/labels/train/{file_name}.txt')

    for file_name in val_names:
        shutil.move(f'all_data/{file_name}.jpg', f'datasets/vehicle/images/val/{file_name}.jpg')
        shutil.move(f'all_data/{file_name}.txt', f'datasets/vehicle/labels/val/{file_name}.txt')

    data_yaml_init()

    return


def dataset_back_organize(change_num=True):
    dirs_list = ['images/train/', 'images/val/', 'labels/train/', 'labels/val/']

    for dir_name in dirs_list:
        path_to_dataset = 'datasets/vehicle/'
        names_list = os.listdir(f'{path_to_dataset}{dir_name}')
        for name in names_list:
            shutil.move(f'{path_to_dataset}{dir_name}{name}', f'all_data/{name}')

    if change_num:
        lpg_files_list = glob(pathname='all_data/*.jpg')
        names_list = [re.sub('\D', '', name) for name in lpg_files_list]
        change_class_num(names_list, back=True)

    return


if __name__ == '__main__':
    data_yaml_init()
    # dataset_organize()
    # dataset_back_organize()
