# DOF Reality Controller

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python -m dof_reality.main
```

Le fichier CSV doit contenir les colonnes suivantes :
```
temps,pitch,roll
0,0,0
0.2,10,5
0.4,-10,-5
0.6,5,-10
0.8,-5,10
1.0,0,0
```

## Configuration (`config.py`)
```python
PORT_NAME = "COM5"  # Port série du simulateur
BAUD_RATE = 115200   # Vitesse de communication
CSV_FILE = "data.csv"  # Fichier de mouvements
SMOOTHING_FACTOR = 5  # Fluidité des mouvements
MAX_DEGREES = 16  # Plage max en degrés
MULTIPLIER_FACTOR = 1.5  # Intensité des mouvements (ex: simulation de G)
```

## 🛠 Développement
### **Lancer les tests unitaires**
```bash
python -m unittest discover tests
```

Pour un test de **10 secondes** avec **50 positions générées automatiquement** :
```bash
python tests/test_motion.py
```

### **Installation en package (optionnel)**
Si vous souhaitez installer le projet en package :
```bash
pip install -e .
```
Puis, exécuter directement :
```bash
dof-reality
```
