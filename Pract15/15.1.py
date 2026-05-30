import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = '5a0bed3d82946f34d6de4ec442852116'

def get_weather():
    city = cityField.get().strip()

    if not city:
        messagebox.showwarning('Предупреждение', 'Введите название города')
        return

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': API_KEY, 'q': city, 'units': 'metric', 'lang': 'ru'}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        weather = response.json()

        city_name = weather['name']
        temperature = weather['main']['temp']
        description = weather['weather'][0]['description']
        humidity = weather['main']['humidity']
        weather_info = f'{city_name}:\n{temperature}°C, {description}\nВлажность: {humidity}%'
        info['text'] = weather_info

    except requests.exceptions.RequestException as e:
        messagebox.showerror('Ошибка', f'Не удалось получить данные о погоде:\n{e}')
    except KeyError:
        messagebox.showerror('Ошибка', 'Не удалось обработать ответ сервера')

root = tk.Tk()
root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('300x250')
root.resizable(width=False, height=False)

frame_top = tk.Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_bottom = tk.Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.3)
cityField = tk.Entry(frame_top, bg='white', font=('Arial', 14))
cityField.pack(fill=tk.BOTH, expand=True)
btn = tk.Button(frame_top, text='Посмотреть погоду', command=get_weather, font=('Arial', 12))
btn.pack(pady=5)
info = tk.Label(frame_bottom, text='Погода в городе', bg='#ffb700', font=('Arial', 12), justify=tk.LEFT, wraplength=200)
info.pack(fill=tk.BOTH, expand=True)

root.mainloop()