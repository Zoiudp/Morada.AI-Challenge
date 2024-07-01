from flask import Flask, jsonify, request
from saque import saque

app = Flask(__name__)

@app.route("/api/saque",methods=['POST'])
def api():
    # Esta rota lida com a solicitação POST para o endpoint /api/saque
    # Ela espera um payload JSON com um campo 'valor' indicando o valor a ser sacado
    try:
        valor = request.json['valor']
        if valor <= 1:
            raise ValueError
    except ValueError as v:
        # Se o valor informado for menor que 1, retorna uma mensagem de erro indicando que o valor é inválido
        return jsonify({'erro': f'Erro: {v}! Valor inválido, não é possível sacar valor menor que 1'})
    except KeyError as k:
        # Se o campo 'valor' não estiver presente no payload, retorna uma mensagem de erro
        return jsonify({'erro': f'Erro: {k}! Campo "valor" não encontrado no payload'})
    except TypeError as t:
        # Se o payload não for um JSON válido, retorna uma mensagem de erro
        return jsonify({'erro': f'Erro: {t}! Verifique se o payload está no formato JSON!'})
    except Exception as e:
        # Se ocorrer qualquer outro erro, retorna uma mensagem de erro genérica
        return jsonify({'erro': f'Erro inesperado: {e}!'})
    

    # Chama a função saque com o valor informado e retorna o resultado
    return saque(valor)



if __name__ == "__main__":
    # Executa a aplicação Flask em localhost:5000
    app.run(port='5000', host='localhost', debug=False)
