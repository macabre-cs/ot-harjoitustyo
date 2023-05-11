# Käyttöohje

Lataa sovelluksen viimeisin [release](https://github.com/macabre-cs/ot-harjoitustyo/releases).

## Konfiguraatio

Sovelluksen tietojen tallennukseen käytettävää tietokantaa voi muuttaa. Voit halutessasi konfiguroida muutoksen käynnistyshakemiston [.env](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/.env)-tiedostossa. Muuten se luodaan data-hakemistoon seuraavasti:

```bash
DATABASE_FILENAME=database.sqlite
```

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

Sovelluksen avautuessa voit valita haluatko luoda uuden virtuaalilemmikin vai kirjautua sisään jo olemassa olevan virtuaalilemmikin tiedoilla.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/welcome_view.png" alt="Kuva aloitusnäkymästä." width="320" height="250">

## Virtuaalilemmikin luominen

- Paina aloitusnäkymässä nappia `I dont't have a pet yet`.
- Syötä kenttiin lemmikin nimi ja salasana. Valitse myös lemmikki. Paina `Adopt a pet!` nappia.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/adopt_view.png" alt="Kuva adoptionäkymästä." width="320" height="250">

## Sisään kirjautuminen

- Paina aloitusnäkymässä nappia `I already have a pet`.
- Syötä kenttiin lemmikin nimi ja salasana ja paina `Log in with your pet!` nappia.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login_view.png" alt="Kuva kirjautumisnäkymästä." width="320" height="250">

## Pelin pelaaminen

Sovelluksen päänäkymässä on nappeja, josta tapahtuu asioita. Vasemassa reunassa sijaitsee lemmikin rakkausmittari. Tee parhaasi ja täytä se tekemällä **hyviä** asioita lemmikillesi.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/main_view.png" alt="Kuva päänäkymästä." width="320" height="250">

- Paina `Love` nappia jos haluat antaa rakkautta lemmikillesi.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/love_clicked.png" alt="Kuva love-napin painamisesta." width="320" height="250">

- Paina `Feed` nappia jos haluat ruokkia lemmikkiäsi.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/feed_clicked.png" alt="Kuva feed-napin painamisesta." width="320" height="250">

- Paina `Hurt :(` nappia jos haluat satuttaa lemmikkiäsi.
- Paina `Close game` nappia jos haluat lopettaa pelin tai kirjautua ulos. Uloskirjautuminen palauttaa käyttäjän sovelluksen aloitusnäkymään.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/close_game_view.png" alt="Kuva lopetusnäkymästä." width="320" height="250">


