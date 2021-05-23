from lesson_3.hw_3_2 import Matrix
import pytest


@pytest.mark.parametrize('mat_1, mat_2, mat_result',
                         [
                          ([[1, 1], [1, 1]],
                           [[1, 1], [1, 1]],
                           [[2, 2], [2, 2]]),

                          ([[1, 2, 3], [4, 5, 6]],
                           [[6, 5, 4], [3, 2, 1]],
                           [[7, 7, 7], [7, 7, 7]]),

                          ([[0, 5, 3], [255, 5, 6], [4, 5, 6]],
                           [[0, 5, 3], [3, -5, 1], [4, 5, 6]],
                           [[0, 10, 6], [258, 0, 7], [8, 10, 12]])
                         ])
def test_add_matrix(mat_1, mat_2, mat_result):
    m1 = Matrix(mat_1)
    m2 = Matrix(mat_2)
    res = m1 + m2
    assert res.mat == mat_result
    

@pytest.mark.parametrize('mat_1, mat_2, mat_result',
                         [
                          ([[1, 1], [1, 1]],
                           [[1, 1], [1, 1]],
                           [[0, 0], [0, 0]]),

                          ([[1, 2, 3], [4, 5, 6]],
                           [[6, 5, 4], [3, 2, 1]],
                           [[-5, -3, -1], [1, 3, 5]]),

                          ([[0, 5, 3], [255, 5, 6], [4, 55, 6]],
                           [[0, 0, 6], [3, -5, 1], [0, 5, 16]],
                           [[0, 5, -3], [252, 10, 5], [4, 50, -10]])
                           ])
def test_sub_matrix(mat_1, mat_2, mat_result):
    m1 = Matrix(mat_1)
    m2 = Matrix(mat_2)
    res = m1 - m2
    assert res.mat == mat_result
    
    
@pytest.mark.parametrize('mat_1,multiplier, mul_res', [
                          ([[1, 1], [1, 1]],
                           1,
                           [[1, 1], [1, 1]]),

                          ([[1, 2, 3], [4, 5, 6]],
                           5,
                           [[5, 10, 15], [20, 25, 30]]),

                          ([[0, 5, 3], [25, -5, 6], [4, 55, 6]],
                           -5,
                           [[0, -25, -15], [-125, 25, -30], [-20, -275, -30]])

                          ])
def test_mul_matrix(mat_1, multiplier, mul_res):
    m1 = Matrix(mat_1)
    res = m1 * multiplier
    assert res.mat == mul_res
    

@pytest.mark.parametrize('mat_1, divizor, res_div',[
                          ([[1, 1], [1, 1]],
                           1,
                           [[1, 1], [1, 1]]),

                          ([[1, 2, 3], [4, 5, 6]],
                           5,
                           [[.2, .4, .6], [.8, 1, 1.2]]),

                          ([[0, 5, 3], [25, -5, 6], [4, 55, 6]],
                           -5,
                           [[0, -1, -.6], [-5, 1, -1.2], [-.8, -11, -1.2]])

                           ])
def test_div_matrix(mat_1, divizor, res_div):
    m1 = Matrix(mat_1)
    res = m1 / divizor
    assert res.mat == res_div
    
    
@pytest.mark.parametrize('mat_1, divizor, exc_type', [
([[0, 5, 3], [25, -5, 6], [4, 55, 6]],
                           0,
                           ZeroDivisionError)
])
def test_div_matrix_with_eror(mat_1, divizor, exc_type):
    m1=Matrix(mat_1)
    with pytest.raises(exc_type):
        m1 / divizor



@pytest.mark.parametrize('mat_1, output', [
    ([[1, 1], [1, 1]],
     '\n[1, 1]\n[1, 1]'),

    ([[1, 2, 3], [4, 5, 6]],
     '\n[1, 2, 3]\n[4, 5, 6]'),

    ([[0, -1, -0.6], [-5, 1, -1.2], [-.8, -11, -1.2]],
     '\n[0, -1, -0.6]\n[-5, 1, -1.2]\n[-0.8, -11, -1.2]')
])
def test_frendly_out_matrix(mat_1, output):
    m1 = str(Matrix(mat_1))
    assert m1 == output
