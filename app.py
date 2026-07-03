import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do e-mail (Mailtrap)
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '963cd577c7883b'
app.config['MAIL_PASSWORD'] = 'c3fac32b3a4ca1'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/termos')
def termos():
    return render_template('termos.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    if request.form.get('website'):
        return "Erro de segurança: Acesso negado.", 403

    nome = request.form['nome']
    email = request.form['email']
    servico = request.form['servico']
    pedido = request.form['pedido']
    ficheiro = request.files['ficheiro']
    
    # 2. Configuração das mensagens
    # Recipient: O teu e-mail real onde queres receber os pedidos
    recipients = [ruben.rodrigues1503@gmail.com] 
    
    msg = Message(f"Novo Pedido AcademiAI: {nome}", 
                  sender='noreply@academiai.com', 
                  recipients=recipients)
    
    msg.body = f"Novo cliente: {nome}\nE-mail: {email}\nServiço: {servico}\n\nPedido:\n{pedido}"
    
    # 3. Processamento do ficheiro
    if ficheiro and ficheiro.filename:
        caminho_completo = os.path.join(app.config['UPLOAD_FOLDER'], ficheiro.filename)
        ficheiro.save(caminho_completo)
        
        with open(caminho_completo, "rb") as f:
            msg.attach(ficheiro.filename, ficheiro.content_type, f.read())
    
    #mail.send(msg)
    return "Pedido recebido com sucesso! Entraremos em contacto brevemente."

if __name__ == '__main__':
    app.run(debug=True)