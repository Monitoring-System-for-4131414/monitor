from flask import Flask,render_template,url_for
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/warning')
def warning():
    return render_template('warning.html')

@app.route('/prompting')
def prompting():
    return render_template('prompting.html')



if __name__ == '__main__':
    app.run()
