from files_configure import dataset_organize, dataset_back_organize, dataset_load
from yolo11 import train, predict, base_predict


def main():
    # dataset_load()
    # dataset_organize(back_num=False)
    # dataset_back_organize(change_num=True)

    # train()

    predict(image='all_data/01001000049.jpg')
    # base_predict(image='all_data/01001000049.jpg')


if __name__ == '__main__':
    main()