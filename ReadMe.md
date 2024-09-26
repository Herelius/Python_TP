# Description

Petit exercice sur l'utilisation des modules `requests` et `unittest` de Python.

# Installation des

```shell
pip install -r requirements.txt
```

# Utilisation

1. Modifier les variables `PYTHON_EXEC`, `PROTOCOL`, `HOSTNAME`, `URI` et `THRESHOLD` se trouvant au début du fichier [exec.sh](exec.sh) par l'exécuteur python local.

**Windows :**

```shell
set PYTHON_EXEC=python
set PROTOCOL=http
set HOSTNAME=google.com
set URI=/fr
set THRESHOLD=10
```

**Linux :**

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
