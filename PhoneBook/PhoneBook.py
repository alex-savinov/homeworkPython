# -*- coding: cp1251 -*-

#  ������� ���� 
from pickle import TRUE


def create_file():
    with open('file.txt','w') as data:
        data.write('���, �������, 892020 \n')
        data.write('���, �������, 892020 \n')

#  ������ ���� 
def read_file():
      path = 'file.txt'
      data = open('file.txt', 'r')
      for line in data:
            print(line, end ='')
      data.close

#  ���� ������ 
def write_data():
      second_name  = input("������� �������: ") 
      first_name = input("������� ���: ")    
      phone = input("������� ����� ��������: ")   
      write_person(second_name, first_name, phone)

#  ������ ������ 
def write_person(second_name, first_name, phone):
      with open('file.txt','a') as f:
            f.write(f'\n {second_name}, {first_name}, {phone}')

#  ����� ��������
def find_person():
      second_name  = input("������� �������: ") 
      first_name = input("������� ���: ")    
      phone = input("������� ����� ��������: ")   
      data = open('file.txt', 'r')
      for line in data:
            if second_name or first_name or phone:
                  print(data.readline())
      data.close()

def delete_contact():
    second_name  = input("������� ��������� �������: ") 
    first_name = input("������� ��������� ���: ")    
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
            print("������� ������")
        else:
            print("������� �� ������")