from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'some_secret'  # Needed for flashing messages

@app.route('/')
def home():
    # Pass personal info to template if needed
    return render_template('index.html', name="Your Name", about="A short bio", skills=["Python", "Flask"])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For demo, just flash a message (In real, you might send an email)
        flash('Thank you for contacting!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
