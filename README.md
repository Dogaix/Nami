# Nami

Nami é uma bot para o aplicativo Project Z, desenvolvida para facilitar interações em chats utilizando Python e a biblioteca `projz`.

## Funcionalidades

- Recebe mensagens e envia respostas conforme configurado.
- Gerencia o status online/offline do bot.
- Interage com comandos específicos definidos.

## Requisitos

Para executar o Nami, certifique-se de ter instalado:

- Python 3.6 ou superior
- Biblioteca `projz`
- Pacotes adicionais conforme necessário pelo `projz`

## Instalação e Uso

1. Clone este repositório e navegue até o diretório:

    ```bash
    git clone <URL_do_seu_repositório>
    cd Nami
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Configuração:

   - Crie um arquivo `client.txt` com as credenciais necessárias para o login do cliente `projz`.
   - Configure o arquivo conforme suas necessidades antes de executar o script.

4. Execução:

    ```bash
    python nami.py
    ```

## Exemplo de Uso
```py
import asyncio
import logging
import projz
from projz import model

# Configuração básica de logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# Leitura das credenciais do arquivo
with open("client.txt", "r") as logi:
    email    = logi.readline().strip()
    password = logi.readline().strip()
    prefixo  = logi.readline().strip()

# Inicialização do cliente projz
client = projz.Client(commands_prefix="!")
logger = logging.getLogger(__name__)

# Função para lidar com mensagens recebidas
@client.on_message()
async def handle_echo(message: projz.ChatMessage):
    if message.content is not None:
        logger.info(f'Mensagem recebida: {message.content}')
        await client.send_message(message.thread_id, content=message.content)
        
    if message.content == "oi":
        client.send_message(thread_id=message.message_id, content="oooooi")

# Comando para colocar o bot offline
@client.on_command("off")
async def offff(message: projz.ChatMessage):
    print(message)
    await client.change_chat_online_status(message.thread_id, is_online=False)
    await client.send_message(message.thread_id, content=f"Estou off agora, {message.author.nickname}!")

# Comando exemplo off2
@client.on_command("off2")
async def off2(message: projz.ChatMessage):
    print(message)
    chats = await projz.Client.get_chat_messages(client,thread_id=message.thread_id,size=32)
    print(chats)
    logger.info(f'Comando off2 recebido. Thread ID: {message.thread_id}')
    await message.send_message(message.thread_id, content="oi")

# Função principal para login e execução contínua
async def main():
    await client.login_email(email, password)
    logger.info("Nami online | By Dogaix")

# Executa o loop de eventos asyncio
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
```
