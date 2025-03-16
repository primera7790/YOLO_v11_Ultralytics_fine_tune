## YOLO v11 Ultralytics fine tuning

### Технологии:
- Язык: &nbsp; `python` ;
- Библиотеки: &nbsp; `ultralytics`, `kaggle`, `yaml` , `glob`, `shutil`, `re` ;
- CV-модели: &nbsp; `YOLO` .
  
### Описание:

&nbsp; &nbsp; **Задача:** &nbsp; переобучение модели Yolo11 под задачу классификации цветов автомобилей; <br>
&nbsp; &nbsp; **Данные:** &nbsp; датасет kaggle `vehicle-color-dataset` ; <br>

### Реализация:

&nbsp; &nbsp; &nbsp; - &nbsp; подгружаем датасет (может понадобиться авторизация API kaggle, см. https://www.kaggle.com/docs/api); <br>
&nbsp; &nbsp; &nbsp; - &nbsp; меняем структуру данных под Ultralytics YOLO format, см. https://docs.ultralytics.com/datasets/detect/; <br>
&nbsp; &nbsp; &nbsp; - &nbsp; забираем модель Yolo11 с обученными весами; <br>
&nbsp; &nbsp; &nbsp; - &nbsp; настраиваем параметры (замораживаем желаемые веса, меняем выходной слой классификатора); <br>
&nbsp; &nbsp; &nbsp; - &nbsp; инициируем дообучение. <br>
