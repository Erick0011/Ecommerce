from flask import render_template, request, redirect, url_for
from app import app
from extensions import db  # 🔥 Importamos `db` do `extensions.py`
from models import Produto, ImagemProduto
import os
from werkzeug.utils import secure_filename
from utils import allowed_file


@app.route('/')
def index():
    produtos = Produto.query.all()
    # Buscando o produto com id = 1
    destaque1 = Produto.query.filter_by(id=1).first()
    categorias = ["Eletrônicos", "Roupas", "Calçados", "Acessórios", "Beleza", "Casa & Jardim", "Brinquedos"]
    return render_template('index.html', title="Home", produtos=produtos, destaque1=destaque1, categorias=categorias)


@app.route('/admin')
def admin():
    produtos = Produto.query.all()
    return render_template('admin.html', produtos=produtos)


@app.route('/delete_produto/<int:produto_id>', methods=['POST'])
def delete_produto(produto_id):
    produto = Produto.query.get(produto_id)


    db.session.delete(produto)
    db.session.commit()



    return redirect(url_for('admin'))


@app.route('/admin/add', methods=['POST'])
def add_produto():
    nome = request.form.get('nome')
    preco = float(request.form.get('preco'))
    descricao = request.form.get('descricao')
    quantidade = int(request.form.get('quantidade'))

    novo_produto = Produto(nome=nome, preco=preco,
                           descricao=descricao, quantidade=quantidade)
    db.session.add(novo_produto)
    db.session.commit()

    # Upload de imagens
    arquivos = request.files.getlist('imagens')
    for arquivo in arquivos[:5]:  # Limite de 5 imagens
        if arquivo and allowed_file(arquivo.filename):
            # Criar um nome único para a imagem usando o nome do produto e o ID
            ext = os.path.splitext(arquivo.filename)[1]  # Extensão da imagem
            # Nome final da imagem
            novo_nome_imagem = f"{novo_produto.nome}_{novo_produto.id}{ext}"
            # Garante que o nome seja seguro
            filename = secure_filename(novo_nome_imagem)
            caminho_imagem = os.path.join(
                app.config['UPLOAD_FOLDER'], filename)
            arquivo.save(caminho_imagem)

            nova_imagem = ImagemProduto(
                produto_id=novo_produto.id, caminho=f'uploads/{filename}')
            db.session.add(nova_imagem)

    db.session.commit()
    return redirect(url_for('admin'))
