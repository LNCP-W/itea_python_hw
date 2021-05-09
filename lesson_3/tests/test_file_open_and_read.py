from lesson_3.hw_3_3 import write_nub, translate_numb
import pytest

@pytest.mark.parametrize('result', [(['One - 1\n', 'Two - 2\n', 'Three - 3\n', 'Four - 4'])])
def test_wr_nmb(result):
    write_nub()
    f1 = open('file_1.txt', 'r')
    f = f1.readlines()
    f1.close()
    assert f == result

@pytest.mark.parametrize('result', [(['Один - 1\n', 'Два - 2\n', 'Три - 3\n', 'Четыре - 4'])])
def test_translate_numb(result):
    translate_numb()
    f1 = open('file_2.txt', 'r')
    f=f1.readlines()
    f1.close()
    assert f == result

