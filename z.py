import json
import asyncio
import logging
import projz
from projz import model

# Configuração básica de logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s', level=logging.DEBUG)

# Carrega as credenciais do arquivo config.json
with open("config.json", "r") as login:
    data     = json.load(login)
    email    = data['email']
    password = data['senha']
    prefixo  = data['prefixo']

# Inicialização do cliente projz
client = projz.Client(commands_prefix=prefixo)
logger = logging.getLogger(__name__)

# Função para lidar com mensagens recebidas
@client.on_message()
async def handle_echo(message: projz.ChatMessage):
    if message.content is not None:
        logger.info(f'Mensagem recebida: {message.content}')
        await client.send_message(message.thread_id, content=message.content)
        
    if message.content == "oi":
        await client.send_message(thread_id=message.message_id, content="oooooi")  # Corrigido para usar await

# Comando para colocar o bot offline
@client.on_command("off")
async def offff(message: projz.ChatMessage):
    logger.info(f'Recebido comando off da thread {message.thread_id}')
    await client.change_chat_online_status(message.thread_id, is_online=False)
    await client.send_message(message.thread_id, content=f"Estou off agora, {message.author.nickname}!")

# Exemplo de comando off2
@client.on_command("off2")
async def off2(message: projz.ChatMessage):
    logger.info(f'Recebido comando off2 da thread {message.thread_id}')
    chats = await projz.Client.get_chat_messages(client, thread_id=message.thread_id, size=32)
    print(chats)
    await message.send_message(message.thread_id, content="oi")

# Função principal para login e execução contínua
async def main():
    await client.login_email(email, password)
    logger.info("Nami online | By Dogaix")

# Execução do loop de eventos asyncio
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
