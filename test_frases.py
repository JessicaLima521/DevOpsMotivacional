from frases import mostrar_frase

def test_frase():

    
    frase = mostrar_frase()
    
    assert frase != ""

def test_tipo_string():
    
    assert isinstance(mostrar_frase(), str)

def test_nao_vazia():
    
    assert mostrar_frase() != ""

def test_tamanho():
    
    assert len(mostrar_frase()) > 3

def test_nao_none():
    assert mostrar_frase() is not None
