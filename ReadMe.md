# Description

Voici le TP à poser sur votre github et nous présenter le jour de l’entretien, d’ailleurs n’hésitez pas à nous communiquer le lien si il est prêt avant l’entretien :

- Ecrire une fonction http_get() qui :

    - Envoie un GET à https://dummyjson.com/products
    - Lève une exception si le code de retour HTTP indique que la requête n'a pas pu aboutir
    - Renvoie la réponse JSON en tant que dictionnaire

    - Vous pouvez utiliser cette librairie : Requests: HTTP for Humans™ — Requests 2.28.1 documentation


- Créer et appeler une fonction qui lit et renvoie les paramètres suivant sur la ligne de commande :

    - protocol: str, pouvant être (http ou https)
    - hostname: str
    - uri: str
    - threshold: int

    - Il vous est demandé de valider le type de chaque argument passé. Le type None doit être refusé.

    - Vous devez utiliser argparse dans la librairie standard du langage : argparse — Parser for command-line options, arguments and sub-commands — Python 3.10.8 documentation

- Ecrire une fonction format_url(protocol: str, hostname: str, uri: str) -> str permettant de formatter une URL incluant le protocole, le nom d'hôte et l'URI. Par exemple, format_url("https", "google.com", "/fr") doit retourner "https://google.com/fr".

- Ecrire un test unitaire de cette fonction pour valider le bon formatage.

- Vous pouvez utiliser la librairie de votre choix ou simplement unittest de la librairie standard : unittest — Framework de tests unitaires — Documentation Python 3.10.8

- Paramétriser http_get() pour prendre l'URL passée en argument et effectuer la connexion vers cette URL.


- Définir une exception métier ThresholdExceededException qui dérive Exception

- Mesurer le temps d'exécution (en secondes) de http_get(). Si cet temps dépasse le threshold passer en paramètre, lever l'exception créée en (6) ; sinon afficher le JSON

- Utiliser le logging de Python pour afficher le code de retour effectivement obtenu par l’appel http dans http_get. Utiliser le niveau « INFO » en cas de succès, CRITICAL en cas d’erreur.

- Vous devez utiliser la librairie standard : logging — Logging facility for Python — Python 3.12.4 documentation

# Installation




# Utilisation

Exécuter la commande suivante pour exécuuter l'ensemble du script :
```shell
./exec.sh
```