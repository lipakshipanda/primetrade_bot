# Binance Futures Testnet Trading Bot

A lightweight, structured Python CLI application to execute Market and Limit orders on the Binance Futures Testnet (USDT-M). 

## Project Structure
Following the suggested architecture, the application separates the API client layer, order execution logic, and CLI command handling:
* `cli.py`: The main entry point for user interaction and argument parsing.
* `bot/client.py`: Handles API authentication and client initialization.
* `bot/orders.py`: Executes the order logic and formats API responses.
* `bot/validators.py`: Ensures CLI inputs are safe and correctly typed.
* `bot/logging_config.py`: Manages console output and file logging.

## Setup Instructions
1. Clone the repository or extract the zip file.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
3. Install the dependencies:
    ```bash
     pip install -r requirements.txt
4. Create a .env file in the root directory and add your Binance Testnet keys:
    ```bash
     BINANCE_API_KEY=your_api_key_here
    BINANCE_API_SECRET=your_secret_key_here
## How to Run Examples
   Execute a Market Buy Order:
    ```bash
     python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
    Execute a Limit Sell Order:
    ```bash  
      python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 95000
## Assumptions & Notes
 API Mocking: During testing, the Binance Testnet initiated a hard KYC block on the IP address, preventing live API calls from resolving. To demonstrate the functionality of the CLI, validation architecture, and logging system, an API mock was engineered within orders.py to simulate network latency and generate the expected exchange responses.

 Logging is configured to output clean summaries to the console while saving detailed API JSON responses to trading_bot.log.
