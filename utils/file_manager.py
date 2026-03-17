import os
from datetime import datetime

def save_text(filepath, content):
    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def save_markdown(output_dir, filename, title, author, url, content):
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    data_atual = datetime.now().strftime("%d/%m/%Y")

    conteudo_md = f"""# {title}

Autor: {author}
Link: {url}
Processado em: {data_atual}

---

{content}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    return filepath
