import pandas as pd 


df = pd.read_excel("candidatos2023.xlsx")

lista_departamentos= df["Descripción del Departamento"].unique()
lista_departamentos=lista_departamentos.tolist()

df=df[(df["Descripción de la Corporación/Cargo"] == "ASAMBLEA")& (df["Descripción del Departamento"] == 'LA GUAJIRA')]

lista_nom1= df["Primer Nombre"][:6].tolist()        
lista_nom2= df["Segundo Nombre"][:6].tolist()
lista_ape1= df["Primer Apellido"][:6].tolist()
lista_ape2= df["Segundo Apellido"][:6].tolist()

lista_nomcompl= lista_nom1+ lista_nom2 +  lista_ape1 + lista_ape2

print(lista_nomcompl)



