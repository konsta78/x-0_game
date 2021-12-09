# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Панфилов К. Ю.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class Glass:
    def __init__(self, capacity=200, occupied=0):
        if not isinstance(capacity, (int, float)):
            raise TypeError('Capacity must be int or float')
        if not isinstance(occupied, (int, float)):
            raise TypeError('Occupied must be int or float')
        if capacity < 0 or occupied < 0:
            raise ValueError('Capacity and occupied must be > 0')
        if occupied > capacity:
            raise ValueError('Capacity must be more than occupied')

        self.capacity_volume = capacity
        self.occupied_volume = occupied

    def __str__(self):
        return f"Стакан объемом {self.capacity_volume} заполнен {self.occupied_volume}"

    def __repr__(self): #надо почитать и разобраться
        return "---"

# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.


glass1 = Glass(100, 0)
glass2 = Glass(200, 100)
glass3 = Glass(300)
glass3.occupied_volume = 290
print("Glass 1: ", glass1)
print("Glass 2: ", glass2)
print("Glass 3: ", glass3)


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    occupied_volume = 0

    def __init__(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError('Occupied must be int or float')
        if occupied_volume < 0:
            raise ValueError('Occupied must be > 0')

        self.occupied_volume = occupied_volume


gl1 = GlassDefaultArg
gl2 = GlassDefaultArg(200)

print("Glass 1: ", gl1.occupied_volume)
print("Glass 2: ", gl2.occupied_volume)

# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?
  

 class GlassDefaultListArg:
     def __init__(self, capacity_volume, occupied_volume=[]):
         self.capacity_volume = capacity_volume




# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.


class GlassAddRemove:
    def __init__(self, capacity, occupied):
        if not isinstance(capacity, (int, float)):
            raise TypeError('Capacity must be int or float')
        if not isinstance(occupied, (int, float)):
            raise TypeError('Occupied must be int or float')
        if capacity < 0 or occupied < 0:
            raise ValueError('Capacity and occupied must be > 0')
        if occupied > capacity:
            raise ValueError('Capacity must be more than occupied')

        self.capacity_volume = capacity
        self.occupied_volume = occupied

    def add_water(self, volume):
        if self.occupied_volume + volume > self.capacity_volume:
            raise ValueError('Стакан переливается через край...')
        self.occupied_volume += volume

    def remove(self):
        self.occupied_volume = 0


glass_one = GlassAddRemove(500, 0)
print(glass_one.capacity_volume, glass_one.occupied_volume)
glass_one.add_water(300)
print(glass_one.capacity_volume, glass_one.occupied_volume)
glass_one.remove()
print(glass_one.capacity_volume, glass_one.occupied_volume)



# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и классаcapacity_volume
#    б. Проверьте тип созданного объекта.




# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.



# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.



"""
class d:
	def __init__(f, a=2):
		f.a = a
		
	def print_me(p):
		print(p.a)
		
d.print_me(d())		

# 10. Исправьте
class A:
	def __init__(self, a):
		if 10 < a < 50:
			return
		self.a = a;	

# Объясните так реализовывать __init__ нельзя?
		
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...

"""






















