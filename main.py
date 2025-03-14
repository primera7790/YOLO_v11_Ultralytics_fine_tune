from files_configure import dataset_organize, dataset_back_organize
from yolo11_train import train, predict


def main():
    # dataset_organize(back_num=False)
    # dataset_back_organize(change_num=True)
    # train()
    predict(image='datasets/vehicle/images/train/01001000049.jpg')


if __name__ == '__main__':
    main()