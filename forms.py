from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class indexForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    phrase = StringField('Winning Phrase', validators=[DataRequired()])
    submit = StringField('Enter the Game')