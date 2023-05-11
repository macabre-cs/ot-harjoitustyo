# Testausdokumentti

Sovellusta on testattu unittestilla automatisoiduilla yksikkö- ja integraatiotason testeillä. Eli yksittäisten luokkien testien lisäksi sovellusta on testattu eri luokkien yhdistelmien tuottavaa toiminnallisuutta. Sovelluksen järjestelmätestaus on toteutettu manuaalisesti.

## Yksikkö- ja integraatiotason testit

### Sovelluslogiikka

Sovelluksen ensisijaisista loogisista operaatioista vastaa `PetService`-luokka. Sitä testataan [TestPetService](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/tests/services/pet_service_test.py)-testiluokalla. Testeissä on käytössä `MockPetRepository`-luokka, jonka repository-olio injektoidaan riippuvuudeksi `PetService`-testioliolle. Tämä operaatio mahdollistaa tiedon tallentamisen muistiin pysyväistallennuksen sijasta.

### Repositorio

`PetRepository`-luokkaa testataan [TestPetRepository](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/tests/repositories/pet_repository_test.py)-testiluokalla. `PetRepository` -luokan testeissä käytetään vain testaamiseen tarkoitettua tiedostoa. Tiedoston nimi on konfiguroitu [.env.test](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/.env.test)-tiedostoon seuraavalla tavalla:

```bash
DATABASE_FILENAME=test-database.sqlite
```

### Testien kattavuus

Sovelluksen käyttöliittymän testaus on toteutettu pitkälti manuaalisesti, joten sitä ei ole huomioitu testikattavuusraportissa.

![](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/testikattavuus.png)

Kuten kuvasta näkee sovelluksen testien haaraumakattavuus on korkea (91%). Muutamien tiedostojen suorittamista komentoriviltä *(build.py ja initialize_database.py)* ei ole testattu. Nämä tiedostot olisi kuitenkin voinut myös jättää testikattavuuden ulkopuolelle. Muutama sovelluksen funktio jäi myös vaille testiä.

## Järjestelmän testit

Sovelluksen järjestelmän tai graafisen käyttöliittymän testit ovat toteutettu manuaalisesti.

## Asennus

Sovellus on asennettu ja testattu [käyttöohjeen](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) ohjeiden mukaan. Sovellusta on testattu Linux- ja Window-ympäristöissä. Sovellusta on testattu jo olemassa olevilla tiedostoilla (tietokanta) ja myös tilanteessa, jossa sovellus on luonut uudet.

## Toiminnallisuus

Sovellusta on testattu kaikilla [käyttöhjeessa](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) ja [vaatimusmäärittelyssä](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) esitettyjen tapojen mukaan. Olen myös yrittänyt parhaani mukaan aiheuttaa virheitä tai muuta epätoivottuja asioita testien yhteydessä.
