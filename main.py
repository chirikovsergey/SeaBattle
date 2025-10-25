from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from libs.ship import ship #временно

class MyApp(App):
    def build(self):
        # -------- временно ----------
        ship1 = ship(1)
        ship2 = ship(2) 
        print(f"Первый корабль - {ship1.damage}")
        ship1.damage = 50
        print(f"Первый корабль - {ship1.damage}")
        # ----------------------------
        return MainLayout()  # Главный виджет (описан в KV)

class MainLayout(GridLayout):
    def on_button_click(self):
        self.ids.label.text = "Кнопка нажата!"


if __name__ == "__main__":
    MyApp().run()