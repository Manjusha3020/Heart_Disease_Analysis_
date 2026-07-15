from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        return 'OK'
    return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)