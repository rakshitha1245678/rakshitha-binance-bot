import logging

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be > 0")
def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are supported")
