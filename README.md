# TSP solver

Sovellus antaa ratkaisun kauppamatkustajan ongelmaan. Kaupunkeja lisätään yksi kerrallaan siten Nearest neighbor -algoritmilla, eli valitsemalla viimeiseksi vierailusta kaupungista lähimpänä oleva kaupunki seuraavaksi reitille.

## Dokumentaatio

[Käyttöohje](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

[Työaikakirjanpito](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Releaset


[Release 1](https://github.com/mikkope123/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/mikkope123/ot-harjoitustyo/releases/tag/viikko6)

[Release 3](https://github.com/mikkope123/ot-harjoitustyo/releases/tag/lopullinen)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Aja sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Sovelluksen suorittaminen

Sovelluksen voi suorittaa komennolla:

```bash
poetry run invoke start
```

### Koodinaattien syöttö

Voit luoda tiedoston, joka sisältää kaupunkien koordinaatit, syöttösovelluksella, joka käynnistyy komennolla:

```bash
poetry run invoke build
```

Syötä ensin haluttu kaupunkien määrä. Tämän jälkeen syötä kaupungin koordinaatit (2 kpl) erotettuna välilyönnillä (eli muodossa "XX YY", jossa XX ja YY ovat liukulukuja).

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Koodin laaduntarkistuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```

Koodin laatukriteerit on määrätty tiedostossa [.pylintrc](https://github.com/mikkope123/ot-harjoitustyo/blob/master/.pylintrc).

## Syötteet ja tulosteet

Sovellus lukee syötteen tiedostosta /data/data.txt. Tiedostossa on koordinaatit jokaiselle reitin kaupungille omalla rivillään. Ohjelma ei vielä tarkasta tiedoston oikeaa muotoa.

Sovellus tulostaa ratkaistun reitin sekä terminaaliin, että kahteen tiedostoon, jotka sijaitsevat /results-kansiossa. Tekstitiedosto route sisältää kaupunkien koordinaatit siinä järjestyksessä kuin niissä ratkaistussa reitissä vieraillaan, palaten takaisin lähtökaupunkiin. Kuvatiedosto route.png (tai .pdf/.svg, riippuen valinnasta) sisältää graafisen esityksen reitistä.
