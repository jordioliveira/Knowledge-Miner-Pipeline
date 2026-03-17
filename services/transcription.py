import whisper

def transcribe_audio(audio_file, model_size="small"):
    modelo = whisper.load_model(model_size)
    resultado = modelo.transcribe(audio_file, language="pt")
    return resultado["text"]
