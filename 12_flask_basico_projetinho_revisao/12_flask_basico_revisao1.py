'''Projetingo: Mini agenda de tarefas(to-do list)
    App web básico em que o usuário pode: adicionar uma tarefa,
                                          visualizar uma lista de tarefa,
                                          remover tarefa
                                          Tudo isso mantendo os dados com session (sem banco de dados)
'''


from flask import Flask, session, request, url_for, jsonify, redirect

app = Flask(__name__)
app.secret_key = 'teste123' #assinatura digital do session


@app.route('/')
def index():
    return redirect(url_for('get_tarefas'))


@app.route('/tarefas', methods=['GET']) # define rota /tarefas, aceita apenas requisição GET
def get_tarefas():
    if 'tarefas' not in session: # sempre que usuário acessar a rota /tarefas e ainda não tiver uma chave 'tarefas' na sessão, será criado uma lista vazia
        session['tarefas'] = []
    return jsonify(session['tarefas']) # retorna a lista session['tarefas'] convertido para JSON


@app.route('/tarefas', methods=['POST'])
def add_tarefas():
    dado = request.get_json() # Ler o corpo da requisição como JSON (POST/PUT)
    tarefa = dado.get('tarefa') # armazena o valor acessado na chave 'tarefa' no json enviado
    if tarefa:
        if 'tarefas' not in session:
            session['tarefas'] = []
        session['tarefas'].append(tarefa)
        session.modified = True # força Flaks a salvar a sessão, mesmo que ele ache que nada mudou /( avisa ao flask que a sessão foi alterada manualmente, mesmo que o objeto session não pareça ter mudado
        return jsonify({'messagem': 'Tarefa Adicionada!', 'tarefas': session['tarefas']})
    return jsonify({'error': 'Campo "tarefa" é obrigatório'}), 400


@app.route('/tarefas/<int:id_tarefa>', methods=['DELETE'])
def del_tarefas(id_tarefa):
    if 'tarefas' in session and 0 <= id_tarefa < len(session['tarefas']):
        remover = session['tarefas'].pop(id_tarefa)
        session.modified = True
        return jsonify({'messagem': f'Tarefa "{remover}" removida com sucesso'})
    return jsonify({'erro': 'ID inválido'}), 400


if __name__ == '__main__':
    app.run(debug=True)


