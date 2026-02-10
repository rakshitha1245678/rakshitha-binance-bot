import sys
import time
import logging
from src.config import client
from src.utils import validate_side, validate_quantity, validate_symbol

def place_twap_order(symbol, side, total_quantity, slices, interval):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(total_quantity)

        slice_qty = round(total_quantity / slices, 6)

        for i in range(slices):
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=slice_qty
            )

            logging.info(f"TWAP slice {i+1}/{slices}: {order}")
            print(f"✅ TWAP order slice {i+1}/{slices} placed")

            if i < slices - 1:
                time.sleep(interval)

    except Exception as e:
        logging.error(f"TWAP order failed: {e}")
        print("❌ Error placing TWAP order")

if __name__ == "__main__":
    # python -m src.advanced.twap BTCUSDT BUY 0.05 5 10
    symbol = sys.argv[1]
    side = sys.argv[2]
    total_quantity = float(sys.argv[3])
    slices = int(sys.argv[4])
    interval = int(sys.argv[5])

    place_twap_order(symbol, side, total_quantity, slices, interval)
