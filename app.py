import openai
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

openai.api_key = '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'
conversation_history = ""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/conversation', methods=['POST'])
def converse():
    global conversation_history
    user_input = request.form['user_input']
    conversation_history += f"User: {user_input}\nEQ:"

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversation_history,
        max_tokens=1000
    )
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split("User:", 1)[0].split("EQ:", 1)[0]

    conversation_history += response_str + "\n"

    return jsonify({'response': response_str.strip()})


if __name__ == '__main__':
    app.run(debug=True)
