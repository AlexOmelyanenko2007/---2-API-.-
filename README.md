# 2-API
Проект для Яндекс Лицея, по API


## Шаблон проекта
![image](https://user-images.githubusercontent.com/94148371/216944539-72262f92-072b-4d4f-a5bd-a0ea6b7a6cde.png)


## Техническое задание
- [x]  Создать оконное приложение, отображающее карту по координатам в масштабе, который задается программно.
- [x]  Добавить обработку клавиш PgUp и PgDown, по нажатию на которые соответственно увеличивать и уменьшать масштаб отображения карты. Необходимо отслеживать предельные значения, за которые значения переменных не должны заходить.
- [ ]  Добавить обработку клавиш вверх/вниз/вправо/влево, по нажатию на которые перемещать центр карты в соответствующую сторону на размер экрана. Также необходимо отслеживать предельные значения координат.
- [ ]  Добавить переключатель слоёв карты (схема/спутник/гибрид), при изменении которого менять вид карты.
- [ ]  Добавить текстовое поле, в которое можно ввести запрос для поиска объекта. По завершению ввода (например, при нажатии на кнопку «Искать») требуется найти указанный объект, спозиционировать карту на его центральную точку, добавить метку на карту в центральную точку объекта.
- [ ]  Сохранить метку при изменении масштаба, движении или изменении вида карты.
- [ ]  Добавить кнопку «сброс поискового результата», по нажатию на которую точка найденного объекта сбрасывается.
- [ ]  Добавить поле для вывода полного адреса найденного объекта. В нем должен отображаться адрес найденного объекта. Адрес должен сбрасываться по «сбросу поискового результата».
- [ ]  Добавить переключатель, включающий и выключающий приписывание почтового индекса к полному адресу объекта.
- [ ]  Переписывать адрес при изменении значения переключателя.
- [ ]  Добавьте возможность найти объект по клику левой кнопкой мыши в карту. Поведение должно быть таким же, как при новом поиске (сброс старых результатов, постановка новой метки, выведение адреса согласно значению переключателя), кроме изменения положения карты.
- [ ]  Добавьте возможность найти организацию в заданной точке по клику правой кнопкой мыши в карту. Выводить первую найденную организацию при условии, что ее координаты находятся не дальше 50 метров от запрошенной точки. В противном случае не выводить ничего. Данная организация сбрасывает значения, связанные с предыдущим поиском. 
