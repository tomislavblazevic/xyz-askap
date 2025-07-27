import pandas as pd
import numpy as np

# Generiramo 20 sekundi simuliranih realističnih podataka
np.random.seed(42)
times = np.arange(0, 20, 1)  # 0 do 19 sekundi, 1s interval
intensities = np.abs(np.sin(times / 2) + np.random.normal(0, 0.2, len(times)))  # sinusoidno + šum
intensities = np.clip(intensities, 0, 1)  # normaliziraj u raspon 0–1

df = pd.DataFrame({
    "time_sec": times,
    "intensity": intensities
})

# Spremi datoteku
    


print("Završeno: datoteka 'askap_realdata.csv' je generirana.")
print
df.to_csv("askap_realdata.csv", index=False)


# Učitaj podatke iz CSV-a
df =pd.read_csv("c:\\Users\\Tomislav\\Desktop\\xyz\\askap_realdata.csv")# Parametri
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

from scipy.io.wavfile import write
import numpy as np  

write("c:\\Users\\Tomislav\\Desktop\\xyz\\askap_j1832_realdata.wav", sample_rate, signal),



print("Gotovo: zvuk iz stvarnih podataka je spreman.")
