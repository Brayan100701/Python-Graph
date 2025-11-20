import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

import utilidades

matplotlib.use('svg')

def main(page: ft.Page):
    def graficar(e):
        if utilidades.validate(txt_min.value, txt_max.value, txt_inter.value):
            x_values, y_values = utilidades.calc_func(txt_min.value, txt_max.value, txt_inter.value, dd_opt.value)
            plt_space.update_plot(x_values,y_values)
            update_graph()

    def set_default(*args):
        txt_min.value = 0
        txt_max.value = 100
        plt_space.default_plot()
        update_graph()
        page.update()

    def rw_template():
        return ft.Row(
            controls=[
                plt_space.space
            ]
        )
    
    def update_graph():
        page.controls.pop()
        page.add(
            rw_template()
        )
        page.update()

    
    page.window.width = 1280
    page.window.height = 720
    page.title = 'Graficadora de funciones'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    lbl_min = ft.Text(value='X min: ', color='white')
    txt_min = ft.TextField(value="0", width=100)

    lbl_max = ft.Text(value='X max: ', color='white')
    txt_max = ft.TextField(value="1000", width=100)

    lbl_inter = ft.Text(value='Intervalo: ', color='white')
    txt_inter = ft.TextField(value="1", width=100)

    btn_default = ft.ElevatedButton(text='Reiniciar', on_click=set_default)
    btn_calc = ft.ElevatedButton(text='Calcular', on_click=graficar)
    

    dd_opt = ft.Dropdown(
        alignment=ft.alignment.center,
        width=100,
        options=[
            ft.dropdown.Option('sin'),
            ft.dropdown.Option('cos'),
            ft.dropdown.Option('tan')
        ],
        value='sin'
    )

    plt_space = utilidades.Space()

    page.add(
        ft.Row(
            wrap=True,
            spacing=30,
            controls=[
                lbl_min,
                txt_min,
                lbl_max,
                txt_max,
                dd_opt,
                lbl_inter,
                txt_inter,
                btn_calc,
                btn_default
            ]
        ),
        rw_template()
    )

    page.update()


if __name__ == '__main__':
    ft.app(main)