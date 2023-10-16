from sqlite3 import connect
from pays.selectexcption import SelectException
from pays.commandException import CommandException
from pays.valueereur import Valueint

class Pays:
    '''
    # Pays      

     permet l'obtentsion d'information sur un ou plusieur pays en tapant quelque caractere du pays\n

    synsthaxe de recherche

       `> code pays`\n
        `$ nom pays`\n
        `_ id [1-254]`\n
        `^ continent`\n
        `~ monnaie`\n
        `+ code d'appel pays`\n
        `. domaine web`\n
        `h> habitant`\n
        `h< habitant`\n
        `s> superficie`\n
        `s< superficie`\n
    
        github : 
    '''

    AVANCER = 'avancer'
    SIMPLE = 'simple'

    def __init__(self,driver = 'databese.dbs') -> None:
        self.bd = connect(driver)
        curseur = self.bd.cursor()
        self.nb_pays =self.commandfre('select id from pays order by id desc limit 1')
        self.attr = ['id','nom','code','drapeau','*']
        self.cmd =  ['$','>','_']

        # determination du driver utiliser
        self.driver = len(self.commandfre('select * from pays where id =1')[0])

        if self.driver != 4:
            self.driver = Pays.AVANCER
            self.cmd.extend(['^','~','+','.','>>h','<<h','>>s','<<s'])
            self.attr.extend([
                'continent',
                'independant',
                'long_nom',
                'capital',
                'point_culminant',
                'point_bas',
                'population',
                'superficie',
                'membre',
                'pib_h',
                'code_appel',
                'monnaie',
                'domain_web'
            ])
        
        else:self.driver = Pays.SIMPLE

        curseur.close()

    def selects(self,select:list) -> str:

        assert select.copy() , 'select is list'
        cmd = [i for i in select if not i in self.attr]

        if len(cmd) > 0:
            raise SelectException(cmd)

        return ', '.join(select)

    def commandValidator(self,command:str) -> bool:
        '''verfie si la commande est correct'''
        try:
            self.__parsecmd(command,self.__triecmd(command))

            return True
        except: return False

    def query(self,command:str,select:list=['nom']) -> list:
        '''requete `>`, `$`, `_` , `...`'''
        assert command.lower() , 'command is str'
        select = self.selects(select)

        # verifie que la commande existe 
        param = self.__triecmd(command)
        command =self.__parsecmd(parm=param,command=command)
        
        # recherche par code pays
        # par code
        if param == '>':
            command = f"select {select} from pays where code like '%{command}%';"

        # par nom
        elif param == '$':
            command = f"select {select} from pays where nom like '%{command}%';"

        # par monnaie
        elif param == '~':
            command = f"select {select} from pays where monnaie like '%{command}%';"

        # par continent
        elif param == '^':
            command = f"select {select} from pays where continent like '%{command}%';"

        # par code appel
        elif param == '+':
            command = f"select {select} from pays where code_appel = '+{command}';"

        # par domaine web
        elif param == '.':
            command = f"select {select} from pays where domain_web = '.{command}';"

        # par identifant
        elif param == '_' :
            command = f"select {select} from pays where id ={command};"

        # par habitant >
        elif param == '>>h' :
            command = f"select {select} from pays where population > {command};"

        # par habitant <
        elif param == '<<h' :
            command = f"select {select} from pays where population < {command};"

        # par superficie >
        elif param == '>>s' :
            command = f"select {select} from pays where superficie > {command};"

        # par superficie <
        elif param == '<<s' :
            command = f"select {select} from pays where superficie < {command};"

        curseur = self.bd.cursor()
        command = curseur.execute(command).fetchall()
        curseur.close()
        return self.__parserequet(command)

    def __parserequet(self,command:list) -> list:
        res = []
        for i in range(len(command)):
            data = []
           
            for j in command[i]:
                try: data.append(j.replace("||","'"))
                except:data.append(j)
            
            if len(command) == 1:return data
            if len(data) ==1:res.append(data[0])
            else:       
                res.append(data)
        return res

    def __parsecmd(self, command:str,parm:str = '',op = False) -> str:
        '''parser la commande'''
        
        if not op:command = command.replace(parm,'')

        if parm:
            if parm in ['_','>>h','<<h','>>s','<<s']:
                try: int(command.strip())
                except: raise Valueint()

        return command.replace("'",'||').strip()

    def __triecmd(self, command:str) -> str:
        '''verifie la commande interne'''
        
        if  command[:3] in self.cmd:
            return command[:3]

        if command[0] in self.cmd:return command[0]

        raise CommandException(command)

    def info(self, pays:list,select:list=['*']) -> list:
        '''
        toutes les informations du/des pays
        `pays:list` [ nom de pays, ..]
        `select:list` [ "attr"]
        '''
        assert type(pays) == type([]), 'pays is of type list'
        select = self.selects(select)

        data = []
        curseur = self.bd.cursor()
            
        for i in pays:
            i = self.__parsecmd(i,op=True)
            i = curseur.execute(f"select {select} from pays where nom like '{i}'").fetchall()
            
            if len(i) == 1:
                data.append(i[0])
        curseur.close()
        return self.__parserequet(data)

    def commandfre(self,cmd = '') -> list:
        return self.bd.execute(cmd).fetchall()
