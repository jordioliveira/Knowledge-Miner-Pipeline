import re

def clean_transcription(texto):
    texto_limpo = re.sub(r'\n+', ' ', texto)
    texto_limpo = re.sub(r'\[.*?\]', '', texto_limpo)
    return texto_limpo.strip()

def clean_filename(nome):
    nome_limpo = re.sub(r'[\\/*?:"<>|]', "", nome)
    return nome_limpo.strip()
