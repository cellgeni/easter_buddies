import random

from flask import Flask, request, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='static')


class Person:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


persons = []
with open("data.txt") as f:
    for line in f:
        data = line.split("\t")
        p = Person(data[0], data[1], data[2])
        persons.append(p)

template = "main.html"


@app.route('/', methods=['GET', 'POST'])
def get_random_email():
    if request.method == "POST":
        return render_template(template, person=random.choice(persons))
    return render_template(template)


if __name__ == '__main__':
    app.run()
