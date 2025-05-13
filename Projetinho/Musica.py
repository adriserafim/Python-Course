from pydub.generators import Sine
from pydub import AudioSegment

# Criando instrumentos simulados com ondas senoidais
piano = Sine(440).to_audio_segment(duration=1000).fade_in(200).fade_out(200)  # A4
harp = Sine(660).to_audio_segment(duration=500).fade_in(100).fade_out(100)   # E5
strings = Sine(220).to_audio_segment(duration=1000).fade_in(300).fade_out(300)  # A3

# Combinando em um loop de 1 minuto
loop = AudioSegment.silent(duration=0)
for _ in range(30):  # 30 * 2 segundos = 60s
    bar = piano.overlay(strings)
    if _ % 2 == 0:
        bar = bar.overlay(harp)
    loop += bar

# Exportando o áudio
loop.export("final_fantasy_trilha_loop.mp3", format="mp3")
print("Arquivo gerado: final_fantasy_trilha_loop.mp3")