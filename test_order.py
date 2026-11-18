
import pytest

from order import (
    calculate_discount,
    calculate_gst,
    calculate_order_total,
)


def test_discount_valid():
    assert calculate_discount(1000, 10) == 100


def test_discount_zero():
    assert calculate_discount(1000, 0) == 0


def test_discount_full():
    assert calculate_discount(1000, 100) == 1000


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(1000, 110)


def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(1000, -10)


def test_gst_calculation():
    assert calculate_gst(1000, 18) == 180


def test_negative_gst_amount():
    with pytest.raises(ValueError):
        calculate_gst(-100, 18)


def test_order_total():
    assert calculate_order_total(1000, 10, 18) == 1062


def test_order_total_no_discount():
    assert calculate_order_total(1000, 0, 18) == 1180
