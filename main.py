from  kivy.app import  App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.button import Button,ButtonBehavior
class StopwatchScreen(Screen):
    pass

class ClockScreen(Screen):
    pass

class mainApp(App):
    pass

if __name__ == '__main__':
    Window.clearcolor=get_color_from_hex('#101216')
    LableBase.register(name='Roboto',fn_regular='Roboto-Thin.tff',)
mainApp().run()
