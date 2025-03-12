import pandas as pd
import numpy as np
import time
from dof_reality import config
from dof_reality.serial_comm import send_command

def play_csv(file_path, port, smoothing_factor):
    """
    Lit un fichier CSV et envoie les commandes interpolées au simulateur.
    """
    df = pd.read_csv(file_path)

    if not {'temps', 'pitch', 'roll'}.issubset(df.columns):
        print("❌ Le fichier CSV doit contenir les colonnes: temps, pitch, roll")
        return

    total_duration = df['temps'].iloc[-1]
    timestamps = df['temps'].values
    pitch_values = df['pitch'].values
    roll_values = df['roll'].values

    new_timestamps = np.linspace(0, total_duration, num=len(timestamps) * smoothing_factor)
    pitch_interp = np.interp(new_timestamps, timestamps, pitch_values)
    roll_interp = np.interp(new_timestamps, timestamps, roll_values)

    interval = total_duration / len(new_timestamps)

    print(f"📌 Début du mouvement - Durée totale: {total_duration}s, Intervalle: {interval:.3f}s")

    for pitch, roll in zip(pitch_interp, roll_interp):
        send_command(port, pitch, roll)
        time.sleep(interval)

    print("✅ Lecture du fichier CSV terminée.")
