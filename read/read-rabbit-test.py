def test_execucao():
    assert True
    
def test_contem_test():
    mensagem = "teste do arquivo read"
    assert "test" in mensagem.lower()
    
def test_soma():
    resultado = 2 + 3
    assert resultado == 5

def test_subtracao():
    resultado = 5 - 2
    assert resultado == 3

def test_multiplicacao():
    resultado = 4 * 3
    assert resultado == 12

def test_divisao():
    resultado = 8 / 2
    assert resultado == 4

def test_potencia():
    resultado = 2 ** 3
    assert resultado == 8
    