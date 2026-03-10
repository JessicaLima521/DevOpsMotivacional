from frases import gerar_frase

def test_frase():
    frase = gerar_frase()
    assert frase != ""