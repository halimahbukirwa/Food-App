from flask import Blueprint,render_template,request,jsonify,redirect,url_for

views = Blueprint(__name__,'views')

@views.route('/')
def home():
    return render_template('index.html', name='Halimah')

@views.route('/profile/<username>')
def profile(username):
    return render_template('index.html',name=username)

#accessing query parameters
@views.route('/status')
def status():
    args = request.args
    name = args.get('name')
    return render_template('index.html',name=name)

#returning json
@views.route('/json')
def get_json():
    return jsonify({'name':'Halimah','age':22})

#Getting data from an incoming 
@views.route('/data')
def data():
    data = request.json
    return jsonify(data)

#Redirecting
@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.get_json'))

@views.route('/profiles')
def profiles():
    return render_template('profile.html')




