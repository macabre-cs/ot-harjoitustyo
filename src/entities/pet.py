class Pet:
    """Luokka, joka kuvaa yksittäistä virtuaalilemmikkiä.

    Attributes:
        name (str): Virtuaalilemmikin nimi.
        password (str): Virtuaalilemmikin salasana.    
    """
    def __init__(self, name, password):
        """Pet-luokan konstruktori, jossa luodaan uusi virtuaalilemmikki.

        Args:
            name (str): Virtuaalilemmikin nimi.
            password (str): Virtuaalilemmikin salasana.
        """
        self.name = name
        self.password = password
