from functools import partial

import flet as ft


def main(page: ft.Page):

	page.title = "JCal"
	page.padding = 20
	page.vertical_alignment = "center"
	page.horizontal_alignment = "center"
	page.window_max_height = 600
	page.window_max_width = 400
	page.bgcolor = '#D2E0FB'

	calc_input = ft.TextField(text_align="right", width=300, autofocus=True)

	page.add(calc_input)

	def enterdata(e, number):
		if (number == 'C'):
			calc_input.value = ''
			page.add(calc_input)
		else:
			calc_input.value = calc_input.value + number
			page.add(calc_input)


	def calculate(e):

		output = eval(calc_input.value)
		calc_input.value = output
		page.add(calc_input)

	but7 = ft.ElevatedButton("7", on_click=partial(enterdata, number='7'))
	but8 = ft.ElevatedButton("8", on_click=partial(enterdata, number='8'))
	but9 = ft.ElevatedButton("9", on_click=partial(enterdata, number='9'))
	but_add = ft.ElevatedButton("+", on_click=partial(enterdata, number='+'), bgcolor="#D988B9", color="black")

	row1 = ft.Row(width=300, controls=[but7, but8, but9, but_add], alignment="center")
	page.add(row1)

	but4 = ft.ElevatedButton("4", on_click=partial(enterdata, number='4'))
	but5 = ft.ElevatedButton("5", on_click=partial(enterdata, number='5'))
	but6 = ft.ElevatedButton("6", on_click=partial(enterdata, number='6'))
	but_minus = ft.ElevatedButton("-", on_click=partial(enterdata, number='-'), bgcolor="#D988B9", color="black")

	row2 = ft.Row(width=300, controls=[but4, but5, but6, but_minus], alignment="center")
	page.add(row2)

	but1 = ft.ElevatedButton("1", on_click=partial(enterdata, number='1'))
	but2 = ft.ElevatedButton("2", on_click=partial(enterdata, number='2'))
	but3 = ft.ElevatedButton("3", on_click=partial(enterdata, number='3'))
	but_mul = ft.ElevatedButton("X", on_click=partial(enterdata, number='*'), bgcolor="#D988B9", color="black")

	row3 = ft.Row(width=300, controls=[but1, but2, but3, but_mul], alignment="center")
	page.add(row3)

	but_dot = ft.ElevatedButton(".", on_click=partial(enterdata, number='.'))
	but0 = ft.ElevatedButton("0", on_click=partial(enterdata, number='0'))
	but_clear = ft.ElevatedButton("AC", on_click=partial(enterdata, number='C'), bgcolor="#D988B9", color="black")
	but_clear = ft.ElevatedButton("AC", on_click=partial(enterdata, number='C'), bgcolor="#D988B9", color="black")
	but_divide = ft.ElevatedButton("/", on_click=partial(enterdata, number='/'), bgcolor="#D988B9", color="black")

	row4 = ft.Row(width=300, controls=[but_dot, but0, but_clear, but_divide], alignment="center")
	page.add(row4)

	but_equal = ft.ElevatedButton("=", width=300, on_click=calculate, bgcolor="cyan", color="black")
	page.add(but_equal)


ft.app(target=main,)