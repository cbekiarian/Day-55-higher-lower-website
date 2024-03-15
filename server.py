from flask import Flask
import random

number = random.randint(1, 9)
app = Flask(__name__)
print (number)

def check_number(function):
    def wrapper():
        function()
    return wrapper
@app.route("/")
def startup():

    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGxlYmdzNzl3OTFpajFkNnpsZTgwcWN1OGw5dTQweDhkdDkxd2h3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3h4EfNUQR02HBk6hpU/giphy.gif' alt='vi lost'>")

@app.route("/<int:user_num>")
def show_number(user_num):
    if user_num == number:
        return ("<h1>Guess a number between 0 and 9</h1>"
                "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDVyaHp3dzBidjRzY3JndW4yMnRjNXFhamJwbmpndjRwdjkyeGcyZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/o75ajIFH0QnQC3nCeD/giphy.gif' alt='vi lost'>")

    if user_num <= number:
         return ("<h1>Guess a number between 0 and 9</h1>"
                 "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGt3M3pmamlmcno1bDAwNWZreHJwbmVyanpvNjZza2dsdHYwdHBuNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WUTxupKrZJMjver3UF/giphy.gif' alt='vi lost'>")

    if user_num >= number:
        return ("<h1>Guess a number between 0 and 9</h1>"
                "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExanRyZjlpOHh0cGtic3lucWthMm01b2dkaGVya2F5YjN4YW9zeHRtaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YKroe55zFMIwpmBCu6/giphy.gif' alt='vi lost'>")





if __name__ == "__main__":
    app.run(debug=True)