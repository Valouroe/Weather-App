# Weather App
 A Weather App created using Python, HTML, CSS, JavaScript
# HOW TO RUN CODE
    Create a Python file with the name "app.py" to help Flask recognize the file by default
    Create two folders- static and weather
    Create a HTML file with the name "index.html" and put it in the weather folder
    NOTE: On line 15 in the Python code you'll have to update the path(right click the index.html file after it's in the folder and copy path) because it's on a new system.
    Create the CSS file and name it "s.css"
    Create the JavaScript file and name it "script.js"
    In the static folder, put in the CSS and JavaScript file.
    Input the five images(clear, clouds, drizzle, mist, rain) into the static folder
# Python
    I used python and flask in python to access the weather API, prompt the user to enter a city name, and run the code. 
# Python/Flask code
    import json
    from flask import Flask, render_template
    app=Flask(__name__)
    from pip._vendor import requests
    name=input("Enter city name ")
    key="d47e82aaa9517ebd0d4c7ce93be3c989"
    @app.route("/")
    def index():
        response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={name}&appid={key}")
        user=response.json()
        temp=round(user["main"]["temp"])
        desc=user["weather"][0]["main"]
        description=user["weather"][0]["description"]
        page=""
        f=open(r"C:\Users\vokey\.vscode\.vscode\weather\index.html","r")
        page=f.read()
        f.close()
        page=page.replace("{temp}",str(temp)+"°C")
        page=page.replace("{name}",name)
        page=page.replace("{desc}",desc)
        page=page.replace("{description}",description)
        return page
    app.run(host='0.0.0.0')
# HTML/CSS
    I used the HTML to accept the temperature and name of the city from Python. And output that data on a good background with pictures.
# HTML Code
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="/static/s.css" type="text/css">
    </head>
    <body>
        <div class="card">
            <div class="weather">
                <p id="des">{desc}</p>
                <h1>{description}</h1>
                <img src="" id="weather-icon">
                <h1 class="temp">{temp}</h1>
                <h2 class="city">{name}</h2>
            </div>
        </div>
            
    </body>
    <script src="/static/script.js"></script>
    </html>
# CSS Code
    .card{
    width:90%;
    max-width:470px;
    background-color: cyan;
    margin:100px auto 0;
    border-radius:20px;
    padding:40px 35px;
    text-align:center;
    }
    .card p{
        display:none;
    }
# JavaScript
    I used JavaScript to accept the description of the weather from Python/HTML. Then use that information to determine what image to show. 
# JavaScript Code
    const w=document.getElementById("weather-icon");
    var d=document.getElementById("des").innerHTML
    console.log(d);
    if(d=="Clouds"){
        w.src="/static/clouds.png";
    }
    else if(d=="Clear"){
        w.src="/static/clear.png";
    }
    else if(d=="Rain"){
        w.src="/static/rain.png";
    }
    else if(d=="Drizzle"){
        w.src="/static/drizzle.png";
    }
    else if(d=="Mist"){
        w.src="/static/mist.png";
    }
