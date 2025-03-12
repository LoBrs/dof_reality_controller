# Configuration du port série
PORT_NAME = "COM5"  # Modifie selon ton setup
BAUD_RATE = 115200

# Fichier CSV contenant les mouvements
CSV_FILE = "data.csv"

# Niveau de fluidité (plus grand = plus fluide)
SMOOTHING_FACTOR = 5

# Plage des degrés du simulateur (ex: -16° à +16°)
MAX_DEGREES = 16  # Degré max du simulateur

# Facteur multiplicateur pour augmenter l'effet des mouvements (ex: simuler des G)
MULTIPLIER_FACTOR = 1.5  # Augmente artificiellement l'amplitude
