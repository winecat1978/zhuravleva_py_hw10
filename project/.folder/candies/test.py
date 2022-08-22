# from kivy.app import App
# from kivy.uix.label import Label
 
# # class MainApp(App):
# #     def build(self):
# #         label = Label(text='Начнем игру!',
# #                       size_hint=(.5, .5),
# #                       pos_hint={'center_x': .5, 'center_y': .5})
 
# #         return label
 
# # if __name__ == '__main__':
# #     app = MainApp()
# #     app.run()

# # from kivy.app import App
# from kivy.uix.image import Image
 
# class MainApp(App):
#     def build(self):
#         img = Image(source='https://avatars.mds.yandex.net/i?id=33863f75d47c2dea7507e30d6295f179-4471740-images-thumbs&n=13',
#                     size_hint=(1, .5),
#                     pos_hint={'center_x':.5, 'center_y':.5})
 
#         return img
 
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

# import kivy
# import random

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout

# red = [1,0,0,1]
# green = [0,1,0,1]
# blue =  [0,0,1,1]
# purple = [1,0,1,1]

# class HBoxLayoutExample(App):
#     def build(self):
#         layout = BoxLayout(padding=10)
#         colors = [red, green, blue, purple]

#         for i in range(5):
#             btn = Button(text="Button #%s" % (i+1),
#                          background_color=random.choice(colors)
#                          )

#             layout.add_widget(btn)
#         return layout

# if __name__ == "__main__":
#     app = HBoxLayoutExample()
#     app.run()

# 

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput

# class MainApp(App):
#     def build(self):
#         self.operators = ["/", "*", "+", "-"]
#         self.last_was_operator = None
#         self.last_button = None
#         main_layout = BoxLayout(orientation="vertical")
#         self.solution = TextInput(
#             multiline=False, readonly=True, halign="right", font_size=55
#         )
#         main_layout.add_widget(self.solution)
#         buttons = [
#             ["7", "8", "9"],
#             ["4", "5", "6"],
#             ["1", "2", "3"],
#             ["0", "Ввод"],
#         ]
#         for row in buttons:
#             h_layout = BoxLayout()
#             for label in row:
#                 button = Button(
#                     text=label,
#                     pos_hint={"center_x": 0.5, "center_y": 0.5},
#                 )
#                 button.bind(on_press=self.on_button_press)
#                 h_layout.add_widget(button)
#             main_layout.add_widget(h_layout)

#         equals_button = Button(
#             text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
#         )
#         equals_button.bind(on_press=self.on_solution)
#         main_layout.add_widget(equals_button)

#         return main_layout

#     def on_button_press(self, instance):
#         current = self.solution.text
#         button_text = instance.text

#         if button_text == "C":
#             # Очистка виджета с решением
#             self.solution.text = ""
#         else:
#             if current and (
#                 self.last_was_operator and button_text in self.operators):
#                 # Не добавляйте два оператора подряд, рядом друг с другом
#                 return
#             elif current == "" and button_text in self.operators:
#                 # Первый символ не может быть оператором
#                 return
#             else:
#                 new_text = current + button_text
#                 self.solution.text = new_text
#         self.last_button = button_text
#         self.last_was_operator = self.last_button in self.operators

#     def on_solution(self, instance):
#         text = self.solution.text
#         if text:
#             solution = str(eval(self.solution.text))
#             self.solution.text = solution


# if __name__ == "__main__":
#     app = MainApp()
#     app.run()

# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Конвертер"


class MyApp(App):
	
	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		self.label = Label(text='Конвертер')
		self.miles = Label(text='Мили')
		self.metres = Label(text='Метры')
		self.santimetres = Label(text='Сантиметры')
		self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
		self.input_data.bind(text=self.on_text) # Добавляем обработчик события

	# Получаем данные и производит их конвертацию
	def on_text(self, *args):
		data = self.input_data.text
		if data.isnumeric():
			self.miles.text = 'Мили: ' + str(float(data) * 0.62)
			self.metres.text = 'Метры: ' + str(float(data) * 1000)
			self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
		else:
			self.input_data.text = ''

	# Основной метод для построения программы
	def build(self):
		# Все объекты будем помещать в один общий слой
		box = BoxLayout(orientation='vertical')
		box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.miles)
		box.add_widget(self.metres)
		box.add_widget(self.santimetres)

		return box


# Запуск проекта
if __name__ == "__main__":
	MyApp().run()