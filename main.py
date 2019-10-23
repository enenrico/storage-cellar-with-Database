from kivy.app import App        #Import lib
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):   #create a screen for the main menue
    pass
class AddScreen(Screen):    #create a screen for a new screen
    pass
class AddFood(Screen):      #create a screen to add food
    pass
class DeleteFood(Screen):   #create a Screen to delete foof
    pass
class Admin(Screen):        ##create a Screen for the admin
     pass


class WindowManager(ScreenManager):
    pass


kv =  Builder.load_file("screen_main.kv")

class MyApp(App):

    def build(self):

        return kv

if __name__ == '__main__':  #build 
    MyApp().run()
