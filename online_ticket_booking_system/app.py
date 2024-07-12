from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        movie = request.form['movie']
        time = request.form['time']
        # Here you can add code to save booking to a database or perform other actions
        return redirect(url_for('confirmation', name=name, movie=movie, time=time))
    return render_template('booking.html')

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    movie = request.args.get('movie')
    time = request.args.get('time')
    return render_template('confirmation.html', name=name, movie=movie, time=time)

if __name__ == '__main__':
    app.run(debug=True)
