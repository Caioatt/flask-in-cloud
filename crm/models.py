from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Motivo(db.Model):
    id_motivo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao_chamada = db.Column(db.String(70), nullable=False)
