from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import pandas as pd
from kivy.uix.image import Image
from kivy.loader import Loader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

df = pd.read_excel("candidatos2023.xlsx")

lista_departamentos= df["Descripción del Departamento"].unique()
lista_departamentos=lista_departamentos.tolist()


Builder.load_string("""

<One>:
    name: "one"
    FloatLayout:
        
        Button:
            text: "Elige tu departamento (La Guajira-Botón habilitado)"
            size_hint: .2, .1
            pos_hint: {'center_x':.5, 'center_y': .15}
            on_release:
                app.root.current = "two"
                    
    AsyncImage:
        source: 'logo.png'
        size_hint: .5, .5
        pos_hint: {'center_x':.5, 'center_y': .5}
    
        
<Two>:
    name: "two"
    GridLayout:
        id:grid
        cols:3

<Three>:
    name:'three'
    GridLayout:
        id:grid3
        cols:3
                    
<Four>:
    name: "four"
    FloatLayout:
        id:lay4


<Five>:
    name: "five"
    FloatLayout:
        id:lay5
     
                    
                  
                       

""")



class One(Screen):
    
    

    pass

class Two(Screen):

   
    
    def on_pre_enter(self):
        for i in lista_departamentos: #assuming you need to create 5 buttons
            button = Button(text=i) #the text on the button
            button.bind(on_press = self.changer) #when the button is clicked
            self.ids.grid.add_widget(button) #added to the grid

    def changer(self,instance):
        
        id = instance.text
        
        df = pd.read_excel("candidatos2023.xlsx")
        df = df[(df["Descripción de la Corporación/Cargo"] == "ASAMBLEA")& (df["Descripción del Departamento"] == id)]
        df = df.fillna('')
        lista_nom1= df["Primer Nombre"].tolist()        
        lista_nom2= df["Segundo Nombre"].tolist()
        lista_ape1= df["Primer Apellido"].tolist()
        lista_ape2= df["Segundo Apellido"].tolist()

        all_names= []
        for i, j,k,l in zip(lista_nom1, lista_nom2,lista_ape1,lista_ape2):
            all_names.append(f'{i} {j} {k} {l}')
            

        for i in all_names: 
           
            button2 = Button(text=i) #the text on the button
            button2.bind(on_press = self.changer2) #when the button is clicked
            self.manager.get_screen('three').ids.grid3.add_widget(button2) #added to the grid

        

        self.manager.current = 'three'


    def changer2(self,instance):
             
        id2 = instance.text
        
        print(id2)

        df2 = pd.read_csv("informacion.txt", delimiter='\t')
        df2 = df2[df2["candidatos"] == id2]
        df2 = df2.fillna('')
        print(df2["candidatos"].tolist())
        label1=df2["candidatos"].tolist()[0]
        label1= "Nombre: "+str(label1)
        label2con= df2["Nombre de la Agrupación Política"].tolist()[0]
        print(label2con)
        label2= "Partido Político: "+str(label2con)
        label3= df2["Descripción de la Corporación/Cargo"].tolist()[0]
        label3= "Cargo a postular: " + str(label3)

        label1 = Label(text=label1,pos_hint= {'center_x':.5, 'center_y': .6})
        label2 = Label(text=label2,pos_hint= {'center_x':.5, 'center_y': .5})
        label3 = Label(text=label3,pos_hint= {'center_x':.5, 'center_y': .4})

        self.manager.get_screen('four').ids.lay4.add_widget(label1)
        self.manager.get_screen('four').ids.lay4.add_widget(label2)
        self.manager.get_screen('four').ids.lay4.add_widget(label3)

        buttona = Button(text="Cargos Anteriores(Botón inhabilitado)", size_hint= {.2, .1}, pos_hint= {'center_x':.2, 'center_y': .3}) #the text on the button
        
        self.manager.get_screen('four').ids.lay4.add_widget(buttona) #added to the grid


        buttonb = Button(text="Contratos(Botón inhabilitado)", size_hint= {.2, .1},pos_hint= {'center_x':.2, 'center_y': .1}) #the text on the button     
       
        self.manager.get_screen('four').ids.lay4.add_widget(buttonb) #added to the grid
        
        buttonc = Button(text="Perfil Mediático de su partido", size_hint= {.2, .1},pos_hint={'center_x':.8, 'center_y': .3}) #the text on the button
        
        if (label2con=="PARTIDO CENTRO DEMOCRATICO"):
            buttonc.bind(on_press = self.changer3)
        else:
            buttonc.bind(on_press = self.changer5)
        
        self.manager.get_screen('four').ids.lay4.add_widget(buttonc) #added to the grid
        
        buttond = Button(text="Relaciones del Partido", size_hint= {.2, .1},pos_hint={'center_x':.8, 'center_y': .1})#the text on the button
        if (label2con=="PARTIDO CENTRO DEMOCRATICO"):
            buttond.bind(on_press = self.changer4)
        else:
            buttond.bind(on_press = self.changer6)
        
        self.manager.get_screen('four').ids.lay4.add_widget(buttond) #added to the grid

            
        self.manager.current = 'four'


        
    
    def changer3(self,instance):

        
        image = Image(source='cen_dem_med.png')

        self.manager.get_screen('five').ids.lay5.add_widget(image) 
        
        self.manager.current = 'five'

    def changer4(self,instance):

        
        image = Image(source='cen_dem_rel.png')

        self.manager.get_screen('five').ids.lay5.add_widget(image) 
        
        self.manager.current = 'five'


    def changer5(self,instance):

        
        image = Image(source='mais_med.png')

        self.manager.get_screen('five').ids.lay5.add_widget(image) 
        
        self.manager.current = 'five'

    
    def changer6(self,instance):

        
        image = Image(source='mais_rel.png')

        self.manager.get_screen('five').ids.lay5.add_widget(image) 
        
        self.manager.current = 'five'
        
        


    
    pass


class Three(Screen):


    
    pass


class Four(Screen):
    
    
          
    

    

    pass

class Five(Screen):
    
    
           

    

    pass




sm = ScreenManager()
one=One(name='one')
two=Two(name='two')
three=Three(name='three')
four=Four(name='four')
five=Five(name='five')
sm.add_widget(one)
sm.add_widget(two)
sm.add_widget(three)
sm.add_widget(four)
sm.add_widget(five)

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()
