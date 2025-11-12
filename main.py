import asyncio
from alert import check_prev_and_curr_price_change
from telegram_bot import send_message
from discord_bot import discord_send_message_webhook
async def main():
    await send_message('Starting crypto price alert script...')
    await discord_send_message_webhook('Starting crypto price alert script...') 
    endpoint = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/spotlight?rankRange=100&timeframe=1h&dataType=2&limit=5"
    await check_prev_and_curr_price_change(endpoint)


if __name__ == "__main__":
    asyncio.run(main())
