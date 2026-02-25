# telegram bot entry

from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN

async def help(update, context):
    await update.message.reply_text(
        "Available commands:\n\n"
        "/price BTC - Get crypto price\n"
        "/stock AAPL - Get stock price\n"
        "/chart BTC - Get price chart\n"
        "/alert BTC 50000 - Set price alert\n"
        "/alerts - List your alerts\n"
        "/delalert 1 - Delete alert"
    )

async def start(update, context):
    await update.message.reply_text(
        "Welcome to StockTrackerHubBot!\n\n"
        "Use /help to see available commands."
    )

async def price(update, context):
    await update.message.reply_text("Price command - not implemented yet")

async def stock(update, context):
    await update.message.reply_text("Stock command - not implemented yet")

async def chart(update, context):
    await update.message.reply_text("Chart command - not implemented yet")

async def alert(update, context):
    await update.message.reply_text("Alert command - not implemented yet")

async def alerts(update, context):
    await update.message.reply_text("Alerts command - not implemented yet")

async def delalert(update, context):
    await update.message.reply_text("Delete alert command - not implemented yet")

def main():
    print(f"Token loaded: {'Yes' if TELEGRAM_TOKEN else 'No (empty!)'}")
    
    if not TELEGRAM_TOKEN:
        print("ERROR: TELEGRAM_TOKEN is not set in .env file")
        return
    
    print("Starting bot...")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Register all commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("stock", stock))
    app.add_handler(CommandHandler("chart", chart))
    app.add_handler(CommandHandler("alert", alert))
    app.add_handler(CommandHandler("alerts", alerts))
    app.add_handler(CommandHandler("delalert", delalert))

    # start bot
    app.run_polling()

if __name__ == "__main__":
    main()