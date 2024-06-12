import aiohttp
import asyncio
import logging
import projz
from projz import model

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

with open("client.txt", "r") as logi:
    email    = logi.readline().strip()
    password = logi.readline().strip()
    prefixo  = logi.readline().strip()

client = projz.Client(commands_prefix="!")
logger = logging.getLogger(__name__)

@client.on_message()
async def handle_echo(message: projz.ChatMessage):
    if message.content is not None:
        logger.info(f'Mensagem recebida: {message.content}')
        await client.send_message(message.thread_id, content=message.content)
        
    if message.content == "oi":
        client.send_message(thread_id=message.message_id, content="oooooi")

@client.on_command("off")
async def offff(message: projz.ChatMessage):
    print(message)
    await client.change_chat_online_status(message.thread_id, is_online=False)
    await client.send_message(message.thread_id, content=f"Estou off agora, {message.author.nickname}!")

@client.on_command("off2")
async def off2(message: projz.ChatMessage):
    print(message)
    chats = await projz.Client.get_chat_messages(client,thread_id=message.thread_id,size=32)
    print(chats)
    logger.info(f'Comando off2 recebido. Thread ID: {message.thread_id}')
    await message.send_message(message.thread_id, content="oi")

async def main():
    await client.login_email(email, password)
    logger.info("Nami online | By Dogaix")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
