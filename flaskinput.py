# Import libraries
from panel.interact import interact

from create_app import create_app
from flask import Flask, render_template, url_for, flash, redirect
from templates.forms import PortfolioForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '00e4efeb013b5fc6ce708590b1a4d6a3'


def my_func():
    my_num = 6
    return my_num


@app.route('/')
@app.route('/about')
def about():
    my_func
    print('testing')
    return render_template('about.html', title='About')


@app.route('/interface', methods=['GET', 'POST'])
def interface():
    # def my_func():
    #     my_num = 4
    #     return my_num

    form = PortfolioForm()
    if form.validate_on_submit():
        my_num = 2
        print(my_num)

        flash(f'Inital Investment: {form.username.data}!', 'success')
        flash(f'ticker1: {form.ticker1.data}', 'success')
        flash(f'ticker2: {form.ticker2.data}', 'success')
        flash(f'ticker3: {form.ticker3.data}', 'success')
        flash(f'ticker4: {form.ticker4.data}', 'success')
        flash(f'show my function: {create_app()}')
        # createapp
        # output = create_app('MSFT', 'DIS', 0.5, 0.5)
        # create_app()
        my_func
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
