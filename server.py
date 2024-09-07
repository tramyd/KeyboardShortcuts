from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect
from flask import url_for
from data import learning_data, quiz_data
from flask import session

app = Flask(__name__)
app.secret_key = '12345'

correct_count = 0

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/macos')
def macos():
    for item in learning_data.values():
        item['curr_os'] = 'macos'
    return render_template('home_macos.html')

@app.route('/windows')
def windows():
    for item in learning_data.values():
        item['curr_os'] = 'windows'
    return render_template('home_windows.html')

@app.route('/module1')
def module1():
    return render_template('module1.html', learning_data=learning_data)

@app.route('/module1/1')
def edit_text():
    return render_template('module1_1.html', learning_data=learning_data)


@app.route('/module2')
def module2():
    return render_template('module2.html', learning_data=learning_data)

@app.route('/module2/1')
def browser():
    return render_template('module2_1.html', learning_data=learning_data)

@app.route('/module3')
def module3():
    return render_template('module3.html', learning_data=learning_data)

@app.route('/module3/1')
def desktop_1():
    return render_template('module3_1.html', learning_data=learning_data)

@app.route('/desktop_2')
def desktop_2():
    return render_template('desktop_2.html', learning_data=learning_data)


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term'].lower()  
    results = {key: val for key, val in learning_data.items() if search_term in val['function'].lower()}
    return render_template('results.html', results=results, learning_data=learning_data)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', learning_data=learning_data)

@app.route('/quiz/1', methods=['GET', 'POST'])
def quiz_1():
    global correct_count 
    message = ''
    # correct_count = session.get('correct_count', 0)
    if request.method == 'POST':
        user_input = request.form['user_input']
        correct_answer = '<u>User</u> <strong>Interface</strong> <em>Design</em>'
        # if user_input == correct_answer:
        if True:
            # session['correct_count'] = correct_count + 1
            # correct_count += 1
            # message = f"Correct! Total correct answers: {session['correct_count']}"
            message = "Nice job on the warm up! Now please proceed to the quiz."
        # else:
        #     message = "Incorrect formatting. Please try again."

    return render_template('quiz_1.html', message=message, correct_count=correct_count, learning_data=learning_data)


@app.route('/quiz/2', methods=['GET', 'POST'])
def quiz_2():
    global correct_count 
    if request.method == 'POST':
        answers = {
            'urlExtension': 'enter',
            'pageClose': 'w',
            'browserAction': 'open'
        }
                
        user_answers = {
            'urlExtension': request.form.get('urlExtension'),
            'pageClose': request.form.get('pageClose'),
            'browserAction': request.form.get('browserAction')
        }

        correct_answers = {}
        # correct_count = session.get('correct_count', 0)

        for key, value in user_answers.items():
            if value == answers[key]:
                correct_answers[key] = True
                correct_count += 1
            else:
                correct_answers[key] = False

        # session['correct_count'] = correct_count
        message = f"Total correct answers: {correct_count}"

        return jsonify({
            'message': message,
            'correctAnswers': correct_answers,
            'correctCount': correct_count,
            **user_answers  
        })

    return render_template('quiz_2.html', learning_data=learning_data)


@app.route('/quiz/3', methods=['GET', 'POST'])
def quiz_3():
    global correct_count
    if request.method == 'POST':
        answers = {
            'q1': 'true',
            'q2': 'true',
            'q3': 'false'
        }
        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3')
        }

        correct_answers = {}
        for key, value in user_answers.items():
            correct_answers[key] = value == answers[key]
            if correct_answers[key]:
                correct_count += 1

        message = f"Total correct answers: {correct_count}"
        return jsonify({
            'message': message,
            'correctAnswers': correct_answers,
            'correctCount': correct_count,
            'answers': answers,
            **user_answers
        })

    return render_template('quiz_3.html', learning_data=learning_data)


@app.route('/quiz/4')
def quiz_4():
    return render_template('quiz_4.html', learning_data=learning_data)

@app.route('/quiz/5')
def keyboard_quiz():
    return render_template('quiz_5.html', learning_data=learning_data)


@app.route('/quiz/6')
def quiz_6():
    global correct_count
    score = correct_count 
    total_questions = 10

    # Create a summary of questions and their correct answers
    summary = [
        {
            'text': 'Replicate this in the text box below (use copy, paste, bold, italicize, and underline shortcuts): <u>User</u> <strong>Interface</strong> <em>Design</em>',
            'correct_answer': '<u>User</u> <strong>Interface</strong> <em>Design</em>'
        },
        {
            'text': 'Which of the following will add ".com" to the end of an URL?',
            'correct_answer': 'Ctrl + Enter'
        },
        {
            'text': 'Which of the following will close the current page?',
            'correct_answer': 'Ctrl + W'
        },
        {
            'text': 'Ctrl + T does which of the following in the browser?',
            'correct_answer': 'Open new tab'
        },
        {
            'text': 'You can refresh a webpage in most browsers using the shortcut Ctrl + R.',
            'correct_answer': 'True'
        },
        {
            'text': 'The keyboard shortcut Ctrl + Shift + N opens a new incognito window in Google Chrome.',
            'correct_answer': 'True'
        },
        {
            'text': 'Shift+B will make your text bold.',
            'correct_answer': 'False'
        },
        {
            'text': 'Match the actions with its shortcut: new tab, minimize all apps, show or hide desktop',
            'correct_answer': 'new tab: ctrl t, minimize all apps: windows m, show or hide desktop: windows d'
        },
        {
            'text': 'Select the keys for the "bookmark current page" shortcut',
            'correct_answer': 'Ctrl + D'
        }
    ]

    return render_template('quiz_6.html', score=score, total_questions=total_questions, learning_data=learning_data, summary=summary)


@app.route('/404')
def error404():
    return render_template('404.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/404")


@app.route('/reset_quiz')
def reset_quiz():
    global correct_count
    correct_count = 0  # Reset the correct count
    return redirect(url_for('quiz_1'))  # Redirect back to the first quiz


@app.route('/increment_correct_count', methods=['POST'])
def increment_correct_count():
    global correct_count
    correct_count += 1
    return jsonify({'correctCount': correct_count})


@app.route('/get_correct_count', methods=['GET'])
def get_correct_count():
    global correct_count
    return jsonify({'correctCount': correct_count})



if __name__ == '__main__':
   app.run(debug = True)