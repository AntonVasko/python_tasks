from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QRadioButton, QListWidget


def change_text():
    text = main_linedit.text()
    main_linedit.setText('')
    if qButton1.isChecked():
        main_text.setText('Добавлено')
        listWidget.addItem(text)
    else:
        main_text.setText('Не добавлено')


main_app = QApplication([])
main_window = QWidget()
main_window.resize(800, 600)
main_text = QLabel('Текст')
main_button = QPushButton('Кнопка')
main_linedit = QLineEdit()
main_linedit.setPlaceholderText('Введите текст')
qButton1 = QRadioButton('Да')
qButton1.setChecked(False)
qButton2 = QRadioButton('Нет')
qButton2.setChecked(True)
listWidget = QListWidget()

main_Vlayout = QVBoxLayout()
hlayout = QHBoxLayout()

hlayout.addWidget(qButton1)
hlayout.addWidget(qButton2)
main_Vlayout.addWidget(listWidget)
main_Vlayout.addWidget(main_text)
main_Vlayout.addWidget(main_linedit)
main_Vlayout.addLayout(hlayout)
main_Vlayout.addWidget(main_button)


main_window.setWindowTitle('training')
main_window.setLayout(main_Vlayout)

main_button.clicked.connect(change_text)

main_window.show()
main_app.exec()