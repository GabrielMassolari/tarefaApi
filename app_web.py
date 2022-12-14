from flask import Flask, jsonify, request
from db import session, Cliente
from db import Produto, Carrinho, Venda

app = Flask(__name__)


@app.route("/inicio", methods=["GET"])
@app.route("/olamundo", methods=["GET"])
def olamundo():
    return "<h1> Ola Mundo </h1>", 201


# Cliente
@app.route("/cliente", methods=["GET", "POST"])
@app.route("/cliente/<int:id_cliente>", methods=["GET", "PUT", "DELETE"])
def cliente(id_cliente=None):
    if request.method == "GET":
        if id_cliente:
            try:
                cliente = (
                    session.query(Cliente)
                    .filter(Cliente.id == id_cliente)
                    .one()
                )
                return (
                    jsonify({"id": cliente.id,
                             "nome": cliente.nome,
                             "endereco": cliente.endereco,
                             "cpf": cliente.cpf,
                             "email": cliente.email}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_clientes = []
            clientes = session.query(Cliente).all()
            for c in clientes:
                lista_clientes.append({"id": c.id,
                                       "nome": c.nome,
                                       "endereco": c.endereco,
                                       "cpf": c.cpf,
                                       "email": c.email})
            return jsonify(lista_clientes), 200
    elif request.method == "POST":
        cliente = request.json
        session.add(
            Cliente(nome=cliente["nome"],
                    endereco=cliente["endereco"],
                    cpf=cliente["cpf"],
                    email=cliente["email"])
        )
        session.commit()
        return "", 200
    elif request.method == "PUT":
        cliente = request.json
        session.query(Cliente).filter(Cliente.id == id_cliente).update(
            {"nome": cliente["nome"],
             "endereco": cliente["endereco"],
             "cpf": cliente["cpf"],
             "email": cliente["email"]})
        session.commit()
        return "", 200
    elif request.method == "DELETE":
        session.query(Cliente).filter(
            Cliente.id == id_cliente
        ).delete()
        session.commit()
        return "", 200


# Produto
@app.route("/produto", methods=["GET", "POST"])
@app.route("/produto/<int:id_produto>", methods=["GET", "PUT", "DELETE"])
def produto(id_produto=None):
    if request.method == "GET":
        if id_produto:
            try:
                produto = (
                    session.query(Produto)
                    .filter(Produto.id == id_produto)
                    .one()
                )
                return (
                    jsonify({"id": produto.id,
                             "nome": produto.nome,
                             "preco": produto.preco,
                             "descricao": produto.descricao}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_produtos = []
            produtos = session.query(Produto).all()
            for p in produtos:
                lista_produtos.append({"id": p.id,
                                       "nome": p.nome,
                                       "preco": p.preco,
                                       "descricao": p.descricao})
            return jsonify(lista_produtos), 200
    elif request.method == "POST":
        produto = request.json
        session.add(
            Produto(nome=produto["nome"],
                    preco=produto["preco"],
                    descricao=produto["descricao"])
        )
        session.commit()
        return "", 200
    elif request.method == "PUT":
        produto = request.json
        session.query(Produto).filter(Produto.id == id_produto).update(
            {"nome": produto["nome"],
             "preco": produto["preco"],
             "descricao": produto["descricao"]}
        )
        session.commit()
        return "", 200
    elif request.method == "DELETE":
        session.query(Produto).filter(
            Produto.id == id_produto
        ).delete()
        session.commit()
        return "", 200


@app.route("/carrinho", methods=["GET", "POST"])
@app.route("/carrinho/<int:id_carrinho>", methods=["GET", "PUT", "DELETE"])
def carrinho(id_carrinho=None):
    if request.method == "GET":
        if id_carrinho:
            try:
                carrinho = (
                    session.query(Carrinho)
                    .filter(Carrinho.id == id_carrinho)
                    .one()
                )
                return (
                    jsonify({"id": carrinho.id,
                             "preco": carrinho.preco,
                             "qtd": carrinho.qtd,
                             "produto_id": carrinho.produto_id,
                             "venda_id": carrinho.venda_id}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_carrinhos = []
            carrinhos = session.query(Carrinho).all()
            for c in carrinhos:
                lista_carrinhos.append({"id": c.id,
                                        "preco": c.preco,
                                        "qtd": c.qtd,
                                        "produto_id": c.produto_id,
                                        "venda_id": c.venda_id})
            return jsonify(lista_carrinhos), 200
    elif request.method == "POST":
        carrinho = request.json
        session.add(
            Carrinho(preco=carrinho["preco"],
                    qtd=carrinho["qtd"],
                    produto_id=carrinho["produto_id"],
                    venda_id=carrinho["venda_id"])
        )
        session.commit()
        return "", 200
    elif request.method == "PUT":
        carrinho = request.json
        session.query(Carrinho).filter(Carrinho.id == id_carrinho).update(
            {"preco": carrinho["preco"],
             "qtd": carrinho["preco"],
             "produto_id": carrinho["produto_id"],
             "venda_id": carrinho["venda_id"]}
        )
        session.commit()
        return "", 200
    elif request.method == "DELETE":
        session.query(Carrinho).filter(
            Carrinho.id == id_carrinho
        ).delete()
        session.commit()
        return "", 200


@app.route("/venda", methods=["GET", "POST"])
@app.route("/venda/<int:id_venda>", methods=["GET", "PUT", "DELETE"])
def venda(id_venda=None):
    if request.method == "GET":
        if id_venda:
            try:
                venda = (
                    session.query(Venda)
                    .filter(Venda.id == id_venda)
                    .one()
                )
                return (
                    jsonify({"id": venda.id,
                             "cliente_id": venda.cliente_id}),
                    200,
                )
            except Exception as ex:
                return "", 404
        else:
            lista_vendas = []
            vendas = session.query(Venda).all()
            for v in vendas:
                lista_vendas.append({"id": v.id,
                                     "cliente_id": v.cliente_id})
            return jsonify(lista_vendas), 200
    elif request.method == "POST":
        venda = request.json
        session.add(
            Venda(cliente_id=venda["cliente_id"])
        )
        session.commit()
        return "", 200
    elif request.method == "PUT":
        venda = request.json
        session.query(Venda).filter(Venda.id == id_venda).update(
            {"cliente_id": venda["cliente_id"]}
        )
        session.commit()
        return "", 200
    elif request.method == "DELETE":
        session.query(Venda).filter(
            Venda.id == id_venda
        ).delete()
        session.commit()
        return "", 200


app.run(host="0.0.0.0", port=8080)
