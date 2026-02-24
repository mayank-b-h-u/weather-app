from tkinter import *
import requests

root=Tk()
root.geometry("360x420")
root.title("Weather App")
root.resizable(False,False)
root.configure(bg="#eaf6ff")
root.iconbitmap("weather.ico")
api_key="YOUR_API_KEY_HERE"
base_url="https://api.openweathermap.org/data/2.5/weather"
Label(root,text=("Weather App"),font=("Segoe UI",20,"bold"),bg="#eaf6ff").pack(padx=5,pady=5)
Label(root,text="Enter The City Name ",font=("Arial",10)).pack(padx=5,pady=5)
def get_weather():
    city=city_name.get().strip()
    params={
        "q":city,
        "appid":api_key,
        "uint":'metric'
    }
    try:
        response=requests.get(base_url,params=params)
        data=response.json()
        if data['cod']!=200:
            result.config(text="City is not found",font=("Arial",15))
            return 
        temp=data["main"]["temp"]-273.15
        temp=round(temp,2)
        humidity=data["main"]["humidity"]
        weather=data['weather'][0]['description'].title()
        city=data["name"]
        output=(
    f"City: {city}\n"
    f"Temperature: {temp} °C\n"
    f"Weather: {weather}\n"
    f"Humidity: {humidity}%")
        result.config(text=output)
    except ValueError:
        result.config(text="Error fetching data")

city_name=Entry(root,
    font=("Segoe UI", 14),
    justify="center",
    bd=2,
    relief=GROOVE,
    insertbackground="#f321f3")
city_name.pack(padx=10)
Button(
    root,
    text="Check Weather",
    font=("Segoe UI", 12, "bold"),
    bg="#2196f3",
    fg="white",
    activebackground="#1976d2",
    cursor="hand2",
    command=get_weather).pack(pady=10, ipadx=15, ipady=5)
card=Frame(root,relief=SOLID)
card.pack(padx=20, pady=10, fill=X)
result=Label(card,justify=LEFT,font=(15))
result.pack(padx=15,pady=15)

root.mainloop()