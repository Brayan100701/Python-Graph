#ejercicio de uso de librerias como numpy y pandas
#con la informacion de accidente de titanic

import numpy as np
import pandas as pd
import matplotlib as plt


print("Ejercico para saber si sobrebirias al accedente de Titanic")

def datos_generales():
    n_h_t = 867 # numero de hombres de la tripulacion
    n_m_t = 23 # numero de mujeres en la tripulacion
    n_n_t = 1 # numero de niños en la tripulacion

def clase_primera():
    n_h_p = 175 # numero de hombres de la primera clase
    n_m_p = 144 # numero de mujeres de la primera clase
    n_n_p = 7 # numero de niños de la primera clase

def clase_segunda():
    n_h_s = 168 # numero de hombres de la segunda clase
    n_m_s = 93 # numero de mujeres de la segunda clase
    n_n_s = 27 # numero de niños de la segunda clase

def clase_tercera ():
    n_h_t = 462 # numero de hombres de la tercera clase
    n_m_t = 165 # numero de mujeres de la tercera clase
    n_n_t = 89 # numero de niños de la tercera clase

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
    porc_n_t = porc_h_t>porc_h_t<porc_n_s # porcentaje de supervivencia de los niños de la tercera clase 


def porcentaje_tripulacion():
    hombres = .2 # porcentaje de supervivencia de los hombres de la tripulacion
    mujeres = .89 # porcentaje de supervivencia de las mujeres de la tripulacion