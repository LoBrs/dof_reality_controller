import serial
import config

def clamp_value(value, min_val, max_val):
    """ Limite une valeur entre min_val et max_val """
    return max(min(value, max_val), min_val)

def degrees_to_value(degrees):
    """
    Convertit une valeur en degrés en valeur utilisable par le simulateur (0-1024).
    Applique le facteur multiplicateur avant conversion.
    """
    adjusted_degrees = degrees * config.MULTIPLIER_FACTOR
    clamped_degrees = clamp_value(adjusted_degrees, -config.MAX_DEGREES, config.MAX_DEGREES)

    # Conversion en plage de 0 à 1024 (512 = neutre)
    return int(512 + (clamped_degrees / config.MAX_DEGREES) * 512)

def send_command(port, pitch, roll):
    """ Envoie une commande fluide au simulateur DOF Reality PM2 """
    left_actuator = degrees_to_value(pitch + roll)
    right_actuator = degrees_to_value(pitch - roll)

    left_high, left_low = divmod(left_actuator, 256)
    right_high, right_low = divmod(right_actuator, 256)

    command = bytes([
        0x5B, 0x41, left_high, left_low, 0x5D,  # Vérin gauche
        0x5B, 0x42, right_high, right_low, 0x5D # Vérin droit
    ])

    port.write(command)
    print(f"Envoyé: {command.hex()} (Pitch={pitch:.1f}°, Roll={roll:.1f}°, Left={left_actuator}, Right={right_actuator})")

def open_serial_connection(port_name, baud_rate):
    """ Ouvre la connexion série """
    try:
        return serial.Serial(port_name, baud_rate, timeout=1)
    except serial.SerialException as e:
        print(f"Erreur de connexion au port série: {e}")
        return None
