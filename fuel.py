fract = input("Дробь: ")
fract = fract.split("/")
try:
    percent = (int(fract[0]) / int(fract[1])) * 100
except ZeroDivisionError:
    fract = input("Дробь: ")
    fract = fract.split("/")
except ValueError:
    fract = input("Дробь")
    fract = fract.split("/")
except fract[0] > fract[1]:
    fract = input("Дробь: ")
    fract = fract.split("/")
finally:
    percent = (int(fract[0]) / int(fract[1])) * 100
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(str(round(percent))+"%")
