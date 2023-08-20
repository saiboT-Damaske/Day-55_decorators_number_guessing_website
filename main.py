from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<strong>" + function() + "</strong>"
    return wrapper


def make_emph(function):
    def wrapper(*args, **kwargs):
        msg = function(*args, **kwargs)
        return "<em>{}</em>".format(msg)
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper



@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


@app.route("/hitsa/<now>")
def hit(now):
    return f"mama mia {now}"



@app.route("/bye")
@make_underlined
@make_emph
def bye():
    return "<b>byeo</b>"

if __name__ == "__main__":
    app.run(debug=True)