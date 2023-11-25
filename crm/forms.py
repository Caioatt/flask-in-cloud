from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MotivoForm(FlaskForm):
    descricao_chamada = StringField('Descrição da Chamada', validators=[DataRequired()])
    submit = SubmitField('Salvar')
