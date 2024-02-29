from flask import render_template,request,redirect,session
from flask_app import app
from flask_app.models.cookie import Cookie

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookie():
    return render_template('cookie.html',cookies = Cookie.get_all())

@app.route('/cookies/new')
def new_cookie():
    return render_template("new_cookie.html")

@app.route('/cookies/create', methods=['POST'])
def create():
    if not Cookie.validate_cookie(request.form):
        return redirect('/cookies/new')
    data={
        'name': request.form['name'],
        'type': request.form['type'],
        'number_of_boxes': request.form['number_of_boxes']
    }
    Cookie.save(data)
    return redirect('/cookies')

@app.route('/cookie/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template('edit_cookie.html', cookie = Cookie.get_one_cookie(data))

@app.route('/cookie/update/<int:id>', methods= ['POST'])
def update(id):
    if not Cookie.validate_cookie(request.form):
        return redirect(f'/cookie/edit/{id}')
    data={
        "id": id,
        'name': request.form['name'],
        'type': request.form['type'],
        'number_of_boxes': request.form['number_of_boxes']
    }
    Cookie.update(data)
    return redirect('/cookies')