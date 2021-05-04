# Käyttöohje

Lataa sovelluksen uusimman releasen lähdekoodi.

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

### Sovelluksen käyttö

Aja sovellus komennolla:

```bash
poetry run invoke start
```

Paina avautuvasta ikkunasta nappia "Solve". Nyt sovellus laskee automaattisesti approksimaation lyhyimmälle kauppamatkustajan reitille. Sovellus tulostaa reitin koordinaatit vierailujärjestyksessä terminaaliin, tallentaa nämä tiedostoon "route" ja luo kuvan reitistä tiedostoon "route.png". Tulostiedostot löytyvät kansiosta "results".
