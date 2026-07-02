import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do e-mail
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '963cd577c7883b'
app.config['MAIL_PASSWORD'] = 'c3fac32b3a4ca1'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estudante')
def estudante():
    return render_template('estudante.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    pedido = request.form['pedido']
    ficheiro = request.files['ficheiro'] # Apanha o ficheiro do formulário
    
    if ficheiro:
        # Guarda o ficheiro na pasta 'uploads'
        ficheiro.save(os.path.join('uploads', ficheiro.filename))
    
    msg = Message("Novo Pedido de Formatação", sender='noreply@academiai.com', recipients=['o_teu_email@email.com'])
    msg.body = f"Nome: {nome}\nEmail: {email}\nPedido: {pedido}"
    mail.send(msg)
    
    return "Pedido de formatação recebido com sucesso e ficheiro guardado!"

@app.route('/enviar_curriculo', methods=['POST'])
def enviar_curriculo():
    nome = request.form['nome']
    email = request.form['email']
    objetivo = request.form['objetivo']
    ficheiro = request.files['ficheiro'] # Apanha o ficheiro do formulário
    
    if ficheiro:
        # Guarda o ficheiro na pasta 'uploads'
        ficheiro.save(os.path.join('uploads', ficheiro.filename))
    
    msg = Message("Novo Pedido de Currículo", sender='noreply@academiai.com', recipients=['o_teu_email@email.com'])
    msg.body = f"Nome: {nome}\nEmail: {email}\nObjetivo: {objetivo}"
    mail.send(msg)
    
    return "Pedido de currículo recebido com sucesso e ficheiro guardado!"

if __name__ == '__main__':
    # Garante que a pasta uploads existe
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)