## Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovellus antaa approksimoidun ratkaisun [kauppamatkustajan ongelman](https://fi.wikipedia.org/wiki/Kauppamatkustajan_ongelma) käyttäjän antamalle verkolle, eli yrittää löytää mahdollisimman lyhyen reitin, joka käy jokaisessa annetussa koordinaatistossa

### Käyttäjät

Käyttäjiä on yksi.

### Käyttöliittymäluonnos

Alustavasti sovelluksessa on tarkoitus olla kaksi tai kolme näkymää. Syöttönäkymässä käyttäjä voi antaa verkon koordinaatit joko manuaalisesti tai tiedostossa. Ratkaistu reitti näytetään tulosnäkymässä. Sovellukseen tulee mahdollisesti laskentanäkymä, jossa käyttäjä näkee laskennan etenemisen. Sovellus aukeaa syöttönäkymään, josta syötteen jälkeen voi siirtyä laskentaan. Laskennan jälkeen sovellus siirtyy automaattisesti tulosnäkymään.

### Perusversion tarjoama toiminnallisuus

* Syötteen voi antaa manuaalisesti yksittäisiä koordinaatteja syöttämällä tai antamalla koordinaatistot tiedostossa **tehty**
* Tulos esitetään graafisesti. **tallennus kuvatiedostoon tehty**
* Tulos tallennetaan tiedostoon. **tehty**
* Koordinaattien etäisyys lasketaan [euklidisena etäisyytenä](https://fi.wikipedia.org/wiki/Euklidinen_metriikka). **tehty**


### Jatkokehitysideoita

Perusversion jälkeen sovellusta täydennetään 
* eri ratkaisualgoritmeja lisäämällä.
* mahdollistamalla epäeuklidiset verkot.
