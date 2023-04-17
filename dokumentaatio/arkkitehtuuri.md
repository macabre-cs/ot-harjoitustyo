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
