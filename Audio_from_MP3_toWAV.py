
from pydub import AudioSegment


src = "Enefit_lenktynes.mp3"
dst = "Enefit_lenktynes.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")