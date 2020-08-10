from tkinter import *
import requests
import json
import datetime

root = Tk()
root.title('Weather')
#root.iconbitmap('py/Weather.ico')

# http://api.openweathermap.org/data/2.5/weather?q=Srikakulam,IN&APPID={API_KEY}


def search():
    city_name = search_city.get()

    try:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city_name + ",IN&APPID={YOUR API_KEY}")
        api = json.loads(api_request.content)
        city = api['name']
        temp = str(round(api['main']['temp']/10, 2))
        category = api['weather'][0]['description']

        label = Label(root, text=city + " Temperature: " + temp + " " + category, font=('Century Gothic',15), anchor = CENTER)
        label.grid(row=1, columnspan=8)

    except Exception as e:
        api = "Error..."

    
search_city = Entry(root, width=50, font=('Century Gothic', 10), bd=2)
search_city.grid(row=0, column=3, padx=10, pady=10)

search_label = Label(root, text='Enter City: ', font=('Century Gothic', 20))
search_label.grid(row=0, column=0, columnspan=3)

search_btn = Button(root, text='Search', font=('Century Gothic', 10), command=search)
search_btn.grid(row=0, column=5, columnspan=3, padx=10, pady=10)

today_label = Label(root, text=datetime.datetime.today(), font=('Candra', 15))
today_label.grid(row=2, columnspan=5)


root.mainloop()

