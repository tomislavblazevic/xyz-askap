import numpy as np
import pandas as pd
from scipy.io.wavfile import write

# Učitaj podatke iz CSV-a
df = pd.read_csv("C:\Users\Tomislav\Desktop\xyz\askap_from_csv.py")  # <- zamijeni naziv po potrebi


# Parametri
sample_rate = 44100
pulse_duration = 0.05  # sekundi

# Priprema praznog audio signala
total_duration = df["time_sec"].max() + 1
total_samples = int(total_duration * sample_rate)
signal = np.zeros(total_samples)

# Sonifikacija: svaki redak = impuls s jačinom
for _, row in df.iterrows():
    t = row["time_sec"]
    intensity = row["intensity"]
    
    if intensity > 0:
        freq = 300 + intensity * 1000  # frekvencija varira s intenzitetom
        start = int(t * sample_rate)
        end = int(start + pulse_duration * sample_rate)
        
        if end < total_samples:
            tone_t = np.linspace(0, pulse_duration, end - start, False)
            tone = intensity * np.sin(2 * np.pi * freq * tone_t)
            signal[start:end] += tone

# Skaliranje i spremanje
signal = np.int16(signal / np.max(np.abs(signal)) * 32767)
write("askap_realdata_sonification.wav", sample_rate, signal)

print("Gotovo: zvuk iz stvarnih podataka je spreman.")

print










