from date_utils import is_valid_date

date_str = input("Введите дату в формате DD.MM.YYYY: ")
if is_valid_date(date_str):
    print("Такая дата может существовать")
else:
    print("Такая дата невозможна")