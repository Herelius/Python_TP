# Description

Petit exercice sur l'utilisation des modules `requests` et `unittest` de Python.

# Installation des dépendances

```shell
pip install -r requirements.txt
```

# Utilisation

1. Modifier les variables `PYTHON_EXEC`, `PROTOCOL`, `HOSTNAME`, `URI` et `THRESHOLD` se trouvant au début du fichier [exec.sh](exec.sh) (ou [exec.bat](exec.bat)) par l'exécuteur python local.

**Windows :**

Fichier [exec.bat](exec.bat) :

```shell
set PYTHON_EXEC=python
set PROTOCOL=http
set HOSTNAME=google.com
set URI=/fr
set THRESHOLD=10
```

**Linux :**

Fichier [exec.sh](exec.sh) :

```shell
PYTHON_EXEC=python
PROTOCOL=http
HOSTNAME=google.com
URI=/fr
THRESHOLD=10
```

Exécuter la commande suivante pour exécuuter l'ensemble du script :

1. Sous Linux :

```shell
source exec.sh
```

2. Sous Windows :

```shell
.\exec.bat
```
