# Ohjelmistotekniikka, harjoitustyö
## Virtuaalilemmikki
Sovellus on peli, jossa käyttäjä pääsee huolehtimaan omasta virtuaalilemmikistään. Pelin idea on saanut paljon inspiraatiota [Tamagotcheista](https://fi.wikipedia.org/wiki/Tamagotchi).

## Dokumentaatio
- [Käyttöohje](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Release

Sovelluksen releaset löytyy [täältä](https://github.com/macabre-cs/ot-harjoitustyo/releases).

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
