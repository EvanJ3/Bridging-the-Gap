from flask import Flask, render_template

app = Flask(__name__)

# app_data = {
#     "name":         "Peter's Starter Template for a Flask Web App",
#     "description":  "A basic Flask app using bootstrap for layout",
#     "author":       "Peter Simeth",
#     "html_title":   "Peter's Starter Template for a Flask Web App",
#     "project_name": "Starter Template",
#     "keywords":     "flask, webapp, template, basic"
# }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/vis1')
def visualization1():
    return render_template('visualization1.html')

@app.route('/vis2')
def visualization2():
    return render_template('visualization2.html')

@app.route('/vis3')
def visualization3():
    return render_template('visualization3.html')

@app.route('/modeling')
def modeling():
    return render_template('modeling.html')


if __name__ == '__main__':
    app.run(debug = True)