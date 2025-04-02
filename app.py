import json
from flask import Flask, render_template,request
app=Flask(__name__)
from pip._vendor import requests

key="d47e82aaa9517ebd0d4c7ce93be3c989"
@app.route("/")
def index():
    city=request.args.get("city", "New York")
    response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={key}")
    user=response.json()
    temp=round(user["main"]["temp"])
    desc=user["weather"][0]["main"]
    description=user["weather"][0]["description"]
    # page=""
    # f=open(r"C:\Users\vokey\OneDrive\Documents\weather app\static\index.html","r")
    # page=f.read()
    # f.close()
    # page=page.replace("{temp}",str(temp)+"°C")
    # page=page.replace("{name}",name)
    # page=page.replace("{desc}",desc)
    # page=page.replace("{description}",description)
    return render_template("index.html", temp=temp, city=city, desc=desc, description=description)
app.run(host='0.0.0.0')