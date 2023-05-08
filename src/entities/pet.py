class Pet:
    """Luokka, joka kuvaa yksittäistä virtuaalilemmikkiä.

    Attributes:
        name (str): Virtuaalilemmikin nimi.
        password (str): Virtuaalilemmikin salasana.    
    """

    def __init__(self, name, password, progress=None, image=None):
        """Pet-luokan konstruktori, jossa luodaan uusi virtuaalilemmikki.

        Args:
            name (str): Virtuaalilemmikin nimi.
            password (str): Virtuaalilemmikin salasana.
            progress (int): Lemmikin rakkausmittarin arvo.
            pet_img (str): Lemmikin kuvan nimi.
        """
        self.name = name
        self.password = password
        self.progress = progress if progress is not None else 0
        self.image = image if image is not None else ""
