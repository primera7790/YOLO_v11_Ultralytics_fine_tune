from ultralytics import YOLO

from files_configure import dataset_organize, dataset_back_organize, change_class_num


def train():
    model = YOLO('yolo11n.pt')

    for k, v in model.named_parameters():
        v.requires_grad = False

    model.train(
        data='datasets/vehicle/vehicle.yaml',
        classes=[0, 1, 2, 3, 4, 5, 6],
        epochs=10,
        imgsz=416,
        val=True,
        project='model_save'
    )

    return model


def predict(image):
    model = YOLO('model_save/train/weights/best.pt')

    results = model(image)

    for result in results:
        result.show()


