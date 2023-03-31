class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self): # печать с помощью обхода в ширину
        queue = [self] # создаем очередь
        values = [] # значения в порядке обхода в ширину
        while queue != []: # пока она не пустая
            last = queue.pop(0) # извлекаем из начала

        if last is not None :  # если не None
            values.append("%d" % last.value)  # добавляем значение
            print(last, last.value) # в чем отличие?
            queue.append(last.left_child)  # добавляем левого потомка
            queue.append(last.right_child)  # добавляем правого потомка
        return ''.join(values)

    def search(self, x) :
        if self.value == x :  # если нашли элемент,
            return self  # возвращаем ссылку на узел

        elif x < self.value:  # или, если значение меньше ключа, продолжаем
            return self.left_child.search(x)  # поиск в левом поддереве
        elif x > self.value:  # иначе в правом
            return self.right_child.search(x)
        else :  # если такое значение не нашлось,
            return False  # возвращаем False

    def minimum(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.minimum()

    def next_value(self, x) :
        current = self
        successor = None
        while current is not None :
            if current.value > x :
                successor = current
                current = current.left_child
            else :
                current = current.right_child
        return successor

    def insert(self, x) :
        if x > self.value :  # идем в правое поддерево
            if self.right_child is not None :  # если оно существует,
                self.right_child.insert(x)  # делаем рекурсивный вызов

            else :  # иначе создаем правого потомка
                self.right_child = BinarySearchTree(x)
        else :  # иначе в левое поддерево и делаем аналогичные действия
            if self.left_child is not None :
                self.left_child.insert(x)
            else :
                self.left_child = BinarySearchTree(x)
        return self  # возвращаем корень

    def delete(self, x) :

        # первым этапом мы должны найти удаляемый узел и его предка
        parent = self
        node = self
        if not self.search(x) :
            return self
        while node.value != x :
            parent = node
            if parent.left_child is not None and x < parent.value :
                node = parent.left_child
            elif parent.right_child is not None and x > parent.value :
                node = parent.right_child
        # по завершении в node хранится искомый узел
        # первый случай - если лист
        if node.left_child is None and node.right_child is None :
            if parent.left_child is node :
                parent.left_child = None
            if parent.right_child is node :
                parent.right_child = None
            if parent.value == x :
                # если нет листов и parent==node до сих пор,
                # значит, нужно вернуть None для корректной работы рекурсии
                return None
        # второй случай - имеет одного потомка
        elif node.left_child is None or node.right_child is None :
            if node.left_child is not None :
                if parent.left_child is node :
                    parent.left_child = node.left_child
            elif parent.right_child is node :
                parent.right_child = node.left_child
        if node.right_child is not None :
            if parent.left_child is node :
                parent.left_child = node.right_child
            elif parent.right_child is node :
                parent.right_child = node.right_child
        else :  # третий случай - имеет двух потомков
            next_ = node.next_value(x).value  # ищем следующее значение
            node.value = next_  # меняем на него
            # делаем рекурсивный вызов
            node.right_child = node.right_child.delete(next_)
        return self

    # Задание 1. Реализуйте функцию поиска максимума в двоичном дереве поиска по
    # аналогии с написанной функцией поиска минимума.
    def maximum(self) :

        if self.right_child is None :
            return self
        else :
            return self.right_child.maximum()

    # Задание 2. Реализуйте функцию поиска предыдущего элемента.
    def prev_value(self, x) :
        current = self
        successor = None
        while current is not None :
            if current.value < x :
                successor = current
                current = current.right_child
            else :
                current = current.left_chilд
        return successor