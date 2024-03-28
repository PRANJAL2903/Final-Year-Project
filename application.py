from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
app = application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database URL
db = SQLAlchemy(app)

# Define your User model here using SQLAlchemy ORM
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Use app context to create all database tables
with app.app_context():
    db.create_all()

# Set a secret key for session management
app.secret_key = 'Pranjal2903'

@app.route('/')
def home_page():
    return render_template('index1.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Route for signing up
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Check if the email is already registered
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return 'Email already exists. Please choose a different email.'
    
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return 'Signed up successfully'

# Route for signing in
@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        # Store user ID in session upon successful login
        session['user_id'] = user.id
        return render_template('index.html', message='Logged in successfully')
    else:
        return 'Invalid credentials'
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return 'Login successful'
        else:
            return 'Invalid email or password'
    return render_template('login.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')

@app.route('/blog4')
def blog4():
    return render_template('blog4.html')

@app.route('/blog5')
def blog5():
    return render_template('blog5.html')

@app.route('/blog6')
def blog6():
    return render_template('blog6.html')

@app.route('/blog7')
def blog7():
    return render_template('blog7.html')

@app.route('/blog8')
def blog8():
    return render_template('blog8.html')

@app.route('/blog9')
def blog9():
    return render_template('blog9.html')

@app.route('/blog10')
def blog10():
    return render_template('blog10.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            carat=request.form.get('carat'),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0], 2)

        # Store the result in session for displaying on the result page
        session['final_result'] = results

        # Redirect to the result page
        return redirect(url_for('show_result'))

@app.route('/show_result')
def show_result():
    # Retrieve the result from the session
    final_result = session.get('final_result', None)

    if final_result is not None:
        return render_template('result_page.html', final_result=final_result)
    else:
        return "Result not available."
    
@app.route('/linked_page_1')
def linked_page_1():
    return render_template('rings_gct1.html')

# Route for linked_page_2.html
@app.route('/linked_page_2')
def linked_page_2():
    return render_template('ring_rgct1.html')

# Route for linked_page_3.html
@app.route('/linked_page_3')
def linked_page_3():
    return render_template('pendant_gct1.html')

# Route for linked_page_4.html
@app.route('/linked_page_4')
def linked_page_4():
    return render_template('pendant_rgct1.html')

# Route for linked_page_5.html
@app.route('/linked_page_5')
def linked_page_5():
    return render_template('nosepins_gct1.html')

# Route for linked_page_6.html
@app.route('/linked_page_6')
def linked_page_6():
    return render_template('necklace_gct1.html')

# Route for linked_page_7.html
@app.route('/linked_page_7')
def linked_page_7():
    return render_template('necklace_rgct1.html')

# Route for linked_page_8.html
@app.route('/linked_page_8')
def linked_page_8():
    return render_template('mangalsutras_gct1.html')

# Route for linked_page_9.html
@app.route('/linked_page_9')
def linked_page_9():
    return render_template('earring_gct1.html')

# Route for linked_page_10.html
@app.route('/linked_page_10')
def linked_page_10():
    return render_template('earring_rgct1.html')

# Route for linked_page_11.html
@app.route('/linked_page_11')
def linked_page_11():
    return render_template('bracelets_gct1.html')

# Route for linked_page_12.html
@app.route('/linked_page_12')
def linked_page_12():
    return render_template('bangles_gct1.html')



@app.route('/ring_rgct2.html')
def ring_rgct2():
    # You can return a rendered template or a simple message
    return render_template('ring_rgct2.html')

@app.route('/ring_gct2.html')
def ring_gct2():
    # You can return a rendered template or a simple message
    return render_template('ring_gct2.html')

@app.route('/pendant_gct2.html')
def pendant_gct2():
    # You can return a rendered template or a simple message
    return render_template('pendant_gct2.html')

@app.route('/pendant_rgct2.html')
def pendant_rgct2():
    # You can return a rendered template or a simple message
    return render_template('pendant_rgct2.html')

@app.route('/nosepins_gct2.html')
def nosepins_gct2():
    # You can return a rendered template or a simple message
    return render_template('nosepins_gct2.html')

@app.route('/necklace_gct2.html')
def necklace_gct2():
    # You can return a rendered template or a simple message
    return render_template('necklace_gct2.html')

@app.route('/necklace_rgct2.html')
def necklace_rgct2():
    # You can return a rendered template or a simple message
    return render_template('necklace_rgct2.html')

@app.route('/mangalsutras_gct2.html')
def mangalsutras_gct2():
    # You can return a rendered template or a simple message
    return render_template('mangalsutras_gct2.html')

@app.route('/earring_gct2.html')
def earring_gct2():
    # You can return a rendered template or a simple message
    return render_template('earring_gct2.html')

@app.route('/earring_rgct2.html')
def earring_rgct2():
    # You can return a rendered template or a simple message
    return render_template('earring_rgct2.html')

@app.route('/bracelets_gct2.html')
def bracelets_gct2():
    # You can return a rendered template or a simple message
    return render_template('bracelets_gct2.html')

@app.route('/bangles_gct2.html')
def bangles_gct2():
    # You can return a rendered template or a simple message
    return render_template('bangles_gct2.html')

@app.route('/buy')
def buy():
    return render_template('buy_page.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
