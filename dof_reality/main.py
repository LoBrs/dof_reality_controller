import config
from .serial_comm import open_serial_connection
from .motion_processor import play_csv


def main():
    """ Point d'entrée du programme """
    print(f"🔧 Chargement de la configuration : {config.PORT_NAME}, Baud: {config.BAUD_RATE}")

    port = open_serial_connection(config.PORT_NAME, config.BAUD_RATE)
    if port:
        play_csv(config.CSV_FILE, port, config.SMOOTHING_FACTOR)
        port.close()


if __name__ == "__main__":
    main()
