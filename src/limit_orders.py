import sys
import logging
from config import client
from utils import validate_side, validate_quantity
from utils import validate_side, validate_quantity, validate_symbol


def validate_price(price):
    if price <= 0:
        raise ValueError("Price must be > 0")

def place_limit_order(symbol, side, quantity, price):
    try:
        validate_side(side)
        validate_quantity(quantity)
        validate_price(price)

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit order placed: {order}")
        print("✅ Limit order placed successfully")

    except Exception as e:
        logging.error(f"Limit order failed: {e}")
        print("❌ Error placing limit order")

if __name__ == "__main__":
    # python src/limit_orders.py BTCUSDT SELL 0.01 50000
    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    price = float(sys.argv[4])

    place_limit_order(symbol, side, quantity, price)
