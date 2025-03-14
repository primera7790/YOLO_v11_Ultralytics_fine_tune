import os

from PIL import Image
from torch.utils.data import Dataset


class DatasetVehicle(Dataset):
    def __init__(self, path, transform=None):
        self.path = path
        self.transform = transform
        self.names_list = sorted(list(set([name[:-4] for name in os.listdir(path)])))
        self.length = len(self.names_list) - 1

        with open(os.path.join(path, 'classes.txt'), 'r') as file:
            self.class_names = [line.strip() for line in file if line.strip()][-7:]
            self.class_names_idx = {cls_name: idx for idx, cls_name in enumerate(self.class_names)}

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        file_name = self.names_list[index]
        img_path = os.path.join(self.path, file_name + '.jpg')
        params_path = os.path.join(self.path, file_name + '.txt')

        params_list = []
        params_list_info = []
        count = 0
        with open(params_path, 'r') as file:
            for line in file:
                if line == '':
                    continue
                line = line.strip()
                class_idx, x_coord, y_coord, width, height = line.split(' ')
                class_name = self.class_names[int(class_idx) - 15]
                count += 1
                params_list.append([int(class_idx) - 15, x_coord, y_coord, width, height])
                params_list_info.append([f'Class: {class_name}',
                                    f'X: {x_coord}',
                                    f'Y: {y_coord}',
                                    f'Width: {width}',
                                    f'Height: {height}'])

        num_bboxes = f'Number of boxes: {count}'
        original_name = f'Original file name: {file_name}'
        img = Image.open(img_path)
#         img.show()

        if self.transform:
            img = self.transform(img)

        return img, params_list, original_name, num_bboxes, params_list_info

    def len_info(self):
        count_list = [0, 0, 0, 0, 0, 0, 0]
        img_names_list = self.names_list.copy()
        img_names_list.remove('classes')
        for name in img_names_list:
            params_path = os.path.join(self.path, name + '.txt')
            with open(params_path, 'r') as file:
                for line in file:
                    if line == '':
                        continue
                    line = line.strip()
                    class_idx = int(line.split(' ')[0]) - 15
                    count_list[class_idx] += 1
        len_info = f'''Images: {self.length}
Bboxes: {sum(count_list)}
Classes:
  {self.class_names[0]}: {count_list[0]}
  {self.class_names[1]}: {count_list[1]}
  {self.class_names[2]}: {count_list[2]}
  {self.class_names[3]}: {count_list[3]}
  {self.class_names[4]}: {count_list[4]}
  {self.class_names[5]}: {count_list[5]}
  {self.class_names[6]}: {count_list[6]}'''
        print(len_info)
        return