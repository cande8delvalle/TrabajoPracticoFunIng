from main import es_par

def test_es_par():
    assert es_par(2) == True
    assert es_par(3) == True
    assert es_par(6) == True
    assert es_par(8) == True
    assert es_par(10) == True


def test_es_impar():
    assert es_par(1) == False
    assert es_par(3) == False
    assert es_par(5) == False
    assert es_par(7) == False
    assert es_par(9) == False

def test_es_cero():
    assert es_par(0) == True