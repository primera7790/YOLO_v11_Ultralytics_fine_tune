## YOLO v11 Ultralytics fine tuning

### Технологии:
- Язык: &nbsp; `python` ;
- Библиотеки: &nbsp; `ultralytics`, `kaggle`, `yaml` , `glob`, `shutil`, `re` ;
- CV-модели: &nbsp; `YOLO` .
  
### Описание:

&nbsp; &nbsp; **Задача:** &nbsp; переобучение модели Yolo11 под задачу классификации цветов автомобилей; <br>
&nbsp; &nbsp; **Данные:** &nbsp; датасет kaggle `vehicle-color-dataset` ; <br>
&nbsp; &nbsp; **Реализация:** <br>
&nbsp; &nbsp; &nbsp; - &nbsp; подгружаем датасет; <br>
&nbsp; &nbsp; &nbsp; - &nbsp; меняем структуру данных под YOLO формат; <br>
&nbsp; &nbsp; &nbsp; - &nbsp; забираем модель Yolo11 с обученными весами; <br>
&nbsp; &nbsp; &nbsp; - &nbsp; настраиваем параметры (замораживаем желаемые веса, меняем выходной слой классификатора); <br>
&nbsp; &nbsp; &nbsp; - &nbsp; инициируем дообучение. <br>
