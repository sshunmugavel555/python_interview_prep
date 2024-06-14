from shopping_cart import ShoppingCart
import pytest
from price_map import PriceMap
from unittest.mock import Mock

@pytest.fixture
def sCart():
    """ Fixture to create a shopping cart object that can be used across all methods """
    return ShoppingCart(5)

def test_can_add_items_to_cart(sCart):
    """ Test method to verify if items can be added to the cart """
    #sCart = ShoppingCart(5)
    sCart.add("Mango")
    assert sCart.size()==1

def test_if_item_is_added_to_cart(sCart):
    """ Test to verify if item is added to the cart """
    #sCart = ShoppingCart(5)
    sCart.add("Apple")
    assert "Apple" in sCart.get_items()

def test_verify_exception_if_cart_loaded_beyond_maxsize(sCart):
    """ Verify the exception when the cart is loaded more than the capacity """
    #sCart = ShoppingCart(3)
    for x in range(4):
        sCart.add("grapes")
    
    try:
        sCart.add("grapes")
    except Exception as e:
        assert str(e)=='You are adding more than the capacity of the cart!'

def test_can_get_total_price(sCart):
    """ Verify if total price of the shopping cart can be pritned """
    #sCart = ShoppingCart(5)
    sCart.add("apple")
    sCart.add("orange")

    def mock_item_price(item):
        """ Mock Function for item prices """
        if item == 'apple':
            return 2.0
        if item == 'orange':
            return 3.0

    price_map = PriceMap()
    #price_map.getty = Mock(return_value=2.0)
    price_map.getty = Mock(side_effect=mock_item_price)
    total_price = sCart.get_total_price(price_map)
    assert total_price == 5.0