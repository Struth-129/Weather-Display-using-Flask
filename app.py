from flask import Flask , render_template,request
import requests

app=Flask(__name__)
app.config['DEBUG']=True


@app.route("/",methods=['POST','GET'])
def index():
    if request.method == "POST":
        text = request.form['text']
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=02f6382ca02ba4fad032b03efdfa7435'
    city=text
    r=requests.get(url.format(city)).json()
    try:
        weather={
            'city': city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
    except:
        weather={
            'city':'Not-Found',
            'temperature':'Nil',
            'description':'Enter a valid city',
            'icon':'0'
        }
    return render_template("index.html",weather=weather)
   

if __name__=="__main__":
    app.run()
