```mermaid
---
title: Monopoli
---

classDiagram
  Monopoli <|-- Pelaaja
  Monopoli <|-- Pelilauta
  Monopoli <|-- Ruutu
  Monopoli <|-- Pelinappula
  Monopoli : +Pelataan kahdella nopalla
  Monopoli : +Pelataan yhdella pelilaudalla
  Monopoli : +Pelaajia 2-8
  Pelilauta -- Ruutu : Pelilauta sisältää 40 ruutua
  Pelaaja -- Pelinappula : Pelaajalla on yksi pelinappula
  Pelinappula -- Ruutu : Pelinappula sijaitsee aina yhdessä ruudussa
  Ruutu -- Pelilauta : Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla
  Ruutu <|-- Aloitusruutu
  Ruutu <|-- Vankila
  Ruutu <|-- Sattuma ja yhteismaa
  Ruutu <|-- Asemat ja laitokset
  Ruutu <|-- Normaalit kadut
  Monopoli -- Aloitusruutu : Monopolipelin täytyy tuntea sijainti
  Monopoli -- Vankila : Monopolipelin täytyy tuntea sijainti
  Sattuma ja yhteismaa <|-- Kortti
  Kortti <|-- Toiminto
  Normaalit kadut -- Pelaaja : Pelaaja voi omistaa kadun
  class Pelaaja{
     +Raha
  }
  class Pelilauta{
      
  }
  class Ruutu{
     
  }
  class Pelinappula{
     
  }
  class Normaalit kadut{
     +Nimi
  }
  class Sattuma ja yhteismaa{
     
  }
  class Kortti{
     
  }
  class Toiminto{
     
  }
  class Normaalit kadut{
     +Voi rakentaa korkeintaan 4 taloa tai yhden hotellin
  }
  
  ```
