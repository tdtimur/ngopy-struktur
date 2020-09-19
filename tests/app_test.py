from app import lalu_lintas


def test_lalu_lintas():
    hasil = lalu_lintas(1)
    assert hasil == 'Jalan ditutup'
