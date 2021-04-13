## TSP solver

Sovellus antaa ratkaisun kauppamatkustajan ongelmaan. Kaupunkeja lisätään yksi kerrallaan siten Nearest neighbor -algoritmilla, eli valitsemalla viimeiseksi vierailusta kaupungista lähimpänä oleva kaupunki seuraavaksi reitille.

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/mikkope123/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Asennus

1. asenna riippuvuudet komennolla

poetry install

2. suorita vaadittavat alustustoimenpiteet komennolla

poetry run invoke build

3. aja sovellus komennolla

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
