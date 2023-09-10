# -*- coding: cp1251 -*-
"""
������ 24: � ���������� ��������� � ������� ���������� �������.
��� ����� �� ������� ������, ������ ����� �������� ������ �� ����������. 
����� �������, � ������� ����� ���� ����� ��� ��������. ����� �� ������ ����� N ������.
��� ����� �������� ������ ������������, ������� �� ������� ����� �� ��� ������� ��������� ����� ���� � �� i-�� ����� ������� ai ����.
� ���� ���������� ��������� �������� ������� ��������������� ����� �������. 
��� ������� ������� �� ������������ ������ � ���������� ���������� �������.
���������� ������ �� ���� �����, �������� ��������������� ����� ��������� ������, �������� ����� � ����� ����� � � ���� �������� � ���.
�������� ��������� ��� ���������� ������������� ����� ����, ������� ����� 
������� �� ���� ����� ���������� ������, �������� ����� ��������� ������ �������� �� ������� ����� ������.
"""

def func_blueberries(bush, blueberries):
    sum_blueberries_bush = []
    sum_buffer = 0
    i = 0
    if bush > 2:
        while (i < bush):
            if (i != bush - 1):
                sum_buffer = blueberries[i] + blueberries[i - 1] + blueberries[i + 1]
            else:
                sum_buffer = blueberries[i] + blueberries[i -1] + blueberries[0]
            sum_blueberries_bush.append( sum_buffer)
            i += 1
        sum_blueberries_bush.sort(reverse = True)
        print(f"������������ ����� ���� �� ���� ����: {sum_blueberries_bush[0]}")
    else:
        for k in range(bush):
            sum_buffer = sum_buffer + blueberries[k]
        print(f"������������ ����� ���� �� ���� ����: {sum_buffer}")

import random
bush = int(input("������� ���������� ������: "))
blueberries = list(random.randint(0, 10) for i in range(bush))
print(blueberries)
func_blueberries(bush,blueberries)
