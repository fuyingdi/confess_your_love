from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MyloveForm(FlaskForm):
    """定义一个表单类"""
    myname = StringField('你的名字|',validators=[
                DataRequired(message= u'邮箱不能为空'), Length(1, 64)])
    lovername = StringField('你喜欢的人的名字',validators=[
                DataRequired(message= u'邮箱不能为空'), Length(1, 64)])
    submit = SubmitField('献上你的爱')
