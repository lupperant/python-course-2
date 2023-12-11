# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Circle:
    def __init__(self, radius: float, x: float, y: float):
        """
                   Объект "Круг"

                   :param radius: радиус круга
                   :param x: абсцисса центра круга
                   :param y: ордината центра круга
                   Примеры:
                   >>> circle = Circle(100, 0, 0)  # инициализация экземпляра класса
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if not isinstance(x, (int, float)):
            raise TypeError("Абсцисса должна быть типа int или float")
        if not isinstance(y, (int, float)):
            raise TypeError("Ордината должна быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
        self.x = x
        self.y = y

    def scale(self, scale_coefficient: float) -> None:
        """
                    Функция которая масштабирует круг
                    :param scale_coefficient: Коэффициент масштабирования
                    Примеры:
                    >>> circle = Circle(100, 0, 0)
                    >>> circle.scale(1.5)
        """
        if not isinstance(scale_coefficient, (int, float)):
            raise TypeError("Коэффициент масштабирования должен быть типа int или float")
        ...

    def transfer(self, new_x: float, new_y: float) -> None:
        """
                    Функция которая перемещает круг
                    :param new_x: новая абсцисса центра круга
                    :param new_y: новая ордината центра круга
                    Примеры:
                    >>> circle = Circle(100, 0, 0)
                    >>> circle.transfer(1.5, 1)
        """
        if not isinstance(new_x, (int, float)):
            raise TypeError("Абсцисса должна быть типа int или float")
        if not isinstance(new_y, (int, float)):
            raise TypeError("Ордината должна быть типа int или float")
        ...

    def change_radius(self, new_radius: float) -> None:
        """
                Функция которая меняет радиус круга
                :param new_radius: новый радиус круга
                :raise ValueError: Если радиус отрицательный, то возвращаем ошибку
                Примеры:
                >>> circle = Circle(100, 0, 0)
                >>> circle.change_radius(1.5)
        """
        if new_radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        if not isinstance(new_radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        ...


class Student:
    def __init__(self, name: str, year: int, status: str):
        """
                Объект "Студент"
                :param name: имя студента
                :param year: год обучения студента
                :param status: статус обучения студента
                Примеры:
                >>> student = Student("Pupkin", 1, "in progress")  # инициализация экземпляра класса
        """
        if not isinstance(year, int):
            raise TypeError("Год обучения студента должен быть типа int")
        if not isinstance(name, str):
            raise TypeError("Имя студента должна быть типа str")
        if not isinstance(status, str):
            raise TypeError("Статус студента должна быть типа str")
        if not (1 <= year <= 4):
            raise ValueError("Год обучения студента должен входить в рамки 1:4")
        self.name = name
        self.year = year
        self.status = status

    def deduct_student(self) -> None:
        """
                Функция для отчисления студента
                Примеры:
                >>> student = Student("Pupkin", 1, "in progress")
                >>> student.deduct_student()
        """
        self.status = "deducted"

    def raise_year(self) -> None:
        """
                Функция для перевода студента на новый курс
                Примеры:
                >>> student = Student("Pupkin", 1, "in progress")
                >>> student.raise_year()
        """
        if self.year < 4:
            self.year += 1
        else:
            self.status = "finished"


class Square:
    def __init__(self, width: float, position=(0, 0)):
        """
                        Объект "Квадрат"
                        :param width: ширина квадрата
                        :param position: координаты центра квадрата
                        Примеры:
                        >>> square = Square(1)  # инициализация экземпляра класса
        """
        if not isinstance(width, (float, int)):
            raise TypeError("Ширина квадрата должна быть типа int или float")
        if not isinstance(position[0], (float, int)) or not (position[1], (float, int)):
            raise TypeError("Координаты центра квадрата быть типа int или float")
        self.width = width
        self.position = position

    def compute_square(self) -> float:
        """
                Функция для вычисления площади квадрата
                :return: площадь квадрата
                Примеры:
                >>> square = Square(1)
                >>> square.compute_square()
        """
        ...

    def compute_perimeter(self) -> float:
        """
                Функция для вычисления периметра квадрата
                :return: периметр квадрата
                Примеры:
                >>> square = Square(1)
                >>> square.compute_perimeter()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
