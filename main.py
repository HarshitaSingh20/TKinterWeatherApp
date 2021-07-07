from tkinter import *
from tkinter import Image,BitmapImage
from configparser import ConfigParser
import requests
from tkinter import messagebox
from PIL import ImageTk,Image


url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=eb3fbe054e819fc8c15333d05b665792'
app=Tk()
app.title("Weather App")
app.geometry('300x200')

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['apikey']['key']

def get_weather(city):
    result= requests.get(url.format(city,api_key))
    if result:
        json=result.json()

        city= json['name']
        country= json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius= temp_kelvin-273.15
        temp_fehrenheit= temp_celcius*(9/5) + 32
        icon= json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        description=json['weather'][0]['description']
        final=(city,country,temp_celcius,temp_fehrenheit,icon,weather,description)
        return final
    else:
        return None
print(get_weather('London'))
def search():
    city=city_text.get()

    weather=get_weather(city)

    if weather:
        location_lbl['text']='City:{} , Country:{}'.format(weather[0],weather[1])
        #image['bitmap']='weather_icons/{}.png'.format(weather[4])
        temp_lbl['text']='{:.2f} ͦC, {:.2f} ͦF'.format(weather[2],weather[3])
        weather_lbl['text']='Weather:{} , Description: {}'.format(weather[5],weather[6])


    else:
        messagebox.showerror('Error','Invalid city name{} '.format(city))

city_text=StringVar()
city_entry=Entry(app,textvariable=city_text)
city_entry.pack()

search_btn=Button(app,text="Search Weather",width=12,command=search)
search_btn.pack()

image=Label(app, bitmap='')
image.pack()
#adding a label to fetch locaion

location_lbl=Label(app,text=' ')
location_lbl.pack()

temp_lbl= Label(app,text='')
temp_lbl.pack()

weather_lbl= Label(app,text='')
weather_lbl.pack()

app.mainloop()
