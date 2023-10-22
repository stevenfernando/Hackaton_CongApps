from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivymd.uix.menu import MDDropdownMenu

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
KV="""
<MenuScreen>:
    Button:
        id: button
        size_hint: .2, .1
        text: "Elige tu departamento"
        pos_hint: {"center_x": .5, "center_y": .15}
        on_release: app.menu.open()
        
    AsyncImage:
        source: 'logo.png'
        size_hint: 1, .5
        pos_hint: {'center_x':.5, 'center_y': .5}

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
"""

# Declare both screens
class MenuScreen(Screen):
    def menu_open(self1):
        
        menu_items = [
            {
                "text": f" {i}",
                "viewclass": "OneLineListItem",                                       
                "on_release": lambda x=f"Item {i}": self1.menu_callback(x),
                
                
            } for i in range(5)
        ]
        
        MDDropdownMenu(
            caller=self1.root.ids.button,
            items=menu_items,
            width_mult=4         
        ).open()

    def menu_callback(self1, text_item):
        print(text_item)

    def build(self):
        
        return Builder.load_string(KV)
    pass

class SettingsScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()