from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        return MainLayout()  # Главный виджет (описан в KV)

class MainLayout(GridLayout):
    def on_button_click(self):
        self.ids.label.text = "Кнопка нажата!"


if __name__ == "__main__":
    MyApp().run()