
class SelectException(Exception):
    '''souleve les erreur du a la mauvaise synthaxe du select'''

    def __init__(self, args: list) -> None:
        super().__init__(f'{", ".join(args)} ne fais pats partir des attr de selection')