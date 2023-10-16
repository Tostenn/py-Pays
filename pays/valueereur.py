
class Valueint(Exception):

    '''souleve les erreur du a la mauvaise valeur'''

    def __init__(self,) -> None:
        super().__init__(f'cette argument attent un entier')