from flask import Flask, render_template, url_for, flash, redirect
from templates.forms import PortfolioForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '00e4efeb013b5fc6ce708590b1a4d6a3'


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/interface', methods=['GET', 'POST'])
def interface():
    form = PortfolioForm()
    if form.validate_on_submit():
        flash(f'Inital Investment: {form.username.data}!', 'success')
        flash(f'ticker1: {form.ticker1.data}', 'success')
        flash(f'ticker2: {form.ticker2.data}', 'success')
        flash(f'ticker3: {form.ticker3.data}', 'success')
        flash(f'ticker4: {form.ticker4.data}', 'success')
        return redirect(url_for('about'))
    return render_template('interface.html', title='Ticker', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/urls')
def urls():
    return '<h1>' + url_for('about') + '</h1>'


if __name__ == '__main__':
    app.run(debug=True)
