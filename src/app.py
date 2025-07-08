from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# in-memory store for characters
characters = []

# default Story Mode ability scores
DEFAULT_ABILITIES = [15, 14, 13, 12, 10, 8]

@app.route('/')
def index():
    return render_template('index.html', characters=characters)

@app.route('/create', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        name = request.form.get('name')
        char_class = request.form.get('class')
        race = request.form.get('race')
        abilities = request.form.getlist('ability')
        if not abilities:
            abilities = DEFAULT_ABILITIES
        else:
            abilities = [int(a) for a in abilities]
        character = {
            'name': name,
            'class': char_class,
            'race': race,
            'abilities': abilities,
        }
        characters.append(character)
        return redirect(url_for('index'))
    return render_template('create_character.html', default_abilities=DEFAULT_ABILITIES)

if __name__ == '__main__':
    app.run(debug=True)
