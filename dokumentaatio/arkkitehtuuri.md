# Sovelluksen arkkitehtuuri

## Rakenne

Kansio [ui](https://github.com/macabre-cs/ot-harjoitustyo/tree/master/src/ui) sisältää koodit, jotka vastaavat sovelluksen käyttöliittymästä ja käyttöliittymälle olennaisesta toiminnallisuudesta (lähinnä napit). Kansio [services](https://github.com/macabre-cs/ot-harjoitustyo/tree/master/src/services) sisältää koodia, joka vastaa sovelluksen käyttäjän ja tietokannan välisestä toiminnallisuudesta. Eli esimerkiksi käyttäjän kirjautumisesta. [Repositories](https://github.com/macabre-cs/ot-harjoitustyo/tree/master/src/repositories)-kansio taas sisältää koodia, joka vastaa tiedon käsittelystä tietokannassa. [Entities](https://github.com/macabre-cs/ot-harjoitustyo/tree/master/src/entities)-kansio sisältää sovelluksen Pet-luokan koodin.

Sovelluksen rakennetta kuvaava kaavio. Kaaviossa on sovelluksen pakkaukset (kansiot) ja niiden sisältämät luokat.

![Sovellusta kuvaava kaavio](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sovelluskavio.drawio.png)

## Käyttöliittymä

Käyttöliittymässä on 5 eri näkymää:

- Aloitusnäkymä
- Lemmikin adoptointinäkymä
- Lemmikin kirjautumisnäkymä
- Päänäkymä
- Sulkemisnäkymä

Eri näkymien näyttämisestä vastaa [UI-luokka](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/ui.py). Jokainen näkymä on toteutettu omana luokkanaan. Eri näkymissä kutsutaan [PetService](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/services/pet_service.py)-luokan metodeja, jotka ovat vastuussa sovelluslogiikasta. Suurin osa sovelluksen toiminnallisuudesta vastaavasta koodista on eristetty käyttölittymän koodista. Käyttöliittymän koodiin on jätetty sille olennaiset sovelluslogiikkaan liittyvät tehtävät, kuten eri viestilaatikkojen näyttäminen käyttäjälle.

## Sovelluslogiikka

Sovelluksen [UI-luokka](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/ui.py) on vastuussa eri näkymien näyttämisestä ja piilottamisesta. Luokat [MainView](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/main_view.py) ja [CloseGameView](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/close_game_view.py) taas vastaavat omien näkymiensä toiminnallisuuksista (esimerkiksi nappien painamisesta). Sovelluksen muut käyttöliittymään liittyvät näkymät toimivat jokseenkin samoilla periaatteilla. Tietokantaa vaativa toiminnallisuus on eristetty käyttöliittymän toiminnallisuudesta.

Käyttäjälle ja lemmikin tiedoista oleellisesta toiminnallisuudesta vastaa [PetService](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/services/pet_service.py)-luokka, joka sisältää kirjautumiseen ja tietokannasta tiedon hakemiseen liittyviä toimintoja. [PetRepository](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/repositories/pet_repository.py)-luokka taas vastaa tiedon käsittelystä tietokannassa, kuten esimerkiksi virtuaalilemmikin tietojen kirjaamisesta tietokantaan. Luokka [Pet](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/entities/pet.py), on luokka joka kuvaa käyttäjän virtuaalilemmikkiä.


## Tietojen tallentaminen

[PetRepository](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/repositories/pet_repository.py)-luokka on vastuussa tietojen tallentamisesta SQLite-tietokantaan. Virtuaalilemmikin tiedot (nimi, salasana, edistys ja kuva) tallennetaan tietokannassa pets-tauluun. Taulu alustetaan [initialize_database.py](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/initialize_database.py) tiedostossa, jossa ensin tuhotaan mahdollisesti jo olemassa oleva pets-taulu, ja luodaan uusi tyhjä pets-taulu tilalle.


## Sovelluksen toiminnallisuus

Sovelluksessa on kahdenlaisia toiminnallisuuksia.

- **Pelaamiselle** olennaiset toiminnallisuudet kuten virtuaalilemmikin ruokkimen ja helliminen.
- Virtuaalilemmikin **tietojen tallentamiselle** olennaiset toiminnallisuudet kuten lemmikin adoptoiminen ja lemmikin poistaminen.

### Virtuaalilemmikin luominen

Sovelluksen avautuessa käyttäjän voi adoptoida uuden lemmikin painamalla nappia ''I dont't have a pet yet'', joka vie käyttäjän uuteen näkymään, jossa käyttäjä syöttää lemmikin nimen ja salasanan. Painamalla ''Adopt your new little friend!'' käyttäjä kirjataan sisään sovellukseen uudella lemmikillään.

*UI-luokka kutsuu sisällään eri näkymiä vaihtavia metodeja, mutta halusin kuvata sen seuraavalla tavalla sekvenssikaaviossa, koska muuten kaaviosta olisi tullut kovin tuhti ja sekava.*

```mermaid
sequenceDiagram
    actor User
    participant main
    participant UI
    participant WelcomeView
    participant AdoptView
    participant PetService
    participant PetRepository
    participant puolukki
    participant MainView
    
    main->>UI: UI(window)
    main->>UI: start()
    UI->>WelcomeView: _show_welcome_view()
    User->>WelcomeView: click "I don't have a pet yet" button
    WelcomeView->>UI: _handle_show_adopt_view
    UI->>AdoptView: _show_adopt_pet_view()
    User->>AdoptView: fills name and password entries and clicks "Adopt your new little friend!" button
    AdoptView->>PetService: adopt_pet("puolukki", "puolukka")
    PetService->>PetRepository: locate_pet_by_name("puolukki")
    PetRepository-->>PetService: None
    PetService->>puolukki: Pet("puolukki", "puolukka")
    PetService->>PetRepository: create("puolukki", "puolukka")
    PetRepository-->>PetService: pet
    PetService-->>AdoptView: pet
    AdoptView->>UI: _handle_adopt_pet()
    UI->>MainView: _show_main_view() 

```
Auki kirjoitettuna käyttäjän avattua sovelluksen ja painettua "I don't  have a pet yet" nappia, käyttäjä syöttää lemmikin nimen ja salasanan niille osoitetuille kentille ja painaa "Adopt your new little friend!" nappia. Tämän jälkeen PetService-luokka tarkistaa PetRepository luokalta, onko tämän niminen lemmikki jo tietokannassa. Tässä tapauksessa ei ole joten PetRepository-luokka palauttaa None. PetService kutsuu Pet-luokkaa, jossa luodaan puolukille Pet-olio. Sen jälkeen PetService-luokka kutsuu PetRepository-luokkaa, jossa kirjataan tietokantantaan uusi lemmikki puolukki, jonka jälkeen PetRepository luokka palauttaa sen takaisin PetService luokalle. Tämän jälkeen käyttäjälle avautuu pelin päänäkymä, jossa on hänen virtuaalilemmikkinsä.

## Sovelluksen heikkoudet

### Käyttöliittymä ja rakenne

Käyttöliittymä on osittain liian sidottu sovelluksen toiminnallisuuteen. Moni oleellinen asia, on kiinni käyttöliittymän koodissa, joka hankaloittaa sovelluslogiikan testaamista. Eri näkymien luokkien koodi ei myöskään ole kovin yhtenäistä, koska olen testaillut eri asioita eri näkymissä. Tämä tekee koodista hankalampaa ymmärtää.
