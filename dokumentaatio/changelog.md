# Changelog

## Viikko 3
- Virtuaalilemmikki on kuvitettu.
- Luotu pelille alustava käyttöliittymä.
<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tkinter_alustava_kayttoliittyma.png" alt="Kuva alustavasta käyttöliittymästä, joka on luotu TkInterillä. Käyttöliittymän keskellä on virtuaalilemmikki ja sen alapuolle on kolme nappia joissa lukee Feed, Love ja Hurt :(. Virtuaalilemmikin yläpuolella on paikka sen nimelle." width="195" height="216">

- Luotu UI-luokka, joka toimii alustavasti koko pelinä.
- Käyttäjä voi painaa eri nappeja, jotka tulostavat komentoriville tulosteen. Painamalla ''Hurt :('' nappia pelin ikkuna myös sulkeutuu.
- Testattu, että UI-luokka toimii. Kaikki napit toimivat ja tulostavat oikeat tulosteet komentoriville. Ikkunan tuhoaminen myös toimii.
- Aloitettu NamePetView-luokka, joka vastaa virtuaalilemmikin nimeämisikkunasta (ei toimi vielä).

## Viikko 4
- Sovelluksen koodin rakenne on uusittu kokonaan, jotta se olisi selkeämpi.
- Käyttäjä voi lopettaa pelin uudesta ''Close game'' napista, joka avaa käyttäjälle uuden ikkunan, jossa kysytään haluaako käyttäjä lopettaa pelin.
- Sovelluksen nappeja painamalla käyttäjän ruudulle ilmestyy ikkuna, joka kertoo käyttäjälle mitä hän teki pelissä. Nappien painaminen ei enää tulosta komentoriville mitään.
- Luotu uusi luokka MainView, joka vastaa sovelluksen pääikkunasta ja sen toiminnallisuuksista.
- Luotu uusi luokka CloseGameView, joka vastaa sovelluksen sulkemisikkunasta.
- UI-luokkaa on päivitetty
- Testattu luokkien toiminnallisuutta (toimii)

## Viikko 5
- Käyttäjä voi nyt adoptoida uuden lemmikin tai kirjautua sisään jos hänellä on jo lemmikki. Eli käyttäjä voi rekisteröityä tai kirjautua sisään.
- Luotu uusi luokka Pet, joka luo jokaiselle lemmikille Pet-olion.
- Luotu uusi luokka PetService, joka vastaa lemmikin adoptoinnin ja kirjautumisen toiminnallisuudesta.
- Luotu uusi luokka PetRepository, joka vastaa SQLite-tietokannan ja virtuaalilemmikin yhteydestä. Eli tallentaa tiedot tietokantaan, etsii tiedot tietokannasta ja poistaa tiedot tietokannasta.
- Luotu uusi luokka WelcomeView, joka vastaa sovelluksen aloitusnäkymästä.
- Luotu uusi luokka AdoptView, joka vastaa virtuaalilemmikin luomisnäkymästä.
- Luotu uusi luokka LoginView, joka vastaa jo olemassa olevan virtuaalilemmikin kirjautumisnäkymästä.
- Testattu luokan PetRepository toimivuutta (lemmikin luominen ja etsiminen nimellä sekä pelaajan rankaiseminen).
- Aloitettu luokan PetService testaus (nykyisen lemmikin hakeminen).

## Viikko 6
- Lisätty uusi ''Logout''-nappi. Käyttäjä voi nyt kirjata lemmikkinsä ulos (nappi on pelin lopetusnäkymässä). Uloskirjautuessa sovellus avaa aloitusnäkymän, eikä sammuta sovellusta.
- Jatkettu luokan PetService testausta.
- Jatkettu luokan PetRepository testausta.
- Aloitettu graafisen käyttöliittymän söpöyttäminen.

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/alustava_kayttoliittymaV2.png" alt="Kuva söpömmästä alustavasta käyttöliittymästä." width="320" height="250">

## Viikko 7
- Ympäristömuuttujien käyttöönotto
- Lisätty edistysmittari peliin
- Lisätty käyttäjälle eri vaihtoehtoja lemmikin ulkomuotoon
  - Virtuaalilemmikin on kuvittanut ystäväni [Haze Laine](https://www.instagram.com/hasuart_/).

lemmikki 1 | lemmikki 2 | lemmikki 3
--- | --- | ---
![trans-lipun värinen lemmikki](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/data/graphics/Rotta_Otus_300x300.png) | ![pride-lipun värinen lemmikki](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/data/graphics/Homo_Rotta_Otus_300x300.png) | ![ace-lipun värinen lemmikki](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/data/graphics/Ace_Rotta_Otus_300x300.png)
- Testit päivitetty testaamaan sovelluksen nykyistä toiminnallisuutta
