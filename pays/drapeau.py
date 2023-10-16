
from requests import get
from os import getcwdb
from os.path import join

from pays.pays import Pays

class Drapeau:
    '''télécharger les drapeaux des différents pays'''
    def __init__(self, pays:Pays,path = '') -> None:
        self.pays = pays
        self.path = str(getcwdb())[2:-1]+ path
        print(path)


    def download(self,name:list):
        assert type(name) == type([]), 'name is of type list'
        chemin = {}

        
        pays = self.pays.info(name,['nom','drapeau'])
        
        if len(pays) == 2:pays = [pays]
        
        for i in pays:
            nomPays = i[0]
            drapeau = i[1]
            
            with open(nomPays+'.png','wb') as file:
                img = get(drapeau).content
                file.write(img)
        
            chemin[nomPays] = join(self.path,nomPays+'.png')
        
        return chemin
