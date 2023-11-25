from flask import render_template, redirect, url_for
from crm import app
from crm.models import Motivo, db
from crm.forms import MotivoForm

@app.route('/')
def index():
    motivos = Motivo.query.all()
    return render_template('index.html', motivos=motivos)

@app.route('/add_motivo', methods=['GET', 'POST'])
def adicionar_motivo():  
    form = MotivoForm()

    if form.validate_on_submit():
        novo_motivo = Motivo(descricao_chamada=form.descricao_chamada.data)
        db.session.add(novo_motivo)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_motivo.html', form=form)
