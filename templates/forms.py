from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class PortfolioForm(FlaskForm):
    username = StringField('Initial Investment', validators=[
                           DataRequired(), Length(min=2, max=20)])
    ticker1 = StringField('Ticker 1', validators=[
        DataRequired(), Length(min=2, max=20)])
    ticker2 = StringField('Ticker 2', validators=[
        DataRequired(), Length(min=2, max=20)])
    ticker3 = StringField('Ticker 3', validators=[
        DataRequired(), Length(min=2, max=20)])
    ticker4 = StringField('Ticker 4', validators=[
        DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Calculate')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class OldForm(FlaskForm):
    username = StringField('Initial Investment', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Find Stock')
