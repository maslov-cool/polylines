# polylines
В игре Lines игроку постоянно добавляются на поле разноцветные шарики (в списке board их можно моделировать целыми числами, ноль означает, что шарика нет).  Игрок может выбрать любой шарик и указать ему клетку, в которую тот должен попасть. Перемещение шарика начинается только тогда, когда есть «проход» из стартовой клетки в финишную.
В нем реализуйте метод has_path(self, x1, y1, x2, y2), возвращающий логическое значение True или False в зависимости от того, есть путь из клетки (x1, y1) в клетку (x2, y2) или нет.

Для этого можно использовать так называемый «волновой» алгоритм, а можно применить и другие методы.

Поведение игры должно быть следующим:

Если мы щелкаем мышкой на пустой клетке, то в нее ставится «синий» шарик.
Если мы щелкаем мышкой на «синем» шарике, то он становится «красным».
Если мы щелкаем мышкой на «красном» шарике, то он становится «синим».
Если на поле есть красный шарик, а мы щелкаем на пустой клетке, то надо проверить наличие пути из клетки с красным шариком в эту клетку, и если таковой есть, то создать в клетке синий шарик, а красный шарик удалить (смоделировать переход шарика).
Если пути нет, то ничего не происходит.

перемещение шарика «по шагам»: при наличии пути из стартовой клетки в финишную шарик должен «побывать» во всех промежуточных, а игрок должен это увидеть. с оптимальным маршрутом волновым алгоритмом(обход в ширину)
