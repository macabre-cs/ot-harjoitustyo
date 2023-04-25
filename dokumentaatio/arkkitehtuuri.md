# Sovelluksen arkkitehtuuri

## Rakenne

Kansio [ui](https://github.com/macabre-cs/ot-harjoitustyo/tree/master/src/ui) sisältää koodit, jotka vastaavat sovelluksen käyttöliittymästä ja sovelluksen toiminnallisuudesta.

![Kansionsisältö](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kansiorakenne.png)

## Käyttöliittymä

Käyttöliittymässä on 2 eri näkymää:

- Pelin päänäkymä (itse peli)
- Pelin sulkeminen

## Sovelluslogiikka

Sovelluksen [UI-luokka](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/ui.py) on vastuussa eri näkymien näyttämisestä ja piilottamisesta. Luokat [MainView](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/main_view.py) ja [CloseGameView](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/src/ui/close_game_view.py) taas vastaavat omien näkymiensä toiminnallisuuksista (esimerkiksi nappien painamisesta).

```mermaid
classDiagram
  UI -- MainView
  UI -- CloseGameView
  
  class UI{
    
  }
  class MainView{
    -_love_clicked(self)
    -_feed_clicked(self)
    -_hurt_clicked(self)
  }
  class CloseGameView{
    -_yes_clicked(self)
  }
```
## Sovelluksen toiminnallisuus

*tähän kiva teksti sovelluksen toimintalogiikasta*

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
