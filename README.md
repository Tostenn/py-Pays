# py-pays
**py-Pays** est un programme écrit en python, qui permet d'effectuer des traitements sur les informations relatives au pays

# <b style='text-transform:capitalize'>à</b> utiliser pour

+ ## rechercher un pays par
    + son nom
    + son code
    + Code d'appel
    + id selon l'ordre alphabétique du pays [1 - 254]
    + Monnaie
    + Continent	

- ## connaitre les information relatifs a un pays comme
    + nombre d'habitant
    + superficie
    + drapeau
    + code pays
    + Point culminant
    + PIB par habitant
    + Monnaie
    + Continent	
    + Capitale 
    + . . . .

# Installation
tres simple à installer exercuter cette et la magie opére seule 
```
pip install py-pays
```
> `important` <br>
aprés l'installation du **package**, vous devez télécharger **base de données** [ici](https://github.com/Tostenn/py-Pays/tree/main/Driver) et la mettre dans le **repertoire courant** de votre projet, cette **base de données** est un **driver** du **package**<br>

## **Driver**
il existe deux **Driver** pour le **package**  
+ driver simple
    > qui contient trois (3) attribute de recherche qui sont `id` identifiant, `nom` nom du pays, `code` code du pays, à télecharger [ici](https://github.com/Tostenn/py-Pays/raw/main/Driver/drive.dbs)

+ driver avancer
    > qui contient trois (9) attribute de recherche qui sont `id` identifiant, `nom` nom du pays avec des fonctions avancer, `code` code du pays, `continant` contiant du pays, `monnaie` monnaie du pays, `code d'appel` du pays, `domaine` domaine web, `habitant` habitant, `superficie` superficie  
     à télécharger [ici](https://github.com/Tostenn/py-Pays/raw/main/Driver/drivers.dbs)

## Utilisation rapide
```
from pays import pays as p

# nouvelle instance de pays
pays = p.Pays(driver="driver")

# faire une requête pour récupérer le pays Côte d'ivoire
civ = pays.query('> civ')

# récupérer toutes les informations concernant ce pays
print(pays.info(civ))
```


# Syntaxe 
il y a une synthaxe a utiliser pour béneficier plein du potentiel des algorithmes
<br>par exemple, si vous voulez

### rechercher à partir du nom du pays
pour cela, vous devez indiquer `$` suivi de l'élémenemnt à rechercher<br>
Exemple : `pays.query('$ ran')` renvoir tout les pays qui ont `ran` dans leur nom

### rechercher à partir du code du pays
pour cela, vous devez indiquer `>` suivi de l'élément à rechercher<br>
Exemple : `pays.query('> an')` renvoir tout les pays qui ont `an` dans leur code pays

### rechercher à partir de l'endentifant
pour cela, vous devez indiquer `_` suivi du numéro à rechercher<br>
Exemple : `pays.query('_ 53')` renvoir le pays qui correspondant à l'identifiant 
> remarque : comme vous le savez il n'y a que 254 pays, par consequent indiquer un nombre qui n'ai pas dans cette intervalle [1 - 254 ] ne renverrait rien

## Avec le driver avancé

### rechercher à partir du continent
pour cela, vous devez indiquer `^` suivi de l'élément à rechercher<br>
Exemple : `pays.query('^ fr')` renvoir tout les pays qui sont sur un continent dont il `fr` dans le nom

### rechercher à partir de la monnaie
pour cela, vous devez indiquer `~` suivi de l'élément à rechercher<br>
Exemple : `pays.query('~ an')` renvoir tout les pays qui utilisent la monnaie dont il `an` dans le nom

### rechercher à partir du code d'appel
pour cela, vous devez indiquer `+` suivi du numéro à rechercher<br>
Exemple : `pays.query('+ 22')` renvoir le pays dont le code d'appel correspond `22` dans le nom

### rechercher à partir du domaine web
pour cela, vous devez indiquer `.` suivi du numéro à rechercher<br>
Exemple : `pays.query('+ ci')` renvoir le pays dont le domaine web correspond `ci` dans le nom

### rechercher à partir du nombre d'habitants
pour cela, vous devez indiquer `>>h` ou `<<h` suivi du numéro à rechercher<br>
Exemple : `pays.query('>>h 50000')` renvoir tout les pays dont le nombre d'habitants est supérieur a `50000` et `<<h` faire l'action inverse

### rechercher à partir de la superfice 
pour cela, vous devez indiquer `>>s` ou `<<s` suivi du numéro à rechercher<br>
Exemple : `pays.query('>>s 50000')` renvoir tout les pays dont la superficie est supérieur à `50000` et `<<s` faire l'action inverse

     
## Fonction 

`pays.info()` prend comme argument une liste de noms de pays et renvoir toutes les informations le concernant ex `pays.info(['France'])`

`pays.commandValidator()` prend comme argument une chaîne qui correspond la votre command. Renvoir true si la commande est bien formulée ex `pays.commandValidator('_ 53')`

`pays.query()` prend comme argument une chaîne qui correspond à votre commande et une liste qui corespond au attribut de selection
. Renvoir une liste selon la selection faite. ex `pays.query('_ 53',['nom','id'])`
```
# pour vérifier quel Driver vous utilisé
print(pays.driver)

# pour voir tous les attributs de selection disponible
print(pays.attr)

# pour voir toutes les commandes disponibles
print(pays.cmd) 
```

`pays.commandfree()` prend comme argument une chaîne qui correspond à votre commande, mais cette fonction ne filtre pas la commande avec la syntaxe précédent donc vous pouvez utiliser les requêtes **`SQL`**, comme les ajouts, suppressions ou mise à jours, cette fonction est pour les professionnels en **`SQL`**, mais ne vous en faite pas si vous endommager votre **`Driver`** vous pouriez toujours le re-télécharger ex `pays.commandfree('select * from pays where id > 200')` cette requête nous renvoir les 54 derniers pays

# **Drapeau**

comment parler de pays sans evoqué leur couleur. J'ai pensais a vous et la **`class Drapeau: `** vous permet comme par magie de télécharger les drapeaux des différents **`pays`**

```
from pyPays.pays import Pays
from pyPays.drapeau import Drapeau

pays = Pays(driver='databases.dbs')
dr = Drapeau(pays,path='drapeau/')
res = dr.download(res)
print(res)
```

aprés initialisation de la class vous utilisez, la fonction `download` pour télécharger le drapeau la fonction renvoir un dictionnaire `{ nom pays : chemin du drapeau }`


merci pour votre lecture pour vous remercier et consolider vos acquis, un petit script de mise en forme de vos connaissance des commandes présenter

```
from pays.pays import Pays
from pays.drapeau import Drapeau


# nouvelle instance de pays
pays = Pays('drivers.dbs')

#coloer style
vt = '\x1b[32m'
bl = '\x1b[37m'
jn = '\x1b[33m'
rg = '\x1b[30m'
b = f'\x1b[38;5;{123}m'

dr = Drapeau(pays)

# faire une requête pour récupérer le pays Côte d'ivoire
status = lambda st = 'corret' : f'{f"commande {st}":-^60}'

print(f"driver : {pays.driver}")
while True:
    cmd = input(bl+'requete pays : '+jn)
    if cmd == 'end':break
        
    if pays.commandValidator(cmd):
        print(vt+status()+bl)
        res = pays.query(cmd,['nom'])
        print(f'{b}{res}')
        
        cmd = input('télécharger le(s) drapeau(x) o/n : ')
        if cmd == 'o':
            res = dr.download(res)
            print(f'{b}{res}')

    else : print(rg+status('incorrect')+bl)
```