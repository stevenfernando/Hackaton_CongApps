from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from functools import partial
from kivy.uix.floatlayout import FloatLayout



Builder.load_string('''
<PageOne>:
   
                    
            
        
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
''')




class PageOne(Screen):

    
    def buttons(self):

        test_floatie = FloatLayout()

        def select(drop_button, text, btn):
            drop_button.text = text

        
        self.manager.dropButton = Button(text="Departamentos " , size_hint=(0.5, 0.2),
                            pos_hint= {'center_x':.5, 'center_y': .2})

        
        return test_floatie

   
class PageTwo(Screen):
    def p_2(self):
        self.manager.current = 'PageOne'

    



manager = ScreenManager()
manager.add_widget(PageOne(name="PageOne"))
manager.add_widget(PageTwo(name="PageTwo"))

class MainApp(App):
    def build(self):
        return manager

if __name__ == '__main__':
    MainApp().run()