import datetime
birth_year = input("Nhập năm sinh của bạn: ")
birth_year = int(birth_year)
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"Tuổi của bạn là: {age} tuổi.")