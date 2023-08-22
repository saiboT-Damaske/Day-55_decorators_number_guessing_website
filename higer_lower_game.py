import flask
import random

app = flask.Flask(__name__)

number_to_guess = random.randint(0, 9)
print(number_to_guess)


@app.route("/")
def main_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='main_gif' />")



@app.route("/<int:guess>")
def check_guess(guess):
    if guess > number_to_guess:
        return ("<h1 style='color: purple'>That was too high. Try again</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' />")
    elif guess < number_to_guess:
        return ("<h1 style='color: red'>That was too low. Try again</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' />")
    elif guess == number_to_guess:
        return ("<h1 style='color: green'>That was correct!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' />")


if __name__ == "__main__":
    app.run(debug=True)
