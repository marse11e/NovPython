from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Ваш API токен для OpenWeatherMap
API_TOKEN = "d5bb44d0fa8e39e2339c9019d833d826"

# Главная страница
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if weather_data:
            return render_template('weather.html', data=weather_data)
        else:
            return render_template('index.html', error="Не удалось получить данные о погоде.")
    return render_template('index.html')

# Функция для получения данных о погоде
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Almaty&appid=d5bb44d0fa8e39e2339c9019d833d826&units=metric"
    response = requests.get(url)
    if response.ok:
        return response.json()
    return None

if __name__ == '__main__':
    app.run(debug=True)
