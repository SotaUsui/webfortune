from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    output = subprocess.run(["fortune"], stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE)
    return '<pre>' + output.stdout.decode("utf8") + '</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
    output = subprocess.run(["cowsay", message], stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
    return '<pre>' + output.stdout.decode("utf8") + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    fortune = subprocess.run(["fortune"], stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
    fortune = fortune.stdout.decode("utf8")
    output = subprocess.run(["cowsay", fortune], stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
    return '<pre>' + output.stdout.decode("utf8") + '</pre>'
