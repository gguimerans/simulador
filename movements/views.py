from flask import render_template, request, url_for, redirect
from movements import app

@app.route('/')
defindex():
    return"Inicio"