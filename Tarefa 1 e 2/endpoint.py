from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Extrair os dados do formulário do corpo da requisição
    data = request.form

    # Validar os dados
    total_percent = 0
    for key in data.keys():
        if key.startswith('email'):
            email = data[key]
            if '@' not in email:
                error = 'E-mail inválido: {}'.format(email)
                return jsonify({'success': False, 'error': error})
        elif key.startswith('percentage'):
            try:
                percent = float(data[key])

            except:
                error = 'Percentual inválido: {}'.format(percent)
                return jsonify({'success': False, 'error': error})
            total_percent += percent
            if percent < 0 or percent > 100:
                error = 'Percentual inválido: {}'.format(percent)
                return jsonify({'success': False, 'error': error})

    if total_percent != 100:
        error = 'A soma dos percentuais deve ser igual a 100%'
        return jsonify({'success': False, 'error': error})

    # Armazenar os dados no banco de dados

    # Retornar a resposta de sucesso
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
