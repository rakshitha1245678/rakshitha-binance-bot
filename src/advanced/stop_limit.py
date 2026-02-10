import sys
import logging
from src.config import client
from src.utils import validate_side, validate_quantity, validate_symbol


def validate_price(price, name):
    if price <= 0:
        raise ValueError(f"{name} must be > 0")

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(quantity)
        validate_price(stop_price, "Stop price")
        validate_price(limit_price, "Limit price")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=limit_price,
            stopPrice=stop_price,
            timeInForce="GTC"
        )

        logging.info(f"Stop-Limit order placed: {order}")
        print("✅ Stop-Limit order placed successfully")

    except Exception as e:
        logging.error(f"Stop-Limit order failed: {e}")
        print("❌ Error placing stop-limit order")

if __name__ == "__main__":
    # python src/advanced/stop_limit.py BTCUSDT SELL 0.01 44500 44300
    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    stop_price = float(sys.argv[4])
    limit_price = float(sys.argv[5])

    place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
