# TSP solver

Sovellus antaa ratkaisun kauppamatkustajan ongelmaan. Kaupunkeja lisätään yksi kerrallaan siten Nearest neighbor -algoritmilla, eli valitsemalla viimeiseksi vierailusta kaupungista lähimpänä oleva kaupunki seuraavaksi reitille.

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuuri](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. asenna riippuvuudet komennolla

poetry install

2. aja sovellus komennolla

poetry run invoke start

## Komentorivitoiminnot

### Sovelluksen suorittaminen

Sovelluksen voi suorittaa komennolla

poetry run invoke start

### Testaus

Testit voi suorittaa komennolla

poetry run invoke test

### Testikattavuus

Testikattavuusraportin voi luoda komennolla

poetry run invoke coverage-report

### Pylint

Koodin laaduntarkistuksen voi suorittaa komennolla:

poetry run invoke lint

Koodin laatukriteerit on määrätty tiedostossa .pylintrc.

## Syötteet ja tulosteet

Sovellus lukee syötteen tiedostosta /src/data/data.txt. Tiedostossa on koordinaatit jokaiselle reitin kaupungille omalla rivillään. Tällä hetkellä ohjelma ei vielä tarkasta tiedoston oikeaa muotoa.

Sovellus tulostaa ratkaistun reitin sekä terminaaliin, että kahteen tiedostoon, jotka sijaitsevat /results-kansiossa. Tekstitiedosto route sisältää kaupunkien koordinaatit siinä järjestyksessä kuin niissä ratkaistussa reitissä vieraillaan, palaten takaisin lähtökaupunkiin. Kuvatiedosto route.png sisältää graafisen esityksen reitistä.
