# Ohjelmistotekniikka, harjoitustyö
## Virtuaalilemmikki
Sovellus on peli, jossa käyttäjä pääsee huolehtimaan omasta virtuaalilemmikistään. Sovelluksessa käyttäjä voi luoda uuden lemmikin kolmesta eri vaihtoehdosta ja nimetä sen. Lemmikit tallennetaan tietokantaan käyttäjän määrittelemällä nimellä ja salasanalla, joten käyttäjällä voi olla useita lemmikkejä samanaikaisesti. Sovelluksessa lemmikille voi antaa hellyyttä, ruokaa tai kärsimystä. Pelin idea on saanut paljon inspiraatiota [Tamagotcheista](https://fi.wikipedia.org/wiki/Tamagotchi).

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/main_view2.png" alt="Kuva sovelluksen päänäkymästä." width="320" height="250">

## Python-versiosta

Sovellusta on testattu Python-versiolla `3.10`. Sovelluksen toiminnallisuudessa voi ilmetä ongelmia mikäli Python-versio on alle `3.8`. 

## Dokumentaatio
- [Käyttöohje](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Release

Sovelluksen viimeisin release löytyy [tästä](https://github.com/macabre-cs/ot-harjoitustyo/releases/tag/viikko7).

## Asennus

1. Asenna sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

2. Alusta sovelluksen tietokanta komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```
## Komentorivikomennot

### Ohjelman suoritus

Ohjelman suoritus tapahtuu komennolla:

```bash
poetry run invoke start
```

### Testaus

Testien suoritus tapahtuu komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuus raportin generoiminen tapahtuu komennolla:

```bash
poetry run invoke coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon

### Pylint

Pylint-tarkistukset suoritetaan komennolla:
```bash
poetry run invoke lint
```
