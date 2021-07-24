import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

def invalid_name():
        error_message = Popup(title = "Invalid Username",
        content=Label(
        text="Invalid Username\nPress ESC and Try Again!"),
        size=(10,10),
        size_hint=(0.5, 0.5))
        error_message.open()

class LandingPage(Screen):
    username = ObjectProperty(None)
    
    Window.clearcolor = (1, 0.8, 0.4, 1)

    def login(self):
        if len(self.ids.username.text) < 1:
            invalid_name()
        else:
            self.manager.current="home"
    
class homepage(Screen):
    pass

class qn1(Screen):
    pass

class qn2(Screen):
    pass

class qn3(Screen):
    pass

class qn4(Screen):
    pass

class qn5(Screen):
    pass

class lastpage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

    

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    MyApp().run()