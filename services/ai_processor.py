import os
from openai import OpenAI
from config import API_KEY, PROMPTS_DIR

client = OpenAI(api_key=API_KEY)

def get_prompt(modo, texto):
    filename = "summary.txt" if modo == "1" else "knowledge.txt"
    filepath = os.path.join(PROMPTS_DIR, filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo de prompt não encontrado: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        template = f.read()

    return template.format(texto=texto)

def generate_insights(modo, texto_limpo):
    prompt = get_prompt(modo, texto_limpo)

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return resposta.choices[0].message.content
