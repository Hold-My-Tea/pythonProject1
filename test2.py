## Реализация на основе использования deque:
# Плюсы:
# Код легче воспринимается, лаконичен
# Быстро выполняется
# Добавление элемента происходит за O(1) и удаление самого старого элемента —
# тоже O(1), что делает его более эффективным
# Минусы:
# Нужно импортировать модуль

from collections import deque

class CircularBufferFIFO:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def add(self, item):
        self.buffer.append(item)

    def get(self):
        return list(self.buffer)

    def __str__(self):
        return str(self.get())


## Реализация на основе списка:
# Плюсы:
# Полный контроль над логикой добавления и получения элементов. Это позволяет легко модифицировать функциональность при необходимости
# Использует стандартный список Python, нет сторонних библиотек
# Минусы:
# Операции обновления размера и индекса могут быть не такими эффективными, как с использованием deque
# При каждом добавлении элемента происходит проверка, что может замедлять операции
# Код более сложный для восприятия из-за необходимости ручного управления индексами и размером буфера

class CircularBufferFIFO2:
    def __init__(self):
        self.buffer = []
        self.index = 0
        self.size = 0

    def add(self, item):
        if self.index < len(self.buffer):
            self.buffer[self.index] = item
        else:
            self.buffer.append(item)
        self.index = (self.index + 1) % (self.size + 1)
        if self.size < len(self.buffer):
            self.size += 1

    def get(self):
        elements = []
        for i in range(self.size):
            index = (self.index - i - 1) % self.size
            elements.append(self.buffer[index])
        return elements

    def __str__(self):
        return str(self.get())
