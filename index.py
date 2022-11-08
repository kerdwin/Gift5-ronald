from flask import Flask, request, redirect, url_for,render_template


app = Flask (__name__)
@app.route('/')
def home():
        return render_template('Home1.html')

@app.route ('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)