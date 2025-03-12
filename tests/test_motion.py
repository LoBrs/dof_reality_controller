import time
import numpy as np
import config
from dof_reality.serial_comm import open_serial_connection, send_command


def generate_test_positions(duration=10, num_positions=50):
    """
    Génère des positions interpolées sur une durée définie.
    :param duration: Durée totale du test en secondes.
    :param num_positions: Nombre total de positions à tester.
    :return: Listes des valeurs interpolées pour pitch et roll.
    """
    # Temps simulé
    timestamps = np.linspace(0, duration, num=num_positions)

    # Génération de valeurs de test en degrés (ex: oscillation entre -10° et +10°)
    pitch_values = 10 * np.sin(np.linspace(0, 2 * np.pi, num=num_positions))  # Mouvement sinusoidal
    roll_values = 10 * np.cos(np.linspace(0, 2 * np.pi, num=num_positions))  # Mouvement sinusoidal déphasé

    return timestamps, pitch_values, roll_values


def test_motion():
    """ Teste l'envoi de commandes au simulateur sans passer par un fichier CSV. """
    port = open_serial_connection(config.PORT_NAME, config.BAUD_RATE)
    if not port:
        print("❌ Impossible d'ouvrir le port série.")
        return

    print(f"📌 Démarrage du test de mouvement pour {config.PORT_NAME}...")

    # Générer les positions de test
    duration = 10  # Durée totale en secondes
    num_positions = 50  # Nombre total de positions
    timestamps, pitch_values, roll_values = generate_test_positions(duration, num_positions)

    # Appliquer SMOOTHING_FACTOR
    new_timestamps = np.linspace(0, duration, num=num_positions * config.SMOOTHING_FACTOR)
    pitch_interp = np.interp(new_timestamps, timestamps, pitch_values)
    roll_interp = np.interp(new_timestamps, timestamps, roll_values)

    interval = duration / len(new_timestamps)  # Calcul de l'intervalle entre chaque commande

    print(f"✅ Test en cours : {len(new_timestamps)} positions générées (Intervalle: {interval:.3f}s)")

    # Envoi des commandes interpolées au simulateur
    for pitch, roll in zip(pitch_interp, roll_interp):
        send_command(port, pitch, roll)
        time.sleep(interval)

    print("✅ Test terminé.")
    port.close()


if __name__ == "__main__":
    test_motion()
