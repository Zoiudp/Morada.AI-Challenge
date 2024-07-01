from flask import jsonify, request

def saque(valor):
    # Lista de notas disponíveis para saque
    notas = [100, 50, 20, 10, 5, 2]
    resultado = []

    try:
        if valor.is_integer() != True:
            raise TypeError
    except TypeError:
        # Se o valor informado não for um número inteiro, retorna uma mensagem de erro indicando que o valor é inválido
        return jsonify({'erro': 'Valor inválido, não é possível sacar valor!'})

    try:
        if valor >= 5000:
            raise ValueError
    except ValueError:
        # Se o valor informado for maior ou igual a 5000, retorna uma mensagem de erro indicando que o valor é inválido
        return jsonify({'erro': 'Valor máximo para saque é de R$ 5000,00! Caso queira sacar um valor maior, favor entrar em contato com o banco!'})

    # Itera pela lista de notas disponíveis e calcula a quantidade de cada nota necessária para sacar o valor informado
    for nota in notas:
        if valor >= nota:
            qtd_notas = valor // nota
            resultado.append({nota: qtd_notas})
            valor = valor % nota
            try:
                if valor == 1:
                    raise ValueError
            except ValueError:
                return jsonify({'erro': 'Saque impossivel. Por favor acrescente mais 1 real para completar o saque!'})
        else:
            resultado.append({nota: 0})
    # Retorna o resultado como uma resposta JSON
    return jsonify(resultado)

