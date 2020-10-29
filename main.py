from flask import Flask # сперва подключим модуль
from flask import Flask, render_template # подключаем render_template, который включает функции для Jinja

app = Flask(__name__) # объявим экземпляр фласка

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products/')
def render_products():
	return 'Продукты'

@app.route('/videos/<video_id>/')
def render_videos_item(video_id):
    return "Здесь будет видео " + video_id

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!",404
@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим",500

app.run() # запустим сервер
