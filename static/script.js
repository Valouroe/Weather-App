const w=document.getElementById("weather-icon");
var d=document.getElementById("des").innerHTML
console.log(d);
    if(d=="Clouds"){
        w.src="C:\Users\vokey\OneDrive\Documents\weather app\static\clouds.png";
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