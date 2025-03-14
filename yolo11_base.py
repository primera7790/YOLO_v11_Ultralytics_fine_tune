from ultralytics import YOLO

model = YOLO('yolo11n.pt')

img_path = 'all_data/01001000028.jpg'

result = model(img_path)

for i in result:
    print(i.boxes)