
def calculate_salary(base_salary, bonus_rate=.1):
''' 
base_salary (float): Lương cơ bản.
bonus_rate (float): Tỷ lệ thưởng, mặc định là 0.1.
'''
  return base_salary * (1 + bonus_rate)

def calculate_bonus(total_salary, base_salary):
'''
total_salary (float)**: Tổng lương.
base_salary (float)**: Lương cơ bản.
'''
  return (total_salary - base_salary) / base_salary
