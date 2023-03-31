# Линейные структуры данных (массивы, списки, очереди, стеки) более понятны интуитивно. Но как же хранить в памяти
# деревья? Здесь нам поможет знание объектно-ориентированного программирования, а воспользуемся мы принципом,
# по которому хранятся списки в памяти. Напомним, что каждый элемент списка хранит собственное значение и указатель
# на следующий элемент.

class BinaryTree :
    def __init__(self, value) :
        self.value = value
        self.left_child = None
        self.right_child = None

    # Мы создали класс узла, а в конструкторе записали значение, которое должно храниться в нём. Также инициализировали
    # левого и правого потомка. Пока что в них ничего не хранится — нужно иметь процедуру вставки новых элементов. Напишем
    # разные методы для вставки на место левого потомка и на место правого потомка.

    def insert_left(self, next_value) :
        if self.left_child is None :
            self.left_child = BinaryTree(next_value)
        else :
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    # Поясним, что здесь произошло. Если в текущем узле нет левого потомка, то новый узел вставляем на его место.
    # Если левый потомок уже существует — он становится таким же левым потомком, но уже нового узла. Иными словами,
    # он остается левым, но его глубина увеличивается. Аналогично поступим с правым.

    def insert_right(self, next_value) :
        if self.right_child is None :
            self.right_child = BinaryTree(next_value)
        else :
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self) :
        print(self.value)  # процедура обработки

        if self.left_child is not None :  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно обрабатываем функцию

        if self.right_child is not None :  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self) :
        if self.left_child is not None :  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None :  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    def in_order(self) :
        if self.left_child is not None :  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None :  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию


# Создание дерева на основе класса BinaryTree
# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)
print(f"Корневой узел {node_root.value}, левый узел {node_root.left_child.value}, правый узел {node_root.right_child.value} ")
print(f"Потомок узла 7 - левый узел {node_7.left_child.value}")
print(f"Потомок узла 7 - правый узел {node_6.value}, его левый потомок {node_6.left_child.value}, правый потомок {node_6.right_child.value}")
print(f"Потомок узла 5 - {node_5.right_child.value} его левый потомок {node_9.left_child.value}")

print("Давайте посмотрим, в каком порядке будет производиться инфиксный обход дерева в глубину на примере созданного нами дерева.")
node_root.in_order()