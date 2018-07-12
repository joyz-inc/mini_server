from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = TextField('name', validators=[DataRequired()])