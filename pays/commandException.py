

class CommandException(Exception):
    '''souleve les erreur du a la mauvaise commande'''

    def __init__(self, args: str) -> None:
        super().__init__(f'{args} ne fais pas partir des commandes')