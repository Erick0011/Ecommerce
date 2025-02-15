from extensions import db  # 🔥 Agora importamos do `extensions.py`


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    quantidade = db.Column(db.Integer, nullable=False,
                            default=1)  # Quantidade disponível
    # Relacionamento com imagens
    imagens = db.relationship('ImagemProduto', backref='produto', lazy=True)


class ImagemProduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey(
        'produto.id'), nullable=False)
    # Caminho da imagem no static/uploads
    caminho = db.Column(db.String(200), nullable=False)
