# Käyttöohje

## Sovelluksen käynnistäminen

Asenna ensin sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

Sen jälkeen alusta sovelluksen tietokanta komennolla:

```bash
poetry run invoke build
```

Nyt voit käynnistää sovelluksen komennolla:

```bash
poetry run invoke start
```

## Aloitus

Valitse haluatko luoda uuden virtuaalilemmikin vai kirjautua sisään jo olemassa olevan virtuaalilemmikin tiedoilla.

## Virtuaalilemmikin luominen

- Paina aloitusnäkymässä nappia `I dont't have a pet yet`.
- Syötä kenttiin lemmikin nimi ja salasana ja paina `Adopt your new little friend!` nappia.

## Sisään kirjautuminen

- Paina aloitusnäkymässä nappia `I already have a pet`.
- Syötä kenttiin lemmikin nimi ja salasana ja paina `Log in with your pet!` nappia.

## Pelin pelaaminen
- Paina `Love` nappia jos haluat antaa rakkautta lemmikillesi.
- Paina `Feed` nappia jos haluat ruokkia lemmikkiäsi.
- Paina `Hurt :(` nappia jos haluat satuttaa lemmikkiäsi.
- Paina `Close game` nappia jos haluat lopettaa pelin.
