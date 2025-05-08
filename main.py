from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = "aqui_e_a_minha_chave"

livros = []

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        livros.append({
            'titulo': titulo,
            'autor': autor,
            'emprestado': False,
            'data_devolucao': None,
            'multas': 0
        })
        flash('Livro cadastrado com sucesso!')
        return redirect('/')
    return render_template('adicionar_livro.html')

@app.route('/editar_livro/<int:codigo>', methods=['GET', 'POST'])
def editar_livro(codigo):
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        livros[codigo]['titulo'] = titulo
        livros[codigo]['autor'] = autor
        return redirect('/')
    return render_template('editar_livro.html', livro=livros[codigo])

@app.route('/apagar_livro/<int:codigo>')
def apagar_livro(codigo):
    del livros[codigo]
    return redirect('/')

@app.route('/emprestar_livro/<int:codigo>')
def emprestar_livro(codigo):
    livro = livros[codigo]
    if not livro['emprestado']:
        livro['emprestado'] = True
        livro['data_devolucao'] = '7 dias'  # Usando string simples
        flash('Livro emprestado com sucesso!')
    return redirect('/')

@app.route('/devolver_livro/<int:codigo>')
def devolver_livro(codigo):
    livro = livros[codigo]
    if livro['emprestado']:
        livro['emprestado'] = False
        livro['data_devolucao'] = None
        flash('Livro devolvido com sucesso!')
    return redirect('/')

@app.route('/catalogo')
def catalogo():
    generos = ['Romance', 'Ficção', 'Suspense', 'Fantasia', 'Terror']
    return render_template('catalogo.html', generos=generos)

if __name__ == '__main__':
    app.run(debug=True)