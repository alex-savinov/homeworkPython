# -*- coding: cp1251 -*-
"""
������ 36: �������� ������� print_operation_table(operation, num_rows=6, num_columns=6),
������� ��������� � �������� ��������� �������, ����������� ������� �� ������ ������ � �������.
��������� num_rows � num_columns ��������� ����� ����� � �������� �������,
������� ������ ���� �����������. ��������� ����� � �������� ���� � �������
(���������, ������ �� � ����). ����������: �������� ��������� ���������� ����� ��������,
� ������� ����� ��� ���������, ���, ��������, � �������� ���������.
"""
def print_operation_table(operation, num_rows=8, num_columns=8):
      for row in range(1, num_rows+1):
            for column in range(1, num_columns+1):
                  result = operation(row, column)
                  print(result, end='\t')
            print()
            
print_operation_table(lambda x, y: x * y)