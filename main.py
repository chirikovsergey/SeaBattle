from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

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
        self.layout = MainLayout()  # Главный виджет (описан в KV)
        return self.layout
    
    # Очистить слой body
    def clear_main_content(self):
        self.root.ids.bl_main_content.clear_widgets()  

    # Задать текст статус-бара
    # Входные параметры:
    #  text - новый текст
    def set_app_status(self, text):
        self.root.ids.bl_statusbar.ids.l_app_status_bar.text = f"{text}"         

class MainLayout(BoxLayout):
    pass


if __name__ == "__main__":
    MyApp().run()