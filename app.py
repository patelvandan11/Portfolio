# app.py
from flask import Flask, render_template, request 
# from flask_pymongo import PyMongo
# from flask_pymongo import PyMongo
app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)
@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = request.form['email']
    #     message = request.form['message']
    #     # Inserting data into MongoDB
    #     contact_data = {'name': name, 'email': email, 'message': message}
    #     mongo.db.collection.insert_one(contact_data)
    #     return render_template('contact.html')
    return render_template('contact.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/paintings', methods=['GET', 'POST'])
def paintings():
    return render_template('paintings.html')

@app.route('/karl_pearson', methods=['GET', 'POST'])
def karl_pearson():
    return render_template('karl_pearson.html')

@app.route('/karl_pearson_out', methods=['POST'])
def karl_pearson_out():
    try:
        n = int(request.form['n'])
        x_values = [float(x) for x in request.form['x'].split(',')]
        y_values = [float(y) for y in request.form['y'].split(',')]

        x_sum = sum(x_values)
        y_sum = sum(y_values)
        xy_sum = sum(x * y for x, y in zip(x_values, y_values))
        x_squared_sum = sum(x ** 2 for x in x_values)
        y_squared_sum = sum(y ** 2 for y in y_values)

        numerator = n * xy_sum - x_sum * y_sum
        denominator = ((n * x_squared_sum - x_sum ** 2) * (n * y_squared_sum - y_sum ** 2)) ** 0.5

        result = numerator / denominator

        return render_template('karl_pearson_out.html', result=result)
    except Exception as e:
        error_message = str(e)
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
