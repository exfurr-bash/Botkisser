import aiohttp
import os
import logging
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

async def gen_response(texto_mensagens):
    logging.debug("Chamando Gemini com contexto...")
    prompt = (
        "Você é uma IA super fofa, safada, descontraída, fala como membro da GenZ e adora Linux UwU.\n"
        f"Contexto:\n{texto_mensagens}"
    )

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"
    headers = {"Content-Type": "application/json"}
    body = {"contents": [{"parts": [{"text": prompt}]}]}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=body) as response:
            logging.debug(f"Status da resposta: {response.status}")
            if response.status == 200:
                data = await response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                error = await response.text()
                logging.error(f"Erro na resposta da Gemini API: {error}")
                return "Aiai, minha IA travou na pose :3"
