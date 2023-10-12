import speech_recognition as sr
import webbrowser
import os
import re
from gtts import gTTS
import playsound
import psutil

def ouvir_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower().strip()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"Erro na requisição ao Google: {e}")
        return ""

def extrair_palavras_chave(comando):
    palavras_chave = ["google", "youtube", "vs code", "fechar", "discord","whatsapp","sword art online","postman","sair google"]

    regex = r'\b(?:' + '|'.join(re.escape(word) for word in palavras_chave) + r')\b'

    palavras_encontradas = re.findall(regex, comando.lower())

    return palavras_encontradas

def executar_comando(comando):
    palavras_chave = extrair_palavras_chave(comando)

    for palavra in palavras_chave:
        if palavra == "google":
            fala("Ok, abrindo o Google.")
            webbrowser.open("https://www.google.com/")
        elif palavra == "youtube":
            fala("Ok, abrindo o YouTube.")
            webbrowser.open("https://www.youtube.com/")
        elif palavra == "discord":
            fala("Ok, abrindo o Discord.")
            webbrowser.open("https://discord.com/")
        elif palavra == "vs code":
            fala("Ok, abrindo o Visual Studio Code.")
            os.system("code")
        elif palavra == "sword art online":
            fala("Ok, abrindo o jogo sword art online")
            os.system("\"D:/Program Files (x86)/Steam/steamapps/common/SAOHR/sao_hr.exe\"")
        elif palavra == "postman":
            fala("Ok, abrindo o postman")
            os.system("\"C:/Users/thiag/AppData/Local/Postman/Postman.exe\"")
        elif palavra == "fechar":
            fala("Ok, encerrando o programa.")
            exit()
        elif "sair google" in comando.lower():
            for proc in psutil.process_iter(attrs=['pid', 'name']):
                proc.kill()

    if not palavras_chave:
        fala("Comando não reconhecido.")

def fala(texto):
    tts = gTTS(texto, lang='pt')
    tts.save("fala.mp3")
    playsound.playsound("fala.mp3")
    os.remove("fala.mp3")

fala("Olá, Thiago! O que você deseja?")
while True:
    comando = ouvir_comando()
    executar_comando(comando)
