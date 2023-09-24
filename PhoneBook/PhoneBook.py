# -*- coding: cp1251 -*-

#  Создаем файл 
from pickle import TRUE


def create_file():
    with open('file.txt','w') as data:
        data.write('Имя, Фамилия, 892020 \n')
        data.write('Имя, Фамилия, 892020 \n')

#  Читаем файл 
def read_file():
      path = 'file.txt'
      data = open('file.txt', 'r')
      for line in data:
            print(line, end ='')
      data.close

#  Ввод данных 
def write_data():
      second_name  = input("Введите фамилию: ") 
      first_name = input("Введите имя: ")    
      phone = input("Введите номер телефона: ")   
      write_person(second_name, first_name, phone)

#  Запись данных 
def write_person(second_name, first_name, phone):
      with open('file.txt','a') as f:
            f.write(f'\n {second_name}, {first_name}, {phone}')

#  Поиск человека
def find_person():
      second_name  = input("Введите фамилию: ") 
      first_name = input("Введите имя: ")    
      phone = input("Введите номер телефона: ")   
      data = open('file.txt', 'r')
      for line in data:
            if second_name or first_name or phone:
                  print(data.readline())
      data.close()

def delete_contact():
    second_name  = input("Введите удаляемое фамилию: ") 
    first_name = input("Введите удаляемое имя: ")    
    with open('file.txt','r') as f:
        lines = f.readlines()
    with open('file.txt','w') as f:
        contact_found = False
        for line in lines:
            contact = line.strip().split(', ')
            if (second_name not in contact[0]) or (first_name not in contact[1]):
                f.write(line)
            else:
                contact_found = True
        if contact_found:
            print("Контакт удален")
        else:
            print("Контакт не найден")