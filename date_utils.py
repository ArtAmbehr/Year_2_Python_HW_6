# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    
    # Проверяем день
    if day < 1 or day > 31:
        return False
    
    # Проверяем месяц
    if month < 1 or month > 12:
        return False
    
    # Проверяем год
    if year < 1 or year > 9999:
        return False
    
    # Проверяем дни в зависимости от месяца
    if month in [4, 6, 9, 11] and day > 30:
        return False
    
    # Проверяем февраль и високосный год
    if month == 2:
        if is_leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    
    return True