from Tassimo import Tassimo


def test_make_coffee():
    """
    Tests whether continuous call of
    make_coffee() crashes the program
    :return:
    """
    tassimo = Tassimo()

    for i in range(10):
        tassimo.make_coffee()
