# 🏋️‍♂️ FitMateo

Webová a mobilní aplikace pro hledání sportovních parťáků a sparring partnerů.  
Bez matchování, bez swipování, bez sociálního balastu.  
Jednoduchý nástroj, který má jediný cíl: dostat lidi ke společnému sportu.

---

## 📖 O projektu

Tato aplikace slouží k propojení lidí, kteří hledají sportovního parťáka do fitka, na bojové sporty nebo jiné individuální či skupinové aktivity.

Nejde o seznamku ani klasickou sociální síť.  
Uživatel si vytvoří profil, přidá sportovní inzerát a ostatní mu mohou rovnou napsat.

Projekt je primárně zaměřený na Českou republiku a větší města, ale architektura je od začátku navržená tak, aby bylo možné aplikaci v budoucnu rozšířit i globálně.

---

## 🎯 Cílová skupina

- Lidé ve věku přibližně 18 až 30 let  
- Začátečníci i pokročilí sportovci  
- Lidé, kteří nechtějí trénovat sami  
- Sportovci hledající motivaci, disciplínu nebo sparring  

Typicky uživatelé, kteří nechtějí psát do Facebook skupin nebo čekat, až se někdo ozve.

---

## ⚙️ Základní funkce při spuštění

### 👤 Uživatelský profil
- Registrace a přihlášení  
- Základní informace o uživateli  
- Lokalita  
- Preferované sporty  
- Úroveň zkušeností  

### 📢 Sportovní inzeráty
- Vytvoření inzerátu ke konkrétnímu sportu  
- Popis, lokalita a časové možnosti  
- Možnost mít více inzerátů pro různé sporty  

### 🔍 Vyhledávání
- Filtrování podle sportu  
- Filtrování podle lokality  
- Přehledné zobrazení dostupných inzerátů  

### 💬 Komunikace
- Přímý real time chat mezi uživateli  
- Žádné matchování  
- Každý může napsat komukoliv s aktivním inzerátem  

---

## 🧠 Filozofie projektu

- Minimum překážek mezi uživateli  
- Žádné algoritmy a žádné swipování  
- Důraz na reálný pohyb a offline aktivitu  
- Aplikace má pomáhat sportovat, ne v ní trávit čas  

Aplikace má být prostředek, ne cíl.

---

## 🚀 Budoucí vize

Projekt je navržen modulárně, aby bylo možné postupně přidávat nové funkce bez nutnosti přepisování celé aplikace.

### Plánovaná rozšíření
- Hodnocení spolehlivosti uživatelů  
- Historie spoluprací  
- Veřejné sportovní příspěvky a fotky  
- Jednoduchý feed zaměřený čistě na sport  
- Skupinové tréninky a otevřené akce  
- Push notifikace  

Dlouhodobým cílem je vytvořit sportovní komunitu, ne další klasickou sociální síť.

---

## 🛠️ Technologický stack

### Backend
- Django  
- Django REST Framework  
- Django Channels  

### Databáze
- SQLite pro lokální vývoj  
- PostgreSQL pro produkční prostředí  

### Frontend
- Moderní webová aplikace  
- Důraz na jednoduchost, přehlednost a rychlost  

---

## 📌 Stav projektu

Projekt je ve fázi aktivního vývoje.  
Základní architektura je připravená s ohledem na škálování, rozšiřitelnost a dlouhodobý provoz.

---

## 📄 Licence

Tento projekt je zatím určen pro osobní a výukové účely.  
Licenční podmínky budou upřesněny v pozdější fázi vývoje.





WORK IN PROGRESS
## VIEWER APP
- [ ] 1.0 Seznam sportů (abecedně)
  - [ ] 1.1 Možnost kliknutí a zobrazení sportovních akcí

- [ ] 2.0 Detail sportu
  - [ ] 2.1 Název
  - [ ] 2.2 Typ sportu
  - [ ] 2.3 země
  - [ ] 2.4 lokace
  - [ ] 2.5 město
  - [ ] 2.6 začátek
  - [ ] 2.7 konec
  - [ ] 2.8 kapacita
---
- [x] 3.0 Seznam událostí (abecedně)
  - [ ] 1.1 Možnost filtrování dle:
    - [ ] 1.1.1 Data
    - [ ] 1.1.2 Sportu
    - [ ] 1.1.3 Města
    - [ ] 1.1.4 Paginace výsledků 3x4?
---
- [ ] 4.0 Detail události
-   [ ] 4.1 Název
-   [ ] 4.2 Datum od/do
-   [ ] 4.3 Čas od/do
-   [ ] 4.4 Celý popis události
-   [ ] 4.5 Adresa,lokace
-   [ ] 4.6 Obrázek
-   [ ] 4.7 Proklik ze seznamu událostí
---
- [ ] 5.0 Přidávání událostí
  - [ ] 5.1 Název
  - [ ] 5.2 Datum od/do
  - [ ] 5.3 Čas od/do
  - [ ] 5.4 Vlastník (uživatel, který událost vytvořil)
  - [ ] 5.5 Obrázek události
  - [ ] 5.6 Popis události
---
- [ ] 6.0 Úprava událostí
  - [x] 6.1 **Úprava**
    - [x] 6.1.1 Pouze ORGANIZÁTOR
  - [x] 6.2 **Mazání**
    - [x] 6.2.1 Pouze ORGANIZÁTOR který je VLASTNÍK
---
- [ ] 7.0 Seznam měst
  - [ ] 7.1 Řazení do krajů
  - [ ] 8.2 Interaktivní mapa krajů, po kliknutí se zobrazí stránka s městy v kraji

- [ ] 8.0 Detail města
  - [ ] 8.1 Název
  - [ ] 8.2 Zip code
  - [ ] 8.3 Země
  - [ ] 8.4 Kraj


## SEARCH BAR APP
- [ ] 1.0 Search bar v navbaru
    - [ ] 1.1 Hledání dle klíčového slova
    - [ ] 1.2 Hledání v popisku, názvu a dle sportu
    - [ ] 1.3 Filtrování výsledků
---


## Places app
- [ ] 1.0 Seznam míst (abecedně)
  - [ ] 1.1 Možnost kliknutí a zobrazení detailu místa
  - [ ] 1.2 Filtrování tagů
  





