import random
import logging
from utils import meowify, alterar_karma
from ai import gen_response

async def handle_command(client, message):
    content = message.content.lower()
    author = f"{message.author} ({message.author.id})"
    logging.info(f"Comando de {author}: {message.content}")

    try:
        if content.startswith('$hello'):
            await message.channel.send('Hello bb :3')
        elif content.startswith('$meowify'):
            await message.channel.send(meowify(message.content[9:]))
        elif content.startswith('$karma') and message.mentions:
            new_karma = alterar_karma(message.mentions[0].id, 1)
            await message.channel.send(f"<@{message.mentions[0].id}> agora tem {new_karma} karmas UwU")
        elif content.startswith('/reset_ai'):
            await message.channel.send("Ai caralho, minhas memórias foram pro lixo… quem sou eu?")
        else:
            should_respond = (
                content.startswith('$test') or
                "boykisser uwu" in content or
                client.user.mentioned_in(message) or
                random.randint(0, 20) == 0
            )
            if should_respond:
                messages = [msg async for msg in message.channel.history(limit=25)]
                messages.reverse()

                last_reset_index = -1
                for i, msg in enumerate(messages):
                    if "/reset_ai" in msg.content.lower():
                        last_reset_index = i

                if last_reset_index != -1:
                    messages = messages[last_reset_index + 1:]

                context = "\n".join(
                    f"{msg.author} (Id:{msg.author.id}): {msg.content}"
                    for msg in messages
                )

                logging.debug("Contexto construído para IA:")
                logging.debug(context)

                resposta = await gen_response(context)
                partes = [resposta[i:i+1999] for i in range(0, len(resposta), 1999)]
                for parte in partes:
                    await message.channel.send(parte)
    except Exception as e:
        logging.exception("Erro processando comando safado:")
        await message.channel.send("Ai deu pau no meu código... me reinicia com carinho UwU")
