import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_calc import Ui_MainWindow

def checkLen():
    numbers = ui.lineEdit.text().split()
    if len(numbers) == 3:
        return True
    return False

def equals():
    if checkLen():
        numbers = ui.lineEdit.text().split()
        number0 = float(numbers[0])
        number2 = float(numbers[2])
        sign = numbers[1]
        if sign == '+':
            number = number0 + number2
        elif sign == '/':
            number = number0/number2
        elif sign == '*':
            number = number0*number2
        elif sign == '-':
            number = number0-number2
        return number
    return None

def showEq():
    num = str(equals())
    ui.lineEdit.setText(num)

def plus():
    if equals() != None:
        ui.lineEdit.setText(str(equals()))
    ui.lineEdit.setText(ui.lineEdit.text() + ' + ')

def multiply():
    if equals() != None:
        ui.lineEdit.setText(str(equals()))
    ui.lineEdit.setText(ui.lineEdit.text() + ' * ')

def division():
    if equals() != None:
        ui.lineEdit.setText(str(equals()))
    ui.lineEdit.setText(ui.lineEdit.text() + ' / ')

def minus():
    if equals() != None:
        ui.lineEdit.setText(str(equals()))
    ui.lineEdit.setText(ui.lineEdit.text() + ' - ')

def zero():
    signs = ['-', '+', '/', '*']
    if ui.lineEdit.text().split() != []:
        if ui.lineEdit.text().split()[-1] not in signs: 
            ui.lineEdit.setText(ui.lineEdit.text() + '0')

def percents():
    nums = ui.lineEdit.text().split()
    if checkLen():
        num = float(nums[2])
        num *= float(nums[0])
        num /= 100
        ans = nums[0] + ' ' + nums[1] + ' ' + str(num)
        ui.lineEdit.setText(ans)

def CE():
    nums = ui.lineEdit.text().split()
    if 0 < len(nums) < 3:
        ui.lineEdit.clear()
    elif len(nums) == 3:
        ui.lineEdit.setText(nums[0])

def C():
    ui.lineEdit.clear()

def erase():
    line = ui.lineEdit.text()
    nums = line.split()
    if len(nums) > 1:
        sign = nums[1]
    else:
        sign = None
    if len(line) >= 1:
        line = line.replace(' ', '')
        line = line[:-1]
        if sign != None:
            if line.find(sign) > -1:
                nums = line.split(sign)
                line = ''
                nums = [nums[0], sign, nums[1]]
                for i in range(len(nums)):
                    line += nums[i]
                    line += ' '
    ui.lineEdit.setText(line)

def showSqrt():
    nums = ui.lineEdit.text().split()
    if 0 < len(nums) < 3:
        num = float(nums[0])
        num **= 1/2
        num = round(num, 3)
        ui.lineEdit.setText(str(num))
    if len(nums) == 3:
        num = float(nums[2])
        num **= 1/2
        num = round(num, 3)
        line = nums[0] + ' ' + nums[1] + ' ' + str(num)
        ui.lineEdit.setText(line)

def square():
    nums = ui.lineEdit.text().split()
    if 0 < len(nums) < 3:
        num = float(nums[0])
        num **= 2
        num = round(num, 3)
        ui.lineEdit.setText(str(num))
    if len(nums) == 3:
        num = float(nums[2])
        num **= 2
        num = round(num, 3)
        line = nums[0] + ' ' + nums[1] + ' ' + str(num)
        ui.lineEdit.setText(line)

def oneToX():
    nums = ui.lineEdit.text().split()
    if 0 < len(nums) < 3:
        num = float(nums[0])
        num = 1/num
        num = round(num, 3)
        ui.lineEdit.setText(str(num))
    if len(nums) == 3:
        num = float(nums[2])
        num = 1/num
        num = round(num, 3)
        line = nums[0] + ' ' + nums[1] + ' ' + str(num)
        ui.lineEdit.setText(line)

def chSgn():
    nums = ui.lineEdit.text().split()
    if 0 < len(nums) < 3:
        num = float(nums[0])
        num *= -1
        num = round(num, 3)
        ui.lineEdit.setText(str(num))
    if len(nums) == 3:
        num = float(nums[2])
        num *= -1
        num = round(num, 3)
        line = nums[0] + ' ' + nums[1] + ' ' + str(num)
        ui.lineEdit.setText(line)

def dot():
    ui.lineEdit.setText(ui.lineEdit.text() + '.')

def one():
    ui.lineEdit.setText(ui.lineEdit.text() + '1')

def two():
    ui.lineEdit.setText(ui.lineEdit.text() + '2')

def three():
    ui.lineEdit.setText(ui.lineEdit.text() + '3')

def four():
    ui.lineEdit.setText(ui.lineEdit.text() + '4')

def five():
    ui.lineEdit.setText(ui.lineEdit.text() + '5')

def six():
    ui.lineEdit.setText(ui.lineEdit.text() + '6')

def seven():
    ui.lineEdit.setText(ui.lineEdit.text() + '7')

def eight():
    ui.lineEdit.setText(ui.lineEdit.text() + '8')

def nine():
    ui.lineEdit.setText(ui.lineEdit.text() + '9')

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.pushButton_9.clicked.connect(division)
ui.pushButton_20.clicked.connect(dot)
ui.pushButton_24.clicked.connect(showEq)
ui.pushButton_2.clicked.connect(percents)
ui.pushButton_19.clicked.connect(three)
ui.pushButton_8.clicked.connect(showSqrt)
ui.pushButton.clicked.connect(seven)
ui.pushButton_15.clicked.connect(two)
ui.pushButton_4.clicked.connect(square)
ui.pushButton_14.clicked.connect(zero)
ui.pushButton_3.clicked.connect(oneToX)
ui.pushButton_17.clicked.connect(nine)
ui.pushButton_22.clicked.connect(minus)
ui.pushButton_5.clicked.connect(four)
ui.pushButton_10.clicked.connect(CE)
ui.pushButton_21.clicked.connect(multiply)
ui.pushButton_7.clicked.connect(chSgn)
ui.pushButton_13.clicked.connect(eight)
ui.pushButton_23.clicked.connect(plus)
ui.pushButton_18.clicked.connect(six)
ui.pushButton_6.clicked.connect(one)
ui.pushButton_12.clicked.connect(erase)
ui.pushButton_11.clicked.connect(C)
ui.pushButton_16.clicked.connect(five)

window.show()
sys.exit(app.exec())