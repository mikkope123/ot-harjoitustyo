## Vaatimusmäärittely

### Sovelluksen tarkoitus

Sovellus antaa approksimoidun ratkaisun [kauppamatkustajan ongelman](https://fi.wikipedia.org/wiki/Kauppamatkustajan_ongelma) käyttäjän antamalle verkolle, eli yrittää löytää mahdollisimman lyhyen reitin, joka käy jokaisessa annetussa koordinaatistossa

### Käyttäjät

Käyttäjiä on yksi.

### Käyttöliittymä

Sovelluksessa on kaksi toisistaan itsenäistä osaa: syöttötiedoston rakennussovellus ja ratkaisinsovellus. Rakennussovelluksessa on tekstikäyttöliittymä, joka kysyy ensin kuinka monta kaupunkia käyttäjä haluaa syöttää ja tämän jälkeen jokaisen kaupungin koordinaatit. Syöttötiedostoa voi muokata myös manuaalisesti tekstieditorilla, mutta ratkaisinsovellus ei tarkista syöttötiedoston muotoa.

Ratkaisinsovelluksessa on graafinen käyttöliittymä, josta voi valita tulosgraafin tallennusmuodon. Ratkaisin aloittaa laskennan painamalla käyttöliittymän "Solve"-nappia. Laskennan päätteeksi ohjelma tulostaa ratkaistun reitin terminaaliin.

### Perusversion tarjoama toiminnallisuus

* Syötteen voi antaa manuaalisesti yksittäisiä koordinaatteja syöttämällä tai antamalla koordinaatistot tiedostossa
* Tuloksesta luodaan kuvatiedosto.
* Tulos tallennetaan tiedostoon.
* Koordinaattien etäisyys lasketaan [euklidisena etäisyytenä](https://fi.wikipedia.org/wiki/Euklidinen_metriikka).
* Reitti ratkaistaan [lähimmän naapurin -algoritmilla](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm).


### Jatkokehitysideoita

Tätä perusversiota voisi parantaa muun muassa:
* eri ratkaisualgoritmeja lisäämällä.
* mahdollistamalla epäeuklidiset verkot.
* luomalla syöttötiedoston rakennussovellukseen graafisen käyttöliittymän.
* antamalla käyttäjän määrittää syöttö- ja tulostiedostojen nimet ja sijainnin.
