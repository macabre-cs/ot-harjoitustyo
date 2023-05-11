# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen päätarkoituksena on viihdyttää käyttäjää. Sovellus on peli, jossa käyttäjä pääsee huolehtimaan omasta virtuaalilemmikistään. Sovelluksessa käyttäjä voi luoda uuden lemmikin kolmesta eri vaihtoehdosta ja nimetä sen. Lemmikit tallennetaan tietokantaan käyttäjän määrittelemällä nimellä ja salasanalla, joten käyttäjällä voi olla useita lemmikkejä samanaikaisesti. Sovelluksessa lemmikille voi antaa hellyyttä, ruokaa tai kärsimystä.Pelin idea on saanut paljon inspiraatiota [Tamagotcheista](https://fi.wikipedia.org/wiki/Tamagotchi).

## Perustoiminnallisuus
- Sovelluksen avautuessa käyttäjä voi kirjautua sisään tai adoptoida uuden lemmikin
- Lemmikin voi valita kolmesta eri vaihtoehdosta ja nimetä.
- Lemmikillä on rakkausmittari
- Virtuaalilemmikkiä voi helliä
- Virtuaalilemmikkiä voi syöttää
- Virtuaalilemmikille voi tuottaa kärsimystä

## Toiminnallisuudesta tarkemmin
- Virtuaalilemmikillä tulee olla uniikki nimi ja sen pitää olla alle 22 merkkiä pitkä
  - Eli voi olla olemassa vain yksi "Mansikki"
- Virtuaalilemmikin edistyminen tallentuu automaattisesti
  - Eli käyttäjä voi jatkaa myöhemmin siitä mihin jäi
- Virtuaalilemmikin tiedot voi poistaa satuttamalla sitä

## Käyttöliittymäluonnos
*Alustava käyttöliittymäluonnos. Virtuaalilemmikin yläpuolella on paikka virtuaalilemmikin nimelle ja alapuolella valikko eri toiminnoille.*

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/alustava_kayttoliittyma.png" alt="Kuva alustavasta käyttöliittymäluonnoksesta. Kuvassa on kissaa muistuttava virtuaalilemmikki, jonka yläpuolella on paikka virtuaalilemmikin nimelle ja alapuolella valikko eri toiminnoista." width="635" height="449">


*Lopullinen pelin päänäkymä*

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/main_view2.png" alt="Kuva päänäkymästä.">

## Grafiikka

**Pelin "päämaskotti" ja ensimmäiseksi kuvitettu virtuaalilemmikki.**

<img src="https://github.com/macabre-cs/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Rotta_Otus_300x300.png" alt="Kuva virtuaalilemmikistä. Virtuaalilemmikki muistuttaa ulkomuodoltaan rottaa. Virtuaalilemmikillä on valkoinen turkki, jossa on sinisiä laikkuja ja sillä on vaaleanpunainen häntä.">

Lopullisessa pelissä voi valita kolmesta eri virtuaalilemmikistä. Lemmikkien väriteemat vastaavat eri [Pride-lippuja](https://fi.wikipedia.org/wiki/LGBTQ%2B-symbolit#Liput).

lemmikki 1 | lemmikki 2 | lemmikki 3
--- | --- | ---
![trans-lipun värinen lemmikki](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/data/graphics/Rotta_Otus_300x300.png) | ![pride-lipun värinen lemmikki](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/data/graphics/Homo_Rotta_Otus_300x300.png) | ![ace-lipun värinen lemmikki](https://github.com/macabre-cs/ot-harjoitustyo/blob/master/data/graphics/Ace_Rotta_Otus_300x300.png)

Virtuaalilemmikit on kuvittanut ystäväni [Haze Laine](https://www.instagram.com/hasuart_/). Kiitos Haze <3

## Jatkokehitysideoita
- Virtuaalilemmikin tiedot voi poistaa satuttamatta sitä
  - Samaa nimeä ei kuitenkaan voisi sitten valita uudelle virtuaalilemmikille
  - Joku teksti, joka rikkoo neljännen seinän esim.*"Mansikki on jo ollut keskuudessamme, valitsethan toisen nimen virtuaalilemmikillesi."*
- Lisää toimintoja peliin
  - Virtuaalilemmikin voi laittaa nukkumaan
  - Virtuaalilemmikin voi pestä
  - Muita hauskoja tai kamalia toimintoja
- Hienompi käyttöliittymä
- Mahdollisuus vaihtaa käyttöliittymän kieli japaniksi *(olisi söpö tribuutti alkuperäiselle tamagotchille)*
- Käyttäjä voisi kirjautua myös sisään itse ja tarkastella jostain valikosta eri lemmikkejään
- Enemmän sovelluslogiikkaa
  - Eri ruokavaihtoja, jotka voisi tallentaa tietokantaan
  - Valuutta, jolla voisi ostaa eri ruokia
  - Eri ruoista saisi enemmän pisteitä rakkausmittariin (tästä saisi myös hyvin testejä)
  - Virtuaalilemmikin rakkausmittari alenee jotenkin
- Mahdollisuus saada [shiny](https://bulbapedia.bulbagarden.net/wiki/Shiny_Pok%C3%A9mon)-virtuaalilemmikki
