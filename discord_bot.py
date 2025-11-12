import httpx
import asyncio
from config import webhook_url

async def discord_send_message_webhook(message):
    async with httpx.AsyncClient() as client:
        data = {"content": message}
        response = await client.post(webhook_url, json=data)
        print(response.status_code)
        if response.status_code == 204:
            print("Message sent successfully")
        else:
            print("Failed to send message")

async def main():
    await discord_send_message_webhook("Hello from bot using webhook!")

asyncio.run(main())
