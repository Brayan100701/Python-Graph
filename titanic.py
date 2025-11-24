#ejercicio de uso de librerias como numpy y pandas
#con la informacion de accidente de titanic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

print("Ejercico para saber si sobrebirias al accidente de Titanic")

def datos_tripulacion():
    n_h_t = 867 # numero de hombres de la tripulacion
    n_m_t = 23 # numero de mujeres en la tripulacion
    n_n_t = 1 # numero de niños en la tripulacion
    print (f"datos de la tripulacion:")
    a = {"Tripulacion": pd.Series([n_h_t,n_m_t,n_n_t], index=["Hombres","mujeres","niños"])}
    df_dt = pd.DataFrame(a)
    ar_nom_t = np.array(["Hombres","mujeres","niños"])
    ar_num_t = np.array([n_h_t,n_m_t,n_n_t])
    print(df_dt)
    return df_dt , ar_num_t, ar_nom_t


def clase_primera():
    n_h_p = 175 # numero de hombres de la primera clase
    n_m_p = 144 # numero de mujeres de la primera clase
    n_n_p = 7 # numero de niños de la primera clase
    print (f"datos de la personas de la primera clase:")
    b = {"Primera clase ": pd.Series([n_h_p,n_m_p,n_n_p], index=["Hombres","mujeres","niños"])}
    df_pc = pd.DataFrame(b)
    print(df_pc)
    return df_pc

def clase_segunda():
    n_h_s = 168 # numero de hombres de la segunda clase
    n_m_s = 93 # numero de mujeres de la segunda clase
    n_n_s = 27 # numero de niños de la segunda clase
    print (f"datos de la personas de la segunda clase:")
    c = {"Primera clase ": pd.Series([n_h_s,n_m_s,n_n_s], index=["Hombres","mujeres","niños"])}
    df_sc = pd.DataFrame(c)
    print(df_sc)
    return df_sc

def clase_tercera ():
    n_h_t = 462 # numero de hombres de la tercera clase
    n_m_t = 165 # numero de mujeres de la tercera clase
    n_n_t = 89 # numero de niños de la tercera clase
    print (f"datos de la personas de la tercera clase:")
    d = {"Primera clase ": pd.Series([n_h_t,n_m_t,n_n_t], index=["Hombres","mujeres","niños"])}
    df_tc = pd.DataFrame(d)
    print(df_tc)
    return df_tc

def procentaje_priera_clase():
    porc_h_p = .32 # porcentaje de supervivencia de los hombres de la primera clase
    porc_m_p = .97 # porcentaje de supervivencia de las mujeres de la primera clase
    porc_n_p = 1 # porcentaje de supervivencia de los niños de la primera clase

def porcentaje_segunda ():
    porc_h_s = .08 # porcentaje de supervivencia de los hombres de la segunda clase
    porc_m_s = .74 # porcentaje de supervivencia de las mujeres de la segunda clase
    porc_n_s = .9 # porcentaje de supervivencia de los niños de la segunda clase

def porcentaje_tercera():
    porc_h_t = .13 # porcentaje de supervivencia de los hombres de la tercera clase
    porc_m_t = .49 # porcentaje de supervivencia de las mujeres de la tercera clase
    porc_n_t = .11 # porcentaje de supervivencia de los niños de la tercera clase 


def porcentaje_tripulacion():
    hombres = .2 # porcentaje de supervivencia de los hombres de la tripulacion
    mujeres = .89 # porcentaje de supervivencia de las mujeres de la tripulacion


PC,PA,PB = datos_tripulacion()
clase_primera()
clase_segunda()
clase_tercera()


plt.bar(PB,PA)
plt.show()