from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__, template_folder='template')

@app.route('/')
def ibm():
    return render_template('ibm.html')
app.run(debug=True)