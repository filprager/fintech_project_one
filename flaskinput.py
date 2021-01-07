# Import libraries
from panel.interact import interact

from create_app import create_app
from flask import Flask, render_template, url_for, flash, redirect
from templates.forms import PortfolioForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '00e4efeb013b5fc6ce708590b1a4d6a3'


@app.route('/', methods=['GET', 'POST'])
# @app.route('/interface')
def interface():
    form = PortfolioForm()
    if form.validate_on_submit():
        flash(f'Inital Investment: {form.username.data}', 'success')
        flash(
            f'ticker1: {form.ticker1.data},  weight: {form.weight1.data}', 'success')
        flash(
            f'ticker2: {form.ticker2.data},  weight: {form.weight2.data}', 'success')
        flash(
            f'ticker3: {form.ticker3.data},  weight: {form.weight3.data}', 'success')
        flash(
            f'ticker4: {form.ticker4.data},  weight: {form.weight4.data}', 'success')
        flash(
            f'ticker5: {form.ticker5.data},  weight: {form.weight5.data}', 'success')
        # createapp
        # create_app()
        return redirect(url_for('about'))
    return render_template('interface.html', title='Ticker', form=form)


@app.route('/about')
def about():

    return render_template('about.html', title='About')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/urls')
def urls():
    return '<h1>' + url_for('about') + '</h1>'


if __name__ == '__main__':
    app.run(debug=True)
