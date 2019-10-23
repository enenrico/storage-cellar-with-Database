from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

class MainScreen(Screen):
    pass
class AddScreen(Screen):
    pass
class AddFood(Screen):
    pass
class DeleteFood(Screen):
    pass
class Admin(Screen):
     pass


class WindowManager(ScreenManager):
    pass


kv =  Builder.load_file("screen_main.kv")

class MyApp(App):
#    abcd = StringProperty('test')
    def build(self):

        return kv

if __name__ == '__main__':
    MyApp().run()
