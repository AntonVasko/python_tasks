import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def createDB():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        mail TEXT NOT NULL,
        number TEXT NOT NULL
    )
    """)
createDB()

class UserScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.changeScreen = Button(text="Войти в учётную запись администратора")
        self.changeScreen.on_press = self.change_screen
        self.registration =  Button(text="Регистрация на конференцию")
        self.registration.on_press = self.save_data
        self.username = TextInput(hint_text='Введите своё ФИО')
        self.mail = TextInput(hint_text='Введите свой адрес электронной почты')
        self.number = TextInput(hint_text='Введите свой номер телефона')
        self.layout = BoxLayout(orientation='horizontal')
        self.mainLayout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.changeScreen)
        self.layout.add_widget(self.registration)
        self.mainLayout.add_widget(self.username)
        self.mainLayout.add_widget(self.mail)
        self.mainLayout.add_widget(self.number)
        self.mainLayout.add_widget(self.layout)
        self.add_widget(self.mainLayout)

    def change_screen(self):
        self.manager.current = 'login'

    def save_data(self):
        nm = self.username.text
        ml = self.mail.text
        nb = self.number.text
        self.username.text = ""
        self.mail.text = ""
        self.number.text = ""
        if nm != "" and ml != "" and nb != "":
            cursor.execute("INSERT INTO users(name, mail, number) VALUES (?, ?, ?)", (nm, ml, nb))
            conn.commit()

class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.changeScreen = Button(text="Отмена")
        self.registration =  Button(text="Вход")
        self.registration.on_press = self.check_password
        self.changeScreen.on_press = self.back
        self.username = TextInput(hint_text='Введите имя')
        self.password = TextInput(hint_text='Введите пароль', password=1)
        self.layout = BoxLayout(orientation='horizontal')
        self.mainLayout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.changeScreen)
        self.layout.add_widget(self.registration)
        self.mainLayout.add_widget(self.username)
        self.mainLayout.add_widget(self.password)
        self.mainLayout.add_widget(self.layout)
        self.add_widget(self.mainLayout)

    def check_password(self):
        nm = self.username.text
        pw = self.password.text
        self.username.text = ""
        self.password.text = ""
        if nm == "" and pw == "":
            self.manager.current = 'admin'
            

    def back(self):
        self.manager.current = 'user'

class AdminScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout(orientation='vertical')
        self.logout = Button(text="Выйти")
        self.logout.on_press = self.change_sc
        self.add_widget(self.layout)

    def change_sc(self):
        self.manager.current = 'user'

    def on_enter(self):
        self.clear_widgets()
        self.layout.clear_widgets()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            self.layout.add_widget(Label(text=f"{user[0]}. Имя: {user[1]}, Почта: {user[2]}, Телефон: {user[3]}"))
        self.layout.add_widget(self.logout)
        self.add_widget(self.layout)

class RegApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserScreen(name='user'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(AdminScreen(name='admin'))
        return sm
    
if __name__ == "__main__":
    RegApp().run()