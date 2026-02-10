import sys
from config import client
from utils import validate_side, validate_quantity, validate_symbol

import logging

def place_market_order(symbol, side, quantity):
    try:
        validate_side(side)
        validate_quantity(quantity)

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Market order placed: {order}")
        print("✅ Market order placed successfully")

    except Exception as e:
        logging.error(f"Market order failed: {e}")
        print("❌ Error placing market order")

if __name__ == "__main__":
    # CLI arguments
    # python src/market_orders.py BTCUSDT BUY 0.01
    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])

    place_market_order(symbol, side, quantity)
