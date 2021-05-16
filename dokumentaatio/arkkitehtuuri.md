# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne noudattaa kaksitasoista kerrosarkkitehtuuria.

## Sovelluslogiikka

Sovelluslogiikka rakentuu luokkien City, Route, File\_reader ja Output\_handler varaan. File\_reader ja Output\_handler ovat tiedostojen käsittelyyn liittyviä luokkia; File\_reader lukee kaupunkien koordinaatit datatiedostosta (kansiosta "/data/"") ja luo niistä listan City-luokan olioita. Output\_handler kirjoittaa tulostiedostot "/results/"-kansioon. Luokka Route saa argumentiksiin listan City-luokan olioita. Route-luokan metodi "solve()" ratkaisee approksimoidun ratkaisun kauppamatkustajan ongelmaan. Luokkien väliset riippuvuudet on kuvailtuna alla olevassa luokkakaaviossa.

![Luokkakaavio](./kuvat/luokkakaavio.png)

## Sekvenssikaavio

Sekvenssikaavio kuvaa nykyistä kaupunkia (city1) lähimpänä olevan kaupungin lisäämistä reitille seuraavaksi.

![Sekvenssikaavio](./kuvat/sekvenssikaavio.png)
