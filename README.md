# Binance USDT-M Futures Order Bot (CLI)

This project is a **CLI-based trading bot** for **Binance USDT-M Futures** developed as part of an assignment.  
It supports **basic and advanced order types** with proper **input validation**, **structured logging**, and **modular code design**.

⚠️ This bot is configured to run on **Binance Futures Testnet only**. No real funds are used.

---

## 📂 Project Structure

rakshitha_binance_bot/
│
├── src/
│ ├── config.py # Binance API configuration
│ ├── utils.py # Validation & logging helpers
│ ├── market_orders.py # Market order logic
│ ├── limit_orders.py # Limit order logic
│ │
│ └── advanced/
│ ├── stop_limit.py # Stop-Limit order
│ └── twap.py # TWAP strategy
│
├── bot.log # Structured logs
├── README.md
└── .env # API keys (not committed)


---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
- Python 3.9+
- Binance Futures Testnet account

### 2️⃣ Install dependencies
```bash
pip install python-binance python-dotenv

3️⃣ API Configuration

Create a .env file in the project root:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key

▶️ How to Run the Bot (CLI Usage)

All commands must be run from the project root directory.

✅ Market Order
python -m src.market_orders BTCUSDT BUY 0.01

✅ Limit Order
python -m src.limit_orders BTCUSDT SELL 0.01 50000

⭐ Stop-Limit Order
python -m src.advanced.stop_limit BTCUSDT SELL 0.01 44500 44300

⭐ TWAP (Time-Weighted Average Price)
python -m src.advanced.twap BTCUSDT BUY 0.05 5 10


Explanation:

Total Quantity: 0.05

Number of slices: 5

Interval between orders: 10 seconds

📌 Supported Order Types
Core Orders

Market Orders

Limit Orders

Advanced Orders

Stop-Limit Orders

TWAP (Time-Weighted Average Price)

🧾 Logging & Validation

All actions are logged to bot.log

Inputs such as symbol, quantity, side, and prices are validated

Errors and API failures are logged with timestamps

🔐 Safety Notes

This bot uses Binance Futures Testnet

No real funds are involved

API keys are stored securely using environment variables

📄 Report

Please refer to report.pdf for:

Execution screenshots

Order examples

Log samples

Explanation of strategies


---

# ✅ What you just achieved with this README

✔ Clear setup  
✔ Reproducible steps  
✔ CLI examples  
✔ Matches assignment exactly  
✔ Easy **10% marks**

---

## 🟢 NEXT (Last steps remaining)

Only **2 things left**:
1. `report.pdf` (screenshots + explanation)
2. Zip + GitHub submission

Reply with **one word**:
👉 **`report`** or **`final submission`**

We’ll finish this cleanly 💪