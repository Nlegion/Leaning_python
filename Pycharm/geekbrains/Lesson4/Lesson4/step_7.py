import sys

# print(sys.argv)
# src_data = input('введите дату: ').split()
src_data = sys.argv[1:]

# print(src_data, type(src_data))

if len(src_data) == 3:
    day, month, year = src_data
    print(day, month, year)
