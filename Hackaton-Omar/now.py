from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

KV='''


<PageOne>:
    Button:
        id: button
        size_hint: .2, .1
        text: "Elige tu departamento"
        pos_hint: {"center_x": .5, "center_y": .15}
        on_press: root.p_1()


<PageTwo>:

    FloatLayout:
        Label:
            size_hint: 1, 0.5
            pos_hint: {"top":1}
            text: "Page 2"
        Button:
            size_hint: 1, 0.3
            pos_hint: {"top": 0.3}
            text: "Open Page 1"
            on_press: root.p_2()

'''


  
#####################################################################################


class PageOne(Screen):
    def p_1(self):
        self.manager.current = 'PageTwo'
   
    
#################################################################################################

class PageTwo(Screen):
    def p_2(self):
        self.manager.current = 'PageOne'



#############################################################################################




manager = ScreenManager()
manager.add_widget(PageOne(name="PageOne"))
manager.add_widget(PageTwo(name="PageTwo"))

class MainApp(App):
    def build(self):
        return manager


MainApp().run()