
start_value = int(input("������� ��������� �������: "))
step_value = int(input("������� ��� ����������: "))
count_step = int(input("������� ���������� ��������: "))
print(*range(start_value,count_step * step_value + start_value,step_value))