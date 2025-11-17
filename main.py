import flet as ft
import matplotlib as plt
import calc


def main(page: ft.Page):
    def graficar(e):
        print(dd_opt.value)
    
    page.title = 'Graficadora de funciones'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    lbl_min = ft.Text(value='X min: ', color='white')
    txt_min = ft.TextField(value="0", width=100)

    lbl_max = ft.Text(value='X max: ', color='white')
    txt_max = ft.TextField(value="100", width=100)

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


    page.add(
        ft.Column(
            wrap=True,
            spacing=20,
            controls=[
                lbl_min,
                txt_min,
                lbl_max,
                txt_max,
                dd_opt,
                btn_calc
            ]
        ),
        ft.Column(
        )
    )


if __name__ == '__main__':
    ft.app(main)