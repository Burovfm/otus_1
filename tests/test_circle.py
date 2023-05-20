import pytest

from src.circle import Circle


@pytest.mark.parametrize('radius, area, perimeter',
                         [
                             (10, 314, 63),
                             (5, 78.5, 31)
                         ])
def test_circle_positive(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == 'Circle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('radius, area, perimeter',
                         [
                             (7, 153.86, 44),
                             (9, 254.34, 57)
                         ])
def test_circle_positive_2(radius, area, perimeter):
    r = Circle(7)
    assert r.name == 'Circle'
    assert r.get_area() == 153.86
    assert r.get_perimeter() == 44
    r.radius = 9
    assert r.get_area() == 254.34
    assert r.get_perimeter() == 57


@pytest.mark.parametrize('radius', [-22, 0])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(-10)


def test_areas_sum():
    expected_sum = 327
    circle_1 = Circle(10)
    circle_2 = Circle(2)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'])
def test_areas_sum_negative(some_other_class):
    circle_1 = Circle(10)
    with pytest.raises(ValueError):
        circle_1.add_area(some_other_class)