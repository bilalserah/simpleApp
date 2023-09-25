# -*- coding: utf-8 -*-
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
import bidi.algorithm
from kivy.core.window import Window
import arabic_reshaper




Window.size = (350,600)
class SecondScreen03(MDScreen):
    pass
class SecondScreen01(MDScreen):
    pass
class SecondScreen02(MDScreen):
    pass
class FirstScreen(MDScreen):
    pass
class ThreeScreen(MDScreen):
    pass
class ForScreen(MDScreen) :
    pass


class MyApp(MDApp):
    def build(self):

        self.Screen_ = ScreenManager(transition = FadeTransition())
        self.Screen_.add_widget(Builder.load_file("Three_Screen.kv"))
        self.Screen_.add_widget(Builder.load_file("For_Screen.kv"))
        self.Screen_.add_widget(Builder.load_file("Second_Screen03.kv"))
        self.Screen_.add_widget(Builder.load_file("Second_Screen02.kv"))
        self.Screen_.add_widget(Builder.load_file("Second_Screen01.kv"))
        self.Screen_.add_widget(Builder.load_file("First_Screen.kv" ))
        return self.Screen_

    def convert_Arab(self ,text_):
        text_1 = arabic_reshaper.reshape(text_)
        text = bidi.algorithm.get_display(text_1,base_dir= "R")
        return text

    def say_hello(self):
        print("Hello, KivyMD!")

if __name__ == '__main__':

    LabelBase.register(name='font_01', fn_regular="font\\arial01.ttf")
    LabelBase.register(name='Roboto', fn_regular="font\poppins\\Poppins-Bold.ttf"  )
    LabelBase.register(name='font_02', fn_regular="font\\arial.ttf")
    LabelBase.register(name='poppins', fn_regular="font\\poppins\\Poppins-SemiBold.ttf")
    MyApp().run()
