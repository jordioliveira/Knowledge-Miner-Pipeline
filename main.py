import os
import sys
from config import OUTPUT_DIR
from services.youtube import download_audio
from services.transcription import transcribe_audio
from services.ai_processor import generate_insights
from utils.cleaner import clean_transcription, clean_filename
from utils.file_manager import save_text, save_markdown

def main():
    print("="*32)
    print("       KNOWLEDGE MINER          ")
    print("="*32)
    print("1 - Resumo profundo")
    print("2 - Extração de repertório")

    modo = input("Modo (1 ou 2): ").strip()
    if modo not in ["1", "2"]:
        print("Modo inválido. Encerrando.")
        sys.exit(1)

    url = input("\nURL do YouTube: ").strip()

    try:
        print("\n[1/4] Baixando áudio...")
        audio_file, titulo, autor = download_audio(url)

        print("[2/4] Transcrevendo (pode levar alguns minutos)...")
        texto_bruto = transcribe_audio(audio_file)
        texto_limpo = clean_transcription(texto_bruto)

        caminho_transcricao = os.path.join(OUTPUT_DIR, "transcricao.txt")
        save_text(caminho_transcricao, texto_limpo)

        print("[3/4] Processando via IA...")
        saida_ia = generate_insights(modo, texto_limpo)

        print("[4/4] Finalizando arquivos...")
        autor_limpo = clean_filename(autor)
        titulo_curto = clean_filename(titulo[:60])
        nome_arquivo = f"{autor_limpo} — {titulo_curto}.md"

        caminho_final = save_markdown(OUTPUT_DIR, nome_arquivo, titulo, autor, url, saida_ia)

        if os.path.exists(audio_file):
            os.remove(audio_file)

        print(f"\n✅ Concluído: {caminho_final}")

    except Exception as e:
        print(f"\n❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
