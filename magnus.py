import speech_recognition as sr
import time
import importlib
import os
import sys
# Komut dosyalarını taramak için commands klasörüne erişim sağlıyoruz
sys.path.append("./commands")
mic = sr.Microphone()
r = sr.Recognizer()
# r.pause_threshold = 0.5
# r.energy_threshold = 50
komutlar = {}
for dosya in os.listdir("commands"):
    # Dosyanın bir Python dosyası olup olmadığını kontrol edin
    if dosya.endswith(".py"):
        # Dosyayı içe aktarın
        modul = importlib.import_module(dosya[:-3])
        # Dosyadaki verileri bir sözlük içine toplayın
        komutlar.update(modul.exec)
        print("Yüklenen komut : "+dosya)


def callback(recognizer, audio):
    r.adjust_for_ambient_noise(mic)
    try:
        yazi = r.recognize_google(audio, language="tr-tr")
        yazi = yazi.lower()
        command = " ".join(yazi.split()[1:]).lower()

        if not command.split()[1:]:
            return
       

        if yazi.split()[0] in ["magnus", "magnos", "magnuz"]:
            if command in komutlar:
                komutlar[command]["exec"](command.split()[1:])
                prevcommand = command

            elif command.split()[0] in komutlar:
                komutlar[command.split()[0]]["exec"](
                    " ".join(command.split()[1:]))
                prevcommand = command
           
        else:
            try:
              for element in komutlar[prevcommand]["other"]:
                if yazi == element:
                    komutlar[prevcommand]["exec"]()
            except:
                return

    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print(" ")

    except sr.RequestError:
        print("İnternete bağlanamıyorum")


r.listen_in_background(mic, callback)
print("Hazır!")
while True:
    time.sleep(0.1)
