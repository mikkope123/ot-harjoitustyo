# Käyttöohje

Lataa sovelluksen uusimman [releasen](https://github.com/mikkope123/ot-harjoitustyo/releases) lähdekoodi.

## Sovelluksen asentaminen

Asenna riippuvuudet komennolla:

```bash
poetry install
```
## Ohjelman käyttö

### Koodinaattien syöttö

Voit luoda tiedoston, joka sisältää kaupunkien koordinaatit, syöttösovelluksella, joka käynnistyy komennolla:

```bash
poetry run invoke build
```

Syöttösovellus pyytää ensimmäisenä syötettävien kaupunkien lukumäärän. Tämän on oltava positiivinen kokonaisluku. Hyväksytyn syötteen jälkeen sovellus pyytää syöttämään kaupunkien koordinaatit (2 reaalilukua, esim. "12.3 -5.9") erotettuna välilyönnillä. Syöttösovellus ei hyväksy aiemmin syötettyjä koordinaatteja tai koordinaatteja, jotka eivät ole liukulukuja. Virheellisellä syötteellä sovellus pyytää uutta syötettä, ja etenee vain hyväksytyn syötteen jälkeen.

### Sovelluksen käyttö

Aja sovellus komennolla:

```bash
poetry run invoke start
```

Avautuvassa ikkunassa voit valita tulosgraafin tallennusmuodon (png (oletus), pdf tai svg). Painamalla avautuvasta ikkunasta nappia "Solve" sovellus laskee automaattisesti approksimaation lyhyimmälle kauppamatkustajan reitille. Sovellus tulostaa reitin koordinaatit vierailujärjestyksessä terminaaliin, tallentaa nämä tiedostoon "route" ja luo kuvan reitistä tiedostoon "route.xxx" (xxx=valittua tiedostomuotoa vastaava pääte). Tulostiedostot löytyvät kansiosta "results".
