from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MyloveForm(FlaskForm):
    """定义一个表单类"""
    myname = StringField('你的名字|', validators=[
        DataRequired(Length(1, 64))])
    lovername = StringField('你喜欢的人的名字', validators=[
        DataRequired(Length(1, 64))])
    comment = StringField("想告诉ta的话")
    submit = SubmitField('悄悄表白')
