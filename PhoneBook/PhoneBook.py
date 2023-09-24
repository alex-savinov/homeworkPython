"""
# Создание файла
with open('file.txt','w') as data:
      data.write('Имя, Фамилия, 892020 \n')
      data.write('Имя, Фамилия, 892020 \n')
"""

# Читаем файл 
def read_file():
      path = 'file.txt'
      data = open('file.txt', 'r')
      for line in data:
            print(line, end ='')
      data.close

# Ввод данных 
def write_data():
      second_name  = input("Введите фамилию: ") 
      first_name = input("Введите имя: ")    
      phone = input("Введите номер телефона: ")   
      write_person(second_name, first_name, phone)

# Запись данных 
def write_person(second_name, first_name, phone):
      with open('file.txt','a') as f:
            f.write(f'\n {second_name}, {first_name}, {phone}')

# Поиск человека
def find_person():
      second_name  = input("Введите фамилию: ") 
      first_name = input("Введите имя: ")    
      phone = input("Введите номер телефона: ")   
      data = open('file.txt', 'r')
      for line in data:
            if second_name or first_name or phone:
                  print(data.readline())
      data.close()

