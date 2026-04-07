import argparse
import sys
from bot.orders import place_futures_order
from bot.validators import validate_order_input
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('--symbol', type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL', 'buy', 'sell'], help="Order side: BUY or SELL")
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT', 'market', 'limit'], dest='order_type', help="Order type: MARKET or LIMIT")
    parser.add_argument('--qty', type=float, required=True, help="Quantity to trade")
    parser.add_argument('--price', type=float, help="Price (Required if type is LIMIT)")

    args = parser.parse_args()

    try:
        # Validate inputs before processing
        symbol, side, order_type, quantity, price = validate_order_input(
            args.symbol, args.side, args.order_type, args.qty, args.price
        )
        
        # Execute trade
        place_futures_order(symbol, side, order_type, quantity, price)
        
    except ValueError as ve:
        logger.error(f"\n[VALIDATION ERROR]: {ve}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()