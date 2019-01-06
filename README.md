# Outil de conversion Markdown vers HTML

Cette outil est à l'origne un projet de classe proposé par Vincent Poulailleau, professeur de python. En résumé, l'objectif etait de creer un outil open source ou non, capable de convertir des fichier markdowns de notre choix vers des fichier HTML, avec la possibilité de fusioner ces derniers dans un template présélectionnés.
La version complète de l'énoncé est disponible sur son GitHub :

* https://github.com/vpoulailleau/site_statique

Ce fichier est déstiné à expliquer l'utilisation du programme.

## Les Arguments

Trois arguments sont disponibles pour ce programmes, sans compter l'aide :

* -i ou --input-directory
  * renseigne le dossier dans lequel se trouvera les fichier markdowns à convertir.
* -o ou --output-directory
  * renseigne le dossier de sortie dans lequels seront créer les différents fichiers.
* -t ou --template-directory
  * renseigne le fichier à modifier afin d'y inclure votre code HTML.
* -h ou --help
  * Affiche l'aide.

### Template

L'argument -t devra mener vers un fichier *.html. Ce fichier devra contenir une ligne sur laquelle sa leur inscription sera  `[REPLACE_ME]`. C'est donc à cet endroit que le code markdown sera transcrit puis copié.

### Précautions

Le fichier d'entré peut contenir tous types de dossier ou de fichier, seul les fichier *.md seront séléctionnés et leur noms seront conservé pour la création du fichier html. En revanche, le fichier de sortie devra être de préférence vide, ou des fichier pourraient être écrasés.
Concernant le fichier template, il vous sera demandé si vous souhaitez conserver tous les fichier et dossier voisins dans le répertoire de sortie, dans ce cas, un dossier `/TEMPLATE` sera créé dans le répertoire de sortie et vous y retrouverez tous vos fichier convertis.
Notez que si les dossier d'entré et de sortie sont obligatoire, il n'en est pas de même pour le template. Dans le cas ou ce dernier n'est pas renseigné, les fichiers seront seulement convertis dans le dossier de sortie.

## Exemple

J'ai joins à ce dossier dossier `/EXEMPLE` contenant des fichier, pour rester cohérent, considérez cela :
```
$ ls -l
Mark2Html.py
input/
output/
template/
```
On lance alors la commande :
```
$ python3.6 Mark2Html.py -i input/ -o output/ -t template/index.html
template/index.html template selected
output output directory already exist
Do you want to copy template files in ouput directory ? (y/n) y
DONE
```
Il est donc tout à fait possible de ne pas fusionner tous les fichier du template. Répondre `n` aura eu pour effet d'arreter le programme après la conversion et la fusion des fichiers.
Notez également que tous les fichiers sont conservés, aussi bien le fichier brute convertis, que le fichier template convertis.

## Bugs à corriger

* Verifier scrupuleusement l'existance des fichier renseignés
* Verifier si les extension correspondent à ce qui est attendu
* Erreur lorsque les fichiers .html à convertir existent déjà
* Problème de reconnaissance des URLs 
