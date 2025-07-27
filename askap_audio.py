import numpy as np
from scipy.io.wavfile import write

# Parametri signala
duration_sec = 10              # Trajanje audio datoteke
sample_rate = 44100            # Učestalost uzorkovanja
pulse_interval_sec = 1         # Impuls svakih 1 sekundu
pulse_duration_sec = 0.05      # Trajanje impulsa
freq = 440                     # Frekvencija impulsa (Hz)

# Inicijalizacija audio signala s nulama (tišina)
samples = np.zeros(duration_sec * sample_rate)

# Impulsi: svaki 1 sekundu
for i in range(0, duration_sec):
    start = int(i * sample_rate)
    end = int(start + pulse_duration_sec * sample_rate)
    if end < len(samples):
        t = np.linspace(0, pulse_duration_sec, end - start, False)
        tone = 0.5 * np.sin(2 * np.pi * freq * t)
        samples[start:end] = tone

# Skaliraj na 16-bitni integer raspon
samples_int16 = np.int16(samples * 32767)

# Spremi .wav datoteku
write("askap_j1832_simulacija.wav", sample_rate, samples_int16)

print("Završeno: datoteka 'askap_j1832_simulacija.wav' je generirana.")
