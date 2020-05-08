from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member/')
def member():
    return render_template('member.html')

@app.route('/changemember/')
def changemember():
    return render_template('changemember.html')

if __name__ == '__main__':
    app.run()
