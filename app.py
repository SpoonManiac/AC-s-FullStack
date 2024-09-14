from flask import Flask, render_template, request, redirect
import os

class Questoes:
    def __init__(self, nome, imagem, link_ver_mais):
        self.nome = nome
        self.imagem = imagem
        self.link_ver_mais = link_ver_mais
    

resp1 = Questoes("Client-server e MVC", "/static/img/resp1.png", "http://127.0.0.1:5000/resp1")
resp2 = Questoes("FrameWork", "/static/img/resp2.png", "http://127.0.0.1:5000/resp2")
resp3 = Questoes("Bootstrap", "/static/img/resp3.png" , "http://127.0.0.1:5000/resp3")
resp4 = Questoes("CDN", "/static/img/resp4.png" , "http://127.0.0.1:5000/resp4")
resp5 = Questoes("Simplicidade do Flask", "/static/img/resp5.png" , "http://127.0.0.1:5000/resp5")

lista = [resp1, resp2, resp3, resp4, resp5]

app = Flask(__name__)

PASTA_UPLOAD = "static/img"
app.config[PASTA_UPLOAD] = PASTA_UPLOAD

@app.route('/')
def index():
    return render_template('index.html', cat=lista)


@app.route('/resp1')
def resp1():
     return render_template('resp1.html', nomePag='Arquitetura Cliente-Servidor', cat=lista)

@app.route('/resp2')
def resp2():
    return render_template('resp2.html', nomePag="Benefícios de Usar um Framework", cat=lista)

@app.route('/resp3')
def resp3():
    return render_template('resp3.html', nomePag="Sobre o Bootstrap", cat=lista)

@app.route('/resp4')
def resp4():
    return render_template('resp4.html', nomePag="Sobre CDN", cat=lista)

@app.route('/resp5')
def resp5():
    return render_template('resp5.html', nomePag="Simplicidade do Flask" , cat=lista)


@app.route('/admin')
def adicionar():
    return render_template('adicionar.html', titulo='Respostinhas cabulosas')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    imagem = request.files.get('imagem')
    link_ver_mais = request.form.get('link_ver_mais')

    if imagem and imagem.filename != '':
        filename = os.path.join(app.config[PASTA_UPLOAD], imagem.filename)
        imagem.save(filename)
        imagem_url = f"/static/img/{imagem.filename}"

    else:
        imagem_url = "/static/img/default-image.gif"

    if not link_ver_mais:
        link_ver_mais = "https://pbs.twimg.com/profile_images/1643667108461412365/9nUoGvqY_400x400.jpg"


    respostas = Questoes(nome, imagem_url, link_ver_mais)
    lista.append(respostas)
    return redirect('/')

app.run(debug=True)