import numpy as np
from scipy.io.wavfile import write

# Postavke
duration_sec = 10
sample_rate = 44100

# Impulsni parametri
pulse_duration = 0.05  # trajanje impulsa u sekundama

# Kanal 1: radio signal (npr. 440 Hz, svakih 1 s)
radio_freq = 440
radio_interval = 1

# Kanal 2: X-ray signal (npr. 880 Hz, svakih 2 s)
xray_freq = 880
xray_interval = 2

# Kreiraj prazne kanale
samples_total = duration_sec * sample_rate
channel_radio = np.zeros(samples_total)
channel_xray = np.zeros(samples_total)

# Funkcija za umetanje pulsa u kanal
def insert_pulse(channel, freq, interval):
    for i in range(0, duration_sec, interval):
        start = int(i * sample_rate)
        end = int(start + pulse_duration * sample_rate)
        if end <= samples_total:
            t = np.linspace(0, pulse_duration, end - start, False)
            tone = 0.5 * np.sin(2 * np.pi * freq * t)
            channel[start:end] += tone

# Umetni impulse u svaki kanal
insert_pulse(channel_radio, radio_freq, radio_interval)
insert_pulse(channel_xray, xray_freq, xray_interval)

# Kombiniraj u stereo (2D niz)
stereo_signal = np.stack((channel_radio, channel_xray), axis=-1)

# Skaliraj u 16-bitni format
stereo_signal = np.int16(stereo_signal / np.max(np.abs(stereo_signal)) * 32767)

# Spremi datoteku
write("askap_j1832_multichannel.wav", sample_rate, stereo_signal)

print("Završeno: datoteka 'askap_j1832_multichannel.wav' s dvokanalnom simulacijom je spremna.")
print

