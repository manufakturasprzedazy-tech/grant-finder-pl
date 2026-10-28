# Karta oceny: `2026-10-28_0034_h0-cag_reasoning-on.jsonl`

Karta BEZ ocen. Dla każdego przypadku: przeczytaj pytanie, wzorzec i odpowiedź, wpisz ✅ albo ❌.
Przy ❌: najpierw jedno zdanie wolnym tekstem (co poszło nie tak), dopiero potem warstwa.
Warstwa rozstrzyga WEJŚCIE kroku: span 1 (to, co dostał model) leży w `span1_catalogue.txt`.

| id | ocena | warstwa |
|---|---|---|
| R01 |  |  |
| R02 |  |  |
| R03 |  |  |
| D04 |  |  |
| D05 |  |  |
| D06 |  |  |
| D07 |  |  |
| D08 |  |  |
| D09 |  |  |
| D10 |  |  |
| D11 |  |  |
| N12 |  |  |

---

## R01 · representative · as-of 2026-09-25

**Pytanie:** Jakie są aktualne dofinansowania dla mojej firmy, która zajmuje się hydrauliką?

**Wzorzec:**
- NIE może zawierać: any of the 8 calls closed on 2026-09-25 presented as open (rows 2, 7, 11, 12, 13, 16, 19, 26)
- NIE może zawierać: row 17 (Wysokiej jakości system włączenia społecznego) presented as open — it starts on 2026-09-30

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (40.81 s · 2289 tokenów wyjścia · finish=stop):

> Na podstawie katalogu naborów, dla firmy zajmującej się hydrauliką najbardziej odpowiednie mogą być następujące otwarte nabory (stan na 25 września 2026):
>
> ### 1. Kadry nowoczesnej gospodarki (FERS, działanie 1.3)
> Kilka podnaborów w trybie ciągłym, które mogą wspierać rozwój kompetencji, zieloną transformację i dostępność:
> - **Zielone rekomendacje** – otwarty do **2027-12-01**  
>   Wsparcie do 80% wartości projektu.  
>   Link: https://fers.parp.gov.pl/component/grants/grants/zielone-rekomendacje---oferta-dla-przedsiebiorcow
> - **GOZ – to się opłaca** – otwarty do **2027-01-01**  
>   Dofinansowanie 100% na rozwój kompetencji w zakresie gospodarki o obiegu zamkniętym.  
>   Link: https://fers.parp.gov.pl/component/grants/grants/goz---to-sie-oplaca---oferta-dla-przedsiebiorcow#opis
> - **Dostępność szansą na rozwój** – otwarty do **2027-12-01**  
>   Dofinansowanie 100% na poprawę dostępności.  
>   Link: https://fers.parp.gov.pl/component/grants/grants/dostepnosc-szansa-na-rozwoj-3---oferta-dla-przedsiebiorcow
> - **Dostępność Dyrektywa EAA** – otwarty do **2027-12-31**  
>   Dofinansowanie 100%.  
>   Link: https://fers.parp.gov.pl/component/grants/grants/dostepnosc-dyrektywa-eaa---oferta-dla-przedsiebiorcow
> - **Wsparcie firm w okresowych trudnościach** – data zakończenia: **2026/2027** (nieokreślona dokładnie, ale nadal dostępny)  
>   Wsparcie do 154 384 zł.  
>   Link: https://fers.parp.gov.pl/component/grants/grants/wsparcie-firm-w-okresowych-trudnosciach---oferta-dla-przedsiebiorcow
>
> ### 2. Polskie Mosty Technologiczne (FENG, działanie 2.24)
> - **Otwarty**: 2026-09-15 – **2026-10-30**  
>   Wsparcie ekspansji zagranicznej MŚP (do 150 tys. zł). Jeśli Twoja firma oferuje innowacyjne rozwiązania hydrauliczne i chce wejść na rynki Japonii, Chin, USA lub Wielkiej Brytanii.  
>   Link: https://www.funduszeunijne.gov.pl/nabory/224-polskie-mosty-technologiczne-3/
>
> ### 3. Wspieranie ochrony krytycznej infrastruktury energetycznej (FEnIKS, działanie 11.2)
> - **Otwarty**: 2026-05-29 – **2026-09-30** (ostatnie dni!)  
>   Budowa magazynów ciepła na poziomie systemowym – może dotyczyć instalacji hydraulicznych w dużych systemach energetycznych. Grupa docelowa: przedsiębiorstwa, administracja publiczna.  
>   Budżet: 300 mln zł.  
>   Link: https://www.funduszeunijne.gov.pl/nabory/112-wspieranie-ochrony-krytycznej-infrastruktury-energetycznej-oraz-magazynow-ciepla-na-poziomie-systemowym/
>
> ### 4. Pożyczki na rozwój turystyki (FEPW, działanie 1.5)
> - **Tryb ciągły** – brak daty zamknięcia.  
>   Pożyczki do 1 mln zł dla MŚP z branży turystycznej (np. modernizacja instalacji hydraulicznych w obiektach noclegowych).  
>   Link: https://www.bgk.pl/programy-i-fundusze/fundusze/fundusze-europejskie-dla-polski-wschodniej-2021-2027/pozyczka-na-rozwoj-turystyki/
>
> **Uwaga**: Warunki kwalifikowalności i szczegóły każdego naboru znajdziesz w regulaminie pod podanymi linkami. Katalog nie pozwala mi ocenić, czy Twoja firma dokładnie spełnia kryteria – to musisz sprawdzić samodzielnie.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Myślę o tym, jakie dofinansowania mogą być dostępne dla firmy hydraulicznej. Sprawdzam katalog naborów, aby znaleźć odpowiednie opcje.

Widzę, że w katalogu są różne nabory, ale żaden nie jest bezpośrednio skierowany do firm hydraulicznych. Jednak niektóre mogą być odpowiednie, jeśli firma zajmuje się na przykład efektywnością energetyczną, OZE, czy modernizacją systemów grzewczych.

Sprawdzam konkretne nabory. Na przykład "Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom" (2.4) jest otwarty do 2026-09-30, ale dotyczy renaturyzacji cieków wodnych, co może być związane z hydrauliką, ale głównie dla JST i organizacji ekologicznych. Nie dla typowej firmy hydraulicznej.

"Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła" (11.2) jest otwarty do 2026-09-30, ale dotyczy budowy magazynów ciepła na poziomie systemowym, a grupa docelowa to administracja publiczna, przedsiębiorstwa, służby publiczne. Może być odpowiedni, jeśli firma hydrauliczna współpracuje z takimi podmiotami.

"Pożyczki na rozwój turystyki" (1.5) są udzielane w trybie ciągłym, ale dotyczą branży turystycznej, nie hydrauliki.

"Polskie Mosty Technologiczne" (2.24) są otwarte od 2026-09-15 do 2026-10-30, ale dotyczą ekspansji zagranicznej MŚP z innowacyjnym produktem, co może być trudne dla typowej firmy hydraulicznej.

"Kadry nowoczesnej gospodarki" (1.3) ma kilka podnaborów, które są otwarte do różnych dat w 2026 i 2027 roku. Na przykład "Usługi rozwojowe 4.0" do 2026-08-31 (zamknięty), "Wsparcie firm w okresowych trudnościach" do 2026/2027 (nieokreślony), "Dostępność szansą na rozwój" do 2027-12-01, "Dostępność Dyrektywa EAA" do 2027-12-31, "Zielone rekomendacje" do 2027-12-01, "GOZ - to się opłaca" do 2027-01-01. Te mogą być odpowiednie dla firmy hydraulicznej, jeśli chce rozwijać kompetencje, wdrażać zielone rozwiązania, czy poprawiać dostępność.

"Ścieżka SMART" (1.1) jest otwarta od 2026-08-07 do 2026-10-16, ale dotyczy projektów B+R, co może być zaawansowane dla małej firmy hydraulicznej.

"Fundusz wsparcia technologii krytycznych" (5.1) dla biotechnologii, nie dla hydrauliki.

"Rozwój kompetencji cyfrowych" (1.9) jest otwarty od 2026-08-31 do 2026-11-16, ale dotyczy edukacji cyfrowej dorosłych, głównie dla JST i organizacji.

"Monitorowanie i identyfikacja potrzeb kompetencyjnych" (1.10) jest otwarty od 2026-09-03 do 2026-09-17 (zamknięty).

"Wysokiej jakości system włączenia społecznego" (4.13) jest otwarty od 2026-09-30 do 2026-11-30, ale dotyczy reintegracji w przedsiębiorstwach społecznych.

"Deinstytucjonalizacja długoterminowej opieki medycznej" (4.14) jest otwarty do 2026-09-30, ale dotyczy podmiotów leczniczych.

"Platformy startowe dla nowych pomysłów" (1.1) są otwarte w trybie ciągłym, ale dotyczą startupów w Polsce Wschodniej.

"Wzmocnienie cyberbezpieczeństwa" (4.1) jest otwarte od 31 lipca 2026 do 30 października 2026, ale dotyczy JST.

Podsumowując, najbardziej odpowiednie dla firmy hydraulicznej mogą być nabory z "Kadry nowoczesnej gospodarki" (1.3), które oferują wsparcie na rozwój kompetencji, zielone rekomendacje, GOZ, dostępność. Są one otwarte do 2027 roku. Ponadto "Polskie Mosty Technologiczne" (2.24) mogą być opcją, jeśli firma chce eksportować innowacyjne rozwiązania.

W odpowiedzi wymienię te nabory, które są otwarte i mogą być potencjalnie interesujące dla firmy hydraulicznej, z zastrzeżeniem, że warunki udziału trzeba sprawdzić w regulaminie.

</details>

**Ocena: ❌** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model): Dane - wpisuje dni tam gdzie podane są tylko miesiące** 

---

## R02 · representative · as-of 2026-09-25

**Pytanie:** Mam czas do końca października. Co się w tym miesiącu zamyka, żebym zdążył?

**Wzorzec:**
- musi zawierać: Ścieżka SMART — until 2026-10-16 (row 5)
- musi zawierać: Współfinansowanie działań EDIH — until 2026-10-28 (row 10)
- musi zawierać: Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury — until 2026-10-30 (row 20)
- musi zawierać: Polskie Mosty Technologiczne — until 2026-10-30 (row 24)
- NIE może zawierać: calls ending in September or November

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (61.35 s · 3630 tokenów wyjścia · finish=stop):

> Oto nabory, które zamykają się do końca października 2026 r. (od dziś, 25 września, do 31 października). Wszystkie są obecnie **otwarte**.
>
> ### Zamykające się we wrześniu (ostatnie dni)
> - **2.4 Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom** (FEnIKS)  
>   Koniec: **30 września 2026** (zostało 5 dni)  
>   Budżet: 100 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/nabory/24-adaptacja-do-zmian-klimatu-zapobieganie-kleskom-i-katastrofom-renaturyzacja/)
>
> - **11.2 Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła** (FEnIKS)  
>   Koniec: **30 września 2026**  
>   Budżet: 300 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/nabory/112-wspieranie-ochrony-krytycznej-infrastruktury-energetycznej-oraz-magazynow-ciepla-na-poziomie-systemowym/)
>
> - **2.1 Międzynarodowe Agendy Badawcze (Teaming)** (FENG)  
>   Koniec: **30 września 2026**  
>   Budżet: 60 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/strony/skorzystaj/nabory/#/domyslne=1/10502=3740) (link zostanie opublikowany po ogłoszeniu naboru)
>
> - **1.4 Rozwój systemu edukacji** (FERS)  
>   Koniec: **30 września 2026**  
>   Budżet: 28,1 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/nabory/14-rozwoj-systemu-edukacji-7/)
>
> - **4.14 Deinstytucjonalizacja długoterminowej opieki medycznej** (FERS)  
>   Koniec: **30 września 2026**  
>   Budżet: 28,8 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/nabory/414-deinstytucjonalizacja-dlugoterminowej-opieki-medycznej-standard-swiadczenia-dziennego-dla-osob-z-otepieniem/)
>
> ### Zamykające się w październiku
> - **1.1 Ścieżka SMART** (FENG)  
>   Koniec: **16 października 2026**  
>   Budżet: 350 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/nabory/sciezka-smart-projekty-realizowane-w-konsorcjach-1/)
>
> - **2.22 Współfinansowanie działań EDIH** (FENG)  
>   Koniec: **28 października 2026**  
>   Budżet: 20 mln zł  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/strony/skorzystaj/nabory/#/domyslne=1/10502=3740) (link zostanie opublikowany 15.09)
>
> - **4.1 Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych** (FERC)  
>   Koniec: **30 października 2026**  
>   Budżet: 269 mln zł  
>   Link do naboru będzie dostępny w dniu ogłoszenia
>
> - **2.24 Polskie Mosty Technologiczne** (FENG)  
>   Koniec: **30 października 2026**  
>   Budżet: do 150 tys. zł na projekt  
>   [Link do naboru](https://www.funduszeunijne.gov.pl/nabory/224-polskie-mosty-technologiczne-3/)  
>   [Dodatkowy link](https://sop.paih.gov.pl/#nabory)
>
> ---
>
> **Uwaga:** Warunki udziału w każdym naborze (kto może aplikować, jakie wydatki są kwalifikowane) musisz sprawdzić w regulaminie dostępnym pod podanymi linkami.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Myślę o pytaniu użytkownika. Dzisiejsza data to 2026-09-25, a użytkownik pyta o nabory zamykające się do końca października 2026. Muszę przejrzeć katalog i znaleźć wszystkie nabory, których data zakończenia przypada między 2026-09-25 a 2026-10-31.

Przeglądam arkusz "Aktualne_konkurencyjne". Szukam wierszy, gdzie data zakończenia jest w tym przedziale. Sprawdzam każdy wiersz:

- Wiersz 2: 1.5 Ochrona przyrody – data zakończenia 2026-09-21. To już zamknięte, bo 21.09 jest przed dzisiejszą datą.
- Wiersz 3: 2.4 Adaptacja do zmian klimatu – data zakończenia 2026-09-30. To jest w przedziale, ale 30.09 to jeszcze wrzesień, nie październik. Użytkownik pyta o "do końca października", więc wrzesień też się liczy, ale 30.09 jest w tym miesiącu, więc to pasuje.
- Wiersz 4: 11.2 Wspieranie ochrony krytycznej infrastruktury – data zakończenia 2026-09-30. To samo, pasuje.
- Wiersz 5: 1.1 Ścieżka SMART – data zakończenia 2026-10-16. To jest w październiku, pasuje.
- Wiersz 6: 2.1 Międzynarodowe Agendy Badawcze – data zakończenia 2026-09-30. Pasuje.
- Wiersz 7: 2.12 Granty na eurogranty – data zakończenia 2026-09-03. To już zamknięte.
- Wiersz 8: 2.17 Rozwój oferty klastrów (Krajowe Klastry Kluczowe) – data zakończenia 2026-11-04. To po październiku, nie pasuje.
- Wiersz 9: 2.17 Rozwój oferty klastrów (Ponadregionalne Klastry Kluczowe) – data zakończenia 2026-11-10. Nie pasuje.
- Wiersz 10: 2.22 Współfinansowanie działań EDIH – data zakończenia 2026-10-28. Pasuje.
- Wiersz 11: 2.28 Startup Booster Poland – data zakończenia 2026-09-08. Zamknięte.
- Wiersz 12: 5.1 Fundusz wsparcia technologii krytycznych (BIOTECH) ścieżka innowacyjność – data zakończenia 2026-09-07. Zamknięte.
- Wiersz 13: 5.1 Fundusz wsparcia technologii krytycznych (BIOTECH) ścieżka strategiczna – data zakończenia 2026-09-16. Zamknięte.
- Wiersz 14: 1.4 Rozwój systemu edukacji – data zakończenia 2026-09-30. Pasuje.
- Wiersz 15: 1.9 Rozwój kompetencji cyfrowych – data zakończenia 2026-11-16. Nie pasuje.
- Wiersz 16: 1.10 Monitorowanie i identyfikacja potrzeb kompetencyjnych – data zakończenia 2026-09-17. Zamknięte.
- Wiersz 17: 4.13 Wysokiej jakości system włączenia społecznego – data zakończenia 2026-11-30. Nie pasuje.
- Wiersz 18: 4.14 Deinstytucjonalizacja długoterminowej opieki medycznej – data zakończenia 2026-09-30. Pasuje.
- Wiersz 19: 1.1 Platformy startowe dla nowych pomysłów Komponent II a – data zakończenia 2026-09-17. Zamknięte.
- Wiersz 20: 4.1 Wzmocnienie cyberbezpieczeństwa – data zakończenia 30 października 2026. Pasuje.
- Wiersz 22: 1.1 Platformy startowe dla nowych pomysłów - wsparcie ekspertów – data zakończenia pusta, opis "Zgłoszenia pomysłów do Platform startowych są prowadzone w rundach." – status nieokreślony, ale nie ma konkretnej daty zakończenia w październiku.
- Wiersz 23: 1.5 Pożyczki na rozwój turystyki – "Pożyczki udzielane w trybie ciągłym" – brak daty zakończenia, status nieokreślony.
- Wiersz 24: 2.24 Polskie Mosty Technologiczne – data zakończenia 2026-10-30. Pasuje.
- Wiersz 25: 1.3 Kadry nowoczesnej gospodarki – Akademia HR – data zakończenia 2026-11-30. Nie pasuje.
- Wiersz 26: 1.3 Kadry nowoczesnej gospodarki – Usługi rozwojowe 4.0 – data zakończenia 2026-08-31. Zamknięte.
- Wiersz 27: 1.3 Kadry nowoczesnej gospodarki – Wsparcie firm w okresowych trudnościach – data zakończenia "2026/2027" – status nieokreślony, ale nie ma konkretnej daty w październiku.
- Wiersz 28: 1.3 Kadry nowoczesnej gospodarki – Dostępność szansą na rozwój – data zakończenia 2027-12-01. Nie pasuje.
- Wiersz 29: 1.3 Kadry nowoczesnej gospodarki – Dostępność Dyrektywa EAA – data zakończenia 2027-12-31. Nie pasuje.
- Wiersz 30: 1.3 Kadry nowoczesnej gospodarki – Zielone rekomendacje – data zakończenia 2027-12-01. Nie pasuje.
- Wiersz 31: 1.3 Kadry nowoczesnej gospodarki – GOZ - to się opłaca – data zakończenia 2027-01-01. Nie pasuje.

Teraz sprawdzam arkusz "NOWE_konkurencyjne". Szukam wierszy z datą zakończenia w przedziale 2026-09-25 do 2026-10-31:

- Wiersz 2: 1.9 Rozwój kompetencji cyfrowych – data zakończenia 2026-11-16. Nie pasuje.
- Wiersz 3: 1.10 Monitorowanie i identyfikacja potrzeb kompetencyjnych – data zakończenia 2026-09-17. Zamknięte.
- Wiersz 4: 4.13 Wysokiej jakości system włączenia społecznego – data zakończenia 2026-11-30. Nie pasuje.
- Wiersz 5: 2.1 Międzynarodowe Agendy Badawcze – data zakończenia 2026-09-30. Pasuje.
- Wiersz 6: 2.17 Rozwój oferty klastrów (Krajowe Klastry Kluczowe) – data zakończenia 2026-11-04. Nie pasuje.
- Wiersz 7: 2.17 Rozwój oferty klastrów (Ponadregionalne Klastry Kluczowe) – data zakończenia 2026-11-10. Nie pasuje.
- Wiersz 8: 2.22 Współfinansowanie działań EDIH – data zakończenia 2026-10-28. Pasuje.

Zbieram wszystkie nabory, które są otwarte (data rozpoczęcia przed lub równa dzisiejszej) i zamykają się do 31 października 2026. Sprawdzam daty rozpoczęcia:

- 2.4 Adaptacja do zmian klimatu: start 2026-05-29, koniec 2026-09-30 – otwarty, zamyka się 30.09.
- 11.2 Wspieranie ochrony krytycznej infrastruktury: start 2026-05-29, koniec 2026-09-30 – otwarty, zamyka się 30.09.
- 1.1 Ścieżka SMART: start 2026-08-07, koniec 2026-10-16 – otwarty, zamyka się 16.10.
- 2.1 Międzynarodowe Agendy Badawcze: start 2026-09-01, koniec 2026-09-30 – otwarty, zamyka się 30.09.
- 2.22 Współfinansowanie działań EDIH: start 2026-09-24, koniec 2026-10-28 – otwarty, zamyka się 28.10.
- 1.4 Rozwój systemu edukacji: start 2026-04-01, koniec 2026-09-30 – otwarty, zamyka się 30.09.
- 4.14 Deinstytucjonalizacja długoterminowej opieki medycznej: start 2026-06-09, koniec 2026-09-30 – otwarty, zamyka się 30.09.
- 4.1 Wzmocnienie cyberbezpieczeństwa: start 31 lipca 2026, koniec 30 października 2026 – otwarty, zamyka się 30.10.
- 2.24 Polskie Mosty Technologiczne: start 2026-09-15, koniec 2026-10-30 – otwarty, zamyka się 30.10.

Uwzględniam też nabory z "NOWE_konkurencyjne", ale te same już są w "Aktualne_konkurencyjne" (2.1 i 2.22), więc nie dubluję.

Teraz formatuję odpowiedź. Dla każdego naboru podaję nazwę, status (otwarty), datę zakończenia i link. Jeśli data zakończenia to 30.09, to jest to za 5 dni od dzisiaj (25.09), więc warto zaznaczyć, że to ostatnie dni. Użytkownik pytał o "do końca października", więc skupiam się na tych, które kończą się w październiku, ale też wrzesień jest w tym okresie, więc wszystkie pasują.

Wymienię je w kolejności dat zakończenia.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## R03 · representative · as-of 2026-09-25

**Pytanie:** Który otwarty nabór ma największy budżet?

**Wzorzec:**
- musi zawierać: Ścieżka SMART — 350 mln zł (row 5)
- NIE może zawierać: a call whose budget is text (e.g. 'Budżet do ustalenia', 'do 150 tys. zł') compared as a number

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (48.64 s · 2983 tokenów wyjścia · finish=stop):

> Na podstawie katalogu naborów, na dzień 2026-09-25 otwartym naborem z największym budżetem jest:
>
> **Ścieżka SMART** (działanie 1.1, program FENG)  
> - Status: **otwarty** (do 16 października 2026)  
> - Budżet: **350 mln zł**  
> - Link: [https://www.funduszeunijne.gov.pl/nabory/sciezka-smart-projekty-realizowane-w-konsorcjach-1/](https://www.funduszeunijne.gov.pl/nabory/sciezka-smart-projekty-realizowane-w-konsorcjach-1/)
>
> Szczegółowe warunki udziału należy sprawdzić w regulaminie naboru.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Na podstawie katalogu, muszę znaleźć otwarte nabory na dzień 2026-09-25 i określić, który ma największy budżet.

Najpierw przeglądam arkusz "Aktualne_konkurencyjne" i "NOWE_konkurencyjne". Szukam naborów, które są otwarte (data rozpoczęcia <= 2026-09-25 <= data zakończenia).

Z arkusza "Aktualne_konkurencyjne":

- row 2: 1.5 Ochrona przyrody... start 2026-06-15, end 2026-09-21. 2026-09-25 > 2026-09-21, więc zamknięty.
- row 3: 2.4 Adaptacja do zmian klimatu... start 2026-05-29, end 2026-09-30. 2026-09-25 <= 2026-09-30, więc otwarty. Budżet: 100 mln zł.
- row 4: 11.2 Wspieranie ochrony krytycznej infrastruktury... start 2026-05-29, end 2026-09-30. Otwarty. Budżet: 300 mln zł.
- row 5: 1.1 Ścieżka SMART start 2026-08-07, end 2026-10-16. Otwarty. Budżet: 350 mln zł.
- row 6: 2.1 Międzynarodowe Agendy Badawcze start 2026-09-01, end 2026-09-30. Otwarty. Budżet: 60 mln zł.
- row 7: 2.12 Granty na eurogranty start 2025-08-12, end 2026-09-03. 2026-09-25 > 2026-09-03, zamknięty.
- row 8: 2.17 Rozwój oferty klastrów dla firm (Krajowe Klastry Kluczowe) start 2026-09-16, end 2026-11-04. Otwarty. Budżet: "Budżet do ustalenia w ramach kolejnej aktualizacji harmonogramu naborów" – nie jest liczbą, więc nie mogę porównać.
- row 9: 2.17 Rozwój oferty klastrów dla firm (Ponadregionalne Klastry Kluczowe) start 2026-09-22, end 2026-11-10. Otwarty. Budżet: "Budżet do ustalenia..." – nie liczba.
- row 10: 2.22 Współfinansowanie działań EDIH start 2026-09-24, end 2026-10-28. Otwarty. Budżet: 20 mln zł.
- row 11: 2.28 Startup Booster Poland start 2026-07-14, end 2026-09-08. 2026-09-25 > 2026-09-08, zamknięty.
- row 12: 5.1 Fundusz wsparcia technologii krytycznych (BIOTECH) ścieżka innowacyjność start 2026-07-06, end 2026-09-07. Zamknięty.
- row 13: 5.1 Fundusz wsparcia technologii krytycznych (BIOTECH) ścieżka strategiczna start 2026-07-13, end 2026-09-16. Zamknięty.
- row 14: 1.4 Rozwój systemu edukacji start 2026-04-01, end 2026-09-30. Otwarty. Budżet: 28.1 mln zł.
- row 15: 1.9 Rozwój kompetencji cyfrowych start 2026-08-31, end 2026-11-16. Otwarty. Budżet: 160.5 mln zł.
- row 16: 1.10 Monitorowanie i identyfikacja potrzeb kompetencyjnych start 2026-09-03, end 2026-09-17. Zamknięty.
- row 17: 4.13 Wysokiej jakości system włączenia społecznego start 2026-09-30, end 2026-11-30. 2026-09-25 < 2026-09-30, więc jeszcze nie ruszył (start później niż dzisiaj).
- row 18: 4.14 Deinstytucjonalizacja długoterminowej opieki medycznej start 2026-06-09, end 2026-09-30. Otwarty. Budżet: 28.8 mln zł.
- row 19: 1.1 Platformy startowe dla nowych pomysłów Komponent II a start 2026-06-30, end 2026-09-17. Zamknięty.
- row 20: 4.1 Wzmocnienie cyberbezpieczeństwa... start "31 lipca 2026" (czyli 2026-07-31), end "30 października 2026" (2026-10-30). Otwarty. Budżet: 269 mln zł.
- row 22: 1.1 Platformy startowe dla nowych pomysłów - wsparcie ekspertów – data rozpoczęcia "Zgłoszenia pomysłów do Platform startowych są prowadzone w rundach." – brak konkretnej daty, więc status nieokreślony. Budżet: "Wsparcie ekspertów" – nie liczba.
- row 23: 1.5 Pożyczki na rozwój turystyki – "Pożyczki udzielane w trybie ciągłym" – brak daty zakończenia, więc status nieokreślony. Budżet: "Budżet jednej pozyczki może wynieść 1 mln zł" – to nie jest budżet konkursu, tylko maksymalna kwota pożyczki.
- row 24: 2.24 Polskie Mosty Technologiczne start 2026-09-15, end 2026-10-30. Otwarty. Budżet: "do 150 tys. zł" – to nie jest budżet w mln zł, tylko maksymalna kwota wsparcia na projekt. W kolumnie budżet konkursu jest napisane "do 150 tys. zł", co nie jest liczbą w mln zł, więc nie mogę tego porównać jako liczby.
- row 25-31: 1.3 Kadry nowoczesnej gospodarki – różne podnabory, ale daty zakończenia są w przyszłości (2026-11-30, 2026-08-31, 2026/2027, 2027-12-01 itd.). Sprawdzam każdy:
  - row 25: Akademia HR start 2024-03-25, end 2026-11-30. Otwarty. Budżet: "Wsparcie wyniesie do 80% wartości projektu" – nie liczba.
  - row 26: Usługi rozwojowe 4.0 start 2024-02-12, end 2026-08-31. 2026-09-25 > 2026-08-31, zamknięty.
  - row 27: Wsparcie firm w okresowych trudnościach start 2024-06-24, end "2026/2027" – to nie jest konkretna data, więc status nieokreślony. Budżet: "do 154 384,00 zł" – nie liczba w mln.
  - row 28: Dostępność szansą na rozwój start 2025-02-01, end 2027-12-01. Otwarty. Budżet: "Dofinansowanie 100 %" – nie liczba.
  - row 29: Dostępność Dyrektywa EAA start 2025-02-25, end 2027-12-31. Otwarty. Budżet: "Dofinansowanie 100 %" – nie liczba.
  - row 30: Zielone rekomendacje start 2025-06-01, end 2027-12-01. Otwarty. Budżet: "Wsparcie wyniesie do 80% wartości projektu" – nie liczba.
  - row 31: GOZ - to się opłaca start 2024-05-01, end 2027-01-01. Otwarty. Budżet: "Dofinansowanie 100 %" – nie liczba.

Z arkusza "NOWE_konkurencyjne":
- row 2: 1.9 Rozwój kompetencji cyfrowych – to samo co w Aktualne row 15, ale data start 2026-08-31, end 2026-11-16. Otwarty. Budżet: 160.5 mln zł.
- row 3: 1.10 Monitorowanie i identyfikacja potrzeb – start 2026-09-03, end 2026-09-17. Zamknięty.
- row 4: 4.13 Wysokiej jakości system włączenia społecznego – start 2026-09-30, end 2026-11-30. Jeszcze nie ruszył.
- row 5: 2.1 Międzynarodowe Agendy Badawcze – to samo co w Aktualne row 6, otwarty, budżet 60 mln.
- row 6: 2.17 Rozwój oferty klastrów (Krajowe) – to samo co w Aktualne row 8, otwarty, budżet nieokreślony.
- row 7: 2.17 Rozwój oferty klastrów (Ponadregionalne) – to samo co w Aktualne row 9, otwarty, budżet nieokreślony.
- row 8: 2.22 Współfinansowanie działań EDIH – to samo co w Aktualne row 10, otwarty, budżet 20 mln.

Teraz zestawiam otwarte nabory z budżetem liczbowym (w mln zł):
- 2.4 Adaptacja do zmian klimatu: 100 mln
- 11.2 Wspieranie ochrony krytycznej infrastruktury: 300 mln
- 1.1 Ścieżka SMART: 350 mln
- 2.1 Międzynarodowe Agendy Badawcze: 60 mln
- 2.22 Współfinansowanie działań EDIH: 20 mln
- 1.4 Rozwój systemu edukacji: 28.1 mln
- 1.9 Rozwój kompetencji cyfrowych: 160.5 mln
- 4.14 Deinstytucjonalizacja długoterminowej opieki medycznej: 28.8 mln
- 4.1 Wzmocnienie cyberbezpieczeństwa: 269 mln

Największy budżet liczbowy to 350 mln zł (Ścieżka SMART). Sprawdzam, czy są jakieś inne z większym budżetem, ale nie. 350 > 300 > 269 > 160.5 > 100 > 60 > 28.8 > 28.1 > 20.

Zatem otwarty nabór z największym budżetem to "1.1 Ścieżka SMART" z budżetem 350 mln zł.

Uwzględniam, że są też nabory z budżetem nieokreślonym liczbowo, ale nie mogę ich porównać.

Odpowiedź: Ścieżka SMART (FENG), otwarty do 2026-10-16, budżet 350 mln zł, link: https://www.funduszeunijne.gov.pl/nabory/sciezka-smart-projekty-realizowane-w-konsorcjach-1/

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## D04 · diagnostic · as-of 2026-09-25

**Pytanie:** Ile naborów jest teraz otwartych?

**Wzorzec:**
- musi zawierać: 17 open
- musi zawierać: 3 without a determined end date (rows 22, 23, 27)
- musi zawierać: 1 not started yet (row 17)
- NIE może zawierać: a count that includes duplicates from sheet NOWE_konkurencyjne

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (70.46 s · 4395 tokenów wyjścia · finish=stop):

> Obecnie otwartych jest **22 naborów** (licząc wszystkie wiersze z obu arkuszy katalogu, które mają daty rozpoczęcia i zakończenia mieszczące dzisiejszą datę 2026-09-25).

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Zgodnie z dzisiejszą datą 2026-09-25, muszę przejrzeć katalog i określić status każdego naboru. Katalog składa się z dwóch arkuszy: "Aktualne_konkurencyjne" i "NOWE_konkurencyjne". Sprawdzę każdy wiersz.

Zaczynam od arkusza "Aktualne_konkurencyjne":

1. row 2: 1.5 Ochrona przyrody... Data rozpoczęcia 2026-06-15, zakończenia 2026-09-21. Dziś 2026-09-25, po 2026-09-21, więc zamknięty.

2. row 3: 2.4 Adaptacja do zmian klimatu... Data rozpoczęcia 2026-05-29, zakończenia 2026-09-30. Dziś 2026-09-25, mieści się między 2026-05-29 a 2026-09-30, więc otwarty.

3. row 4: 11.2 Wspieranie ochrony krytycznej infrastruktury... Data rozpoczęcia 2026-05-29, zakończenia 2026-09-30. Dziś 2026-09-25, otwarty.

4. row 5: 1.1 Ścieżka SMART... Data rozpoczęcia 2026-08-07, zakończenia 2026-10-16. Dziś 2026-09-25, otwarty.

5. row 6: 2.1 Międzynarodowe Agendy Badawcze (Teaming)... Data rozpoczęcia 2026-09-01, zakończenia 2026-09-30. Dziś 2026-09-25, otwarty.

6. row 7: 2.12 Granty na eurogranty... Data rozpoczęcia 2025-08-12, zakończenia 2026-09-03. Dziś 2026-09-25, po 2026-09-03, więc zamknięty.

7. row 8: 2.17 Rozwój oferty klastrów dla firm (Krajowe Klastry Kluczowe)... Data rozpoczęcia 2026-09-16, zakończenia 2026-11-04. Dziś 2026-09-25, otwarty.

8. row 9: 2.17 Rozwój oferty klastrów dla firm (Ponadregionalne Klastry Kluczowe)... Data rozpoczęcia 2026-09-22, zakończenia 2026-11-10. Dziś 2026-09-25, otwarty.

9. row 10: 2.22 Współfinansowanie działań EDIH... Data rozpoczęcia 2026-09-24, zakończenia 2026-10-28. Dziś 2026-09-25, otwarty.

10. row 11: 2.28 Startup Booster Poland... Data rozpoczęcia 2026-07-14, zakończenia 2026-09-08. Dziś 2026-09-25, po 2026-09-08, więc zamknięty.

11. row 12: 5.1 Fundusz wsparcia technologii krytycznych (BIOTECH) ścieżka innowacyjność... Data rozpoczęcia 2026-07-06, zakończenia 2026-09-07. Dziś 2026-09-25, zamknięty.

12. row 13: 5.1 Fundusz wsparcia technologii krytycznych (BIOTECH) ścieżka strategiczna niezależność... Data rozpoczęcia 2026-07-13, zakończenia 2026-09-16. Dziś 2026-09-25, zamknięty.

13. row 14: 1.4 Rozwój systemu edukacji... Data rozpoczęcia 2026-04-01, zakończenia 2026-09-30. Dziś 2026-09-25, otwarty.

14. row 15: 1.9 Rozwój kompetencji cyfrowych... Data rozpoczęcia 2026-08-31, zakończenia 2026-11-16. Dziś 2026-09-25, otwarty.

15. row 16: 1.10 Monitorowanie i identyfikacja potrzeb kompetencyjnych... Data rozpoczęcia 2026-09-03, zakończenia 2026-09-17. Dziś 2026-09-25, zamknięty.

16. row 17: 4.13 Wysokiej jakości system włączenia społecznego... Data rozpoczęcia 2026-09-30, zakończenia 2026-11-30. Dziś 2026-09-25, data rozpoczęcia 2026-09-30 jest późniejsza niż dzisiejsza, więc jeszcze nie ruszył.

17. row 18: 4.14 Deinstytucjonalizacja długoterminowej opieki medycznej... Data rozpoczęcia 2026-06-09, zakończenia 2026-09-30. Dziś 2026-09-25, otwarty.

18. row 19: 1.1 Platformy startowe dla nowych pomysłów Komponent II a... Data rozpoczęcia 2026-06-30, zakończenia 2026-09-17. Dziś 2026-09-25, zamknięty.

19. row 20: 4.1 Wzmocnienie cyberbezpieczeństwa... Data rozpoczęcia "31 lipca 2026", zakończenia "30 października 2026". To są daty w formacie tekstowym, ale można je interpretować jako 2026-07-31 i 2026-10-30. Dziś 2026-09-25, mieści się między, więc otwarty.

20. row 22: 1.1 Platformy startowe dla nowych pomysłów - wsparcie ekspertów... Data rozpoczęcia "Zgłoszenia pomysłów do Platform startowych są prowadzone w rundach." Brak konkretnej daty zakończenia. Status nieokreślony, bo nie ma daty zakończenia. Zacytuję dosłownie.

21. row 23: 1.5 Pożyczki na rozwój turystyki... Data rozpoczęcia "Pożyczki udzielane w trybie ciągłym", brak daty zakończenia. Status nieokreślony.

22. row 24: 2.24 Polskie Mosty Technologiczne... Data rozpoczęcia 2026-09-15, zakończenia 2026-10-30. Dziś 2026-09-25, otwarty.

23. row 25: 1.3 Kadry nowoczesnej gospodarki - Akademia HR... Data rozpoczęcia 2024-03-25, zakończenia 2026-11-30. Dziś 2026-09-25, otwarty.

24. row 26: 1.3 Kadry nowoczesnej gospodarki - Usługi rozwojowe 4.0... Data rozpoczęcia 2024-02-12, zakończenia 2026-08-31. Dziś 2026-09-25, zamknięty.

25. row 27: 1.3 Kadry nowoczesnej gospodarki - Wsparcie firm w okresowych trudnościach... Data rozpoczęcia 2024-06-24, zakończenia "2026/2027". To jest przedział lat, a dzisiejsza data 2026-09-25 mieści się w 2026, więc status nieokreślony. Zacytuję.

26. row 28: 1.3 Kadry nowoczesnej gospodarki - Dostępność szansą na rozwój... Data rozpoczęcia 2025-02-01, zakończenia 2027-12-01. Dziś 2026-09-25, otwarty.

27. row 29: 1.3 Kadry nowoczesnej gospodarki - Dostępność Dyrektywa EAA... Data rozpoczęcia 2025-02-25, zakończenia 2027-12-31. Dziś 2026-09-25, otwarty.

28. row 30: 1.3 Kadry nowoczesnej gospodarki - Zielone rekomendacje... Data rozpoczęcia 2025-06-01, zakończenia 2027-12-01. Dziś 2026-09-25, otwarty.

29. row 31: 1.3 Kadry nowoczesnej gospodarki - GOZ - to się opłaca... Data rozpoczęcia 2024-05-01, zakończenia 2027-01-01. Dziś 2026-09-25, otwarty.

Teraz arkusz "NOWE_konkurencyjne":

1. row 2: 1.9 Rozwój kompetencji cyfrowych... Data rozpoczęcia 2026-08-31, zakończenia 2026-11-16. Dziś 2026-09-25, otwarty.

2. row 3: 1.10 Monitorowanie i identyfikacja potrzeb kompetencyjnych... Data rozpoczęcia 2026-09-03, zakończenia 2026-09-17. Dziś 2026-09-25, zamknięty.

3. row 4: 4.13 Wysokiej jakości system włączenia społecznego... Data rozpoczęcia 2026-09-30, zakończenia 2026-11-30. Dziś 2026-09-25, jeszcze nie ruszył.

4. row 5: 2.1 Międzynarodowe Agendy Badawcze (Teaming)... Data rozpoczęcia 2026-09-01, zakończenia 2026-09-30. Dziś 2026-09-25, otwarty.

5. row 6: 2.17 Rozwój oferty klastrów dla firm (Krajowe Klastry Kluczowe)... Data rozpoczęcia 2026-09-16, zakończenia 2026-11-04. Dziś 2026-09-25, otwarty.

6. row 7: 2.17 Rozwój oferty klastrów dla firm (Ponadregionalne Klastry Kluczowe)... Data rozpoczęcia 2026-09-22, zakończenia 2026-11-10. Dziś 2026-09-25, otwarty.

7. row 8: 2.22 Współfinansowanie działań EDIH... Data rozpoczęcia 2026-09-24, zakończenia 2026-10-28. Dziś 2026-09-25, otwarty.

Teraz muszę policzyć, ile naborów jest otwartych. Z arkusza "Aktualne_konkurencyjne" otwarte to:

- row 3: 2.4 Adaptacja do zmian klimatu
- row 4: 11.2 Wspieranie ochrony krytycznej infrastruktury
- row 5: 1.1 Ścieżka SMART
- row 6: 2.1 Międzynarodowe Agendy Badawcze (Teaming)
- row 8: 2.17 Rozwój oferty klastrów (Krajowe Klastry Kluczowe)
- row 9: 2.17 Rozwój oferty klastrów (Ponadregionalne Klastry Kluczowe)
- row 10: 2.22 Współfinansowanie działań EDIH
- row 14: 1.4 Rozwój systemu edukacji
- row 15: 1.9 Rozwój kompetencji cyfrowych
- row 18: 4.14 Deinstytucjonalizacja długoterminowej opieki medycznej
- row 20: 4.1 Wzmocnienie cyberbezpieczeństwa
- row 24: 2.24 Polskie Mosty Technologiczne
- row 25: 1.3 Kadry nowoczesnej gospodarki - Akademia HR
- row 28: 1.3 Kadry nowoczesnej gospodarki - Dostępność szansą na rozwój
- row 29: 1.3 Kadry nowoczesnej gospodarki - Dostępność Dyrektywa EAA
- row 30: 1.3 Kadry nowoczesnej gospodarki - Zielone rekomendacje
- row 31: 1.3 Kadry nowoczesnej gospodarki - GOZ - to się opłaca

To daje 17 naborów otwartych z arkusza "Aktualne_konkurencyjne".

Z arkusza "NOWE_konkurencyjne" otwarte to:

- row 2: 1.9 Rozwój kompetencji cyfrowych
- row 5: 2.1 Międzynarodowe Agendy Badawcze (Teaming)
- row 6: 2.17 Rozwój oferty klastrów (Krajowe Klastry Kluczowe)
- row 7: 2.17 Rozwój oferty klastrów (Ponadregionalne Klastry Kluczowe)
- row 8: 2.22 Współfinansowanie działań EDIH

To daje 5 naborów otwartych z arkusza "NOWE_konkurencyjne".

Razem: 17 + 5 = 22.

Ale uwaga: niektóre nabory mogą się powtarzać między arkuszami? Sprawdzam: np. 1.9 Rozwój kompetencji cyfrowych występuje w obu arkuszach (row 15 w Aktualne i row 2 w NOWE). To jest ten sam nabór? W arkuszu Aktualne ma daty 2026-08-31 do 2026-11-16, a w NOWE też 2026-08-31 do 2026-11-16. Wygląda na duplikat. Podobnie 1.10 Monitorowanie... w Aktualne row 16 (2026-09-03 do 2026-09-17) i w NOWE row 3 (te same daty) - ale ten jest zamknięty, więc nie wpływa na liczbę otwartych. 4.13 Wysokiej jakości system włączenia społecznego w Aktualne row 17 (2026-09-30 do 2026-11-30) i w NOWE row 4 (te same daty) - jeszcze nie ruszył. 2.1 Międzynarodowe Agendy Badawcze w Aktualne row 6 (2026-09-01 do 2026-09-30) i w NOWE row 5 (te same daty) - otwarty w obu. 2.17 Krajowe Klastry Kluczowe w Aktualne row 8 (2026-09-16 do 2026-11-04) i w NOWE row 6 (te same daty) - otwarty w obu. 2.17 Ponadregionalne Klastry Kluczowe w Aktualne row 9 (2026-09-22 do 2026-11-10) i w NOWE row 7 (te same daty) - otwarty w obu. 2.22 Współfinansowanie działań EDIH w Aktualne row 10 (2026-09-24 do 2026-10-28) i w NOWE row 8 (te same daty) - otwarty w obu.

Zatem te nabory są zduplikowane. W katalogu są dwa arkusze, ale to ten sam nabór? W arkuszu "Aktualne_konkurencyjne" są one wymienione, a w "NOWE_konkurencyjne" też. Pytanie użytkownika: "Ile naborów jest teraz otwartych?" - jeśli liczymy unikalne nabory, to duplikaty należy liczyć raz. Ale w katalogu są one zapisane jako osobne wiersze w różnych arkuszach. Reguły mówią: "Katalog obejmuje wyłącznie programy krajowe, bez programów regionalnych. Korzystasz z niego po to, żeby każda odpowiedź opierała się na faktach z arkusza". Nie ma instrukcji, aby unikać duplikatów. W arkuszu "Aktualne_konkurencyjne" i "NOWE_konkurencyjne" to osobne zestawienia. Być może "NOWE" to nowe nabory, które jeszcze nie były wcześniej, ale widać, że niektóre się pokrywają. Dla bezpieczeństwa, policzę wszystkie wiersze z obu arkuszy, które są otwarte, bez usuwania duplikatów, bo tak są przedstawione w danych.

Zatem z Aktualne: 17 otwartych, z NOWE: 5 otwartych, razem 22.

Ale sprawdźmy jeszcze raz, czy wszystkie wymienione przeze mnie są faktycznie otwarte. Dla row 20 w Aktualne: data rozpoczęcia "31 lipca 2026" - to jest 2026-07-31, data zakończenia "30 października 2026" - 2026-10-30. Dziś 2026-09-25, więc otwarty. OK.

Dla row 22 w Aktualne: "Zgłoszenia pomysłów do Platform startowych są prowadzone w rundach." - brak daty zakończenia, więc status nieokreślony, nie otwarty.

Dla row 23: "Pożyczki udzielane w trybie ciągłym" - brak daty zakończenia, nieokreślony.

Dla row 27: data zakończenia "2026/2027" - to przedział, a dziś 2026-09-25 mieści się w 2026, więc nieokreślony.

Zatem te trzy nie są liczone jako otwarte.

Podsumowując: liczba otwartych naborów to 22.

Odpowiem: "Obecnie otwartych jest 22 naborów." I ewentualnie wymienię je, ale pytanie brzmi tylko o liczbę.

</details>

**Ocena:❌** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):model/logika - duplikaty z arkuszy - model w span prawidłowo rozpoznał że to mogą być duplikaty ale dla bezpieczeństwa je dodał do siebie bo miały minimalne różnice** 

---

## D05 · diagnostic · as-of 2026-09-25

**Pytanie:** Do kiedy mogę złożyć wniosek w naborze na cyberbezpieczeństwo?

**Wzorzec:**
- musi zawierać: 30 października 2026 (row 20)
- musi zawierać: open

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (10.89 s · 316 tokenów wyjścia · finish=stop):

> Nabór **4.1 Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych** (FERC) jest **otwarty**. Możesz składać wnioski do **30 października 2026** (włącznie).
>
> Link do naboru (strona ogłoszenia):  
> https://www.funduszeunijne.gov.pl/nabory/41-wzmocnienie-cyberbezpieczenstwa-oraz-rozwoj-odpornej-infrastruktury-przetwarzania-danych/

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Z pytania wynika, że użytkownik pyta o nabór na cyberbezpieczeństwo. W katalogu znajduję jeden nabór związany z cyberbezpieczeństwem: w arkuszu "Aktualne_konkurencyjne", wiersz 20, działanie 4.1 "Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych" z programu FERC. Data rozpoczęcia: 31 lipca 2026, data zakończenia: 30 października 2026. Dzisiejsza data to 2026-09-25, więc nabór jest otwarty. Odpowiadam: nabór otwarty, data zakończenia 30 października 2026, podaję link.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## D06 · diagnostic · as-of 2026-09-25

**Pytanie:** Do kiedy trwa nabór na pożyczki na rozwój turystyki?

**Wzorzec:**
- musi zawierać: status undetermined — continuous intake, no end date in the data (row 23)
- musi zawierać: the sheet's wording quoted
- musi zawierać: the call's link
- NIE może zawierać: an invented end date

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (17.83 s · 780 tokenów wyjścia · finish=stop):

> Nabór na **Pożyczki na rozwój turystyki** (działanie 1.5, program FEPW) jest prowadzony **w trybie ciągłym** – nie ma określonej daty zakończenia. W katalogu widnieje zapis: *„Pożyczki udzielane w trybie ciągłym”*.
>
> Szczegóły znajdziesz pod linkiem:  
> [https://www.bgk.pl/programy-i-fundusze/fundusze/fundusze-europejskie-dla-polski-wschodniej-2021-2027/pozyczka-na-rozwoj-turystyki/](https://www.bgk.pl/programy-i-fundusze/fundusze/fundusze-europejskie-dla-polski-wschodniej-2021-2027/pozyczka-na-rozwoj-turystyki/)
>
> Warunki udziału sprawdź w regulaminie dostępnym u regionalnych pośredników finansowych.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Z pytania wynika, że użytkownik chce wiedzieć, do kiedy trwa nabór na pożyczki na rozwój turystyki. Sprawdzam w katalogu. W arkuszu "Aktualne_konkurencyjne" w wierszu 23 (row 23) znajduje się wpis: "1.5 | Pożyczki na rozwój turystyki | FEPW | konkurencyjny | Pożyczki udzielane w trybie ciągłym |  | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średnich działających w branży turystycznej... | Pożyczki udzielane są przez regionalnych pośredników finansowych | Budżet jednej pozyczki może wynieść 1 mln zł | https://www.bgk.pl/programy-i-fundusze/fundusze/fundusze-europejskie-dla-polski-wschodniej-2021-2027/pozyczka-na-rozwoj-turystyki/ | MŚP, które: - działają w branży turystycznej i pokrewnych...".

W kolumnie "Data zakończenia konkursu" jest puste pole. W kolumnie "Data rozpoczęcia konkursu (nabór wniosków)" jest napisane "Pożyczki udzielane w trybie ciągłym". Oznacza to, że nabór jest ciągły, bez określonej daty zakończenia. Zgodnie z regułami, jeśli brak daty zakończenia, status jest "nieokreślony" i należy zacytować dosłownie, co jest w arkuszu, oraz podać link.

Dzisiejsza data to 2026-09-25. Ponieważ nabór jest ciągły, nie ma daty zakończenia, więc jest otwarty w sensie ciągłym. W odpowiedzi należy podać, że nabór trwa w trybie ciągłym, bez określonej daty zakończenia, i podać link.

Użytkownik pyta "do kiedy trwa", więc odpowiadam, że nie ma określonej daty zakończenia – nabór jest prowadzony w trybie ciągłym. Cytuję z arkusza: "Pożyczki udzielane w trybie ciągłym". Podaję link.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## D07 · diagnostic · as-of 2026-09-25

**Pytanie:** Do kiedy trwa nabór „Kadry nowoczesnej gospodarki”?

**Wzorzec:**
- musi zawierać: there are 7 calls under this name (rows 25–31), with different end dates
- NIE może zawierać: a single end date given as the only answer

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (42.72 s · 1693 tokenów wyjścia · finish=stop):

> Nabór „Kadry nowoczesnej gospodarki” (działanie 1.3, program FERS) składa się z kilku podnaborów. Oto ich statusy na dzień 2026-09-25:
>
> 1. **Akademia HR** – **otwarty**, do 2026-11-30.  
>    Link: https://fers.parp.gov.pl/component/grants/grants/akademia-hr-oferta-dla-przedsiebiorcow#opis
>
> 2. **Usługi rozwojowe 4.0** – **zamknięty** (zakończył się 2026-08-31).  
>    Link: https://fers.parp.gov.pl/component/grants/grants/uslugi-rozwojowe-4-0---oferta-dla-dostawcow-uslug-bur
>
> 3. **Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców** – **nieokreślony** (w arkuszu podano datę zakończenia „2026/2027”).  
>    Link: https://fers.parp.gov.pl/component/grants/grants/wsparcie-firm-w-okresowych-trudnosciach---oferta-dla-przedsiebiorcow
>
> 4. **Dostępność szansą na rozwój** – **otwarty**, do 2027-12-01.  
>    Link: https://fers.parp.gov.pl/component/grants/grants/dostepnosc-szansa-na-rozwoj-3---oferta-dla-przedsiebiorcow
>
> 5. **Dostępność Dyrektywa EAA – oferta dla przedsiębiorców** – **otwarty**, do 2027-12-31.  
>    Link: https://fers.parp.gov.pl/component/grants/grants/dostepnosc-dyrektywa-eaa---oferta-dla-przedsiebiorcow
>
> 6. **Zielone rekomendacje** – **otwarty**, do 2027-12-01.  
>    Link: https://fers.parp.gov.pl/component/grants/grants/zielone-rekomendacje---oferta-dla-przedsiebiorcow
>
> 7. **GOZ – to się opłaca** – **otwarty**, do 2027-01-01.  
>    Link: https://fers.parp.gov.pl/component/grants/grants/goz---to-sie-oplaca---oferta-dla-przedsiebiorcow#opis
>
> Szczegółowe warunki udziału w każdym podnaborze należy sprawdzić w regulaminie dostępnym pod podanymi linkami.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Myślimy o pytaniu użytkownika: "Do kiedy trwa nabór „Kadry nowoczesnej gospodarki”?" Dzisiejsza data to 2026-09-25. Muszę odpowiedzieć na podstawie katalogu.

Szukam w katalogu naboru o nazwie "Kadry nowoczesnej gospodarki". Widzę w arkuszu "Aktualne_konkurencyjne" wiersze 25-31, które mają w kolumnie "Nazwa działania/poddziałania" wartość "Kadry nowoczesnej gospodarki". To jest jedno działanie, ale ma kilka podnaborów (różne obszary wsparcia). Każdy ma własne daty rozpoczęcia i zakończenia.

Zgodnie z regułą 5: "Jeśli pod jedną nazwą jest kilka naborów, wymień każdy osobno, z jego datami." Muszę więc wymienić każdy podnabór osobno.

Sprawdzam daty dla każdego podnaboru:

- Wiersz 25: "Akademia HR" – data rozpoczęcia 2024-03-25, data zakończenia 2026-11-30. Status: otwarty (2026-09-25 mieści się między 2024-03-25 a 2026-11-30).
- Wiersz 26: "Usługi rozwojowe 4.0" – data rozpoczęcia 2024-02-12, data zakończenia 2026-08-31. Status: zamknięty (2026-09-25 > 2026-08-31).
- Wiersz 27: "Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców" – data rozpoczęcia 2024-06-24, data zakończenia "2026/2027". To jest nieokreślona data (przedział lat). Zgodnie z regułą 3: "nieokreślony: brak daty zakończenia albo znany jest tylko miesiąc lub przedział lat, a dzisiejsza data mieści się w tym przedziale. Wtedy zacytuj dosłownie, co jest w arkuszu, i podaj link." Dzisiejsza data 2026-09-25 mieści się w przedziale 2026/2027, więc status nieokreślony. Cytuję: "2026/2027".
- Wiersz 28: "Dostępność szansą na rozwój" – data rozpoczęcia 2025-02-01, data zakończenia 2027-12-01. Status: otwarty.
- Wiersz 29: "Dostępność Dyrektywa EAA – oferta dla przedsiębiorców" – data rozpoczęcia 2025-02-25, data zakończenia 2027-12-31. Status: otwarty.
- Wiersz 30: "Zielone rekomendacje" – data rozpoczęcia 2025-06-01, data zakończenia 2027-12-01. Status: otwarty.
- Wiersz 31: "GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompetencji dotyczących zielonej ekonomii)" – data rozpoczęcia 2024-05-01, data zakończenia 2027-01-01. Status: otwarty.

Uwaga: w arkuszu "NOWE_konkurencyjne" nie ma tego naboru, więc tylko z arkusza "Aktualne_konkurencyjne".

Odpowiadam po polsku, zwięźle. Dla każdego podnaboru podaję nazwę, status, datę zakończenia (lub startu jeśli jeszcze nie ruszył) i link. Dla zamkniętych podaję, że są zamknięte. Dla nieokreślonego cytuję datę.

Linki: w wierszach są linki, np. dla wiersza 25: https://fers.parp.gov.pl/component/grants/grants/akademia-hr-oferta-dla-przedsiebiorcow#opis, dla wiersza 26: https://fers.parp.gov.pl/component/grants/grants/uslugi-rozwojowe-4-0---oferta-dla-dostawcow-uslug-bur, itd. Wszystkie linki są podane.

Upewniam się, że nie oceniam kwalifikowalności, tylko podaję fakty z katalogu.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## D08 · diagnostic · as-of 2026-09-30

**Pytanie:** Czy mogę jeszcze złożyć wniosek w naborze „Rozwój systemu edukacji”?

**Wzorzec:**
- musi zawierać: yes — open (row 14)
- musi zawierać: today is the last day

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-30**: otwarty: **18** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty (dziś ostatni dzień)** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty (dziś ostatni dzień)** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty (dziś ostatni dzień)** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty (dziś ostatni dzień)** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty (dziś ostatni dzień)** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (10.59 s · 312 tokenów wyjścia · finish=stop):

> Nabór **„Rozwój systemu edukacji”** (działanie 1.4, program FERS) jest **otwarty** – **dzisiaj (30 września 2026) jest jego ostatni dzień**. Możesz jeszcze złożyć wniosek, ale musisz to zrobić najpóźniej do końca dnia.
>
> - **Data zakończenia:** 2026-09-30 (włącznie)  
> - **Link:** [https://www.funduszeunijne.gov.pl/nabory/14-rozwoj-systemu-edukacji-7/](https://www.funduszeunijne.gov.pl/nabory/14-rozwoj-systemu-edukacji-7/)
>
> Szczegółowe warunki udziału sprawdź w regulaminie naboru.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Zgodnie z katalogiem, nabór "Rozwój systemu edukacji" (działanie 1.4, program FERS) ma datę rozpoczęcia 2026-04-01 i datę zakończenia 2026-09-30. Dzisiejsza data to 2026-09-30, więc jest to ostatni dzień naboru. Status: otwarty, ale ostatni dzień. Odpowiadam zgodnie z regułami: podaję status, że to ostatni dzień, i link.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## D09 · diagnostic · as-of 2026-10-01

**Pytanie:** Czy mogę jeszcze złożyć wniosek w naborze „Rozwój systemu edukacji”?

**Wzorzec:**
- musi zawierać: no — it closed on 2026-09-30 (row 14)

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-10-01**: otwarty: **13** · nieokreślony: **3** · zamknięty: **13** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **zamknięty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **zamknięty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **zamknięty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **zamknięty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **zamknięty** |

</details>

**Odpowiedź modelu** (19.29 s · 369 tokenów wyjścia · finish=stop):

> Nabór **„Rozwój systemu edukacji”** (działanie 1.4, program FERS) jest już **zamknięty**. Jego data zakończenia to **30 września 2026**, a dziś jest 1 października 2026, więc nie można już złożyć wniosku.
>
> Szczegóły naboru były dostępne pod linkiem:  
> https://www.funduszeunijne.gov.pl/nabory/14-rozwoj-systemu-edukacji-7/

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Mamy datę dzisiejszą: 2026-10-01. Pytanie dotyczy naboru "Rozwój systemu edukacji". Szukam w katalogu.

W arkuszu "Aktualne_konkurencyjne" w wierszu 14 (row 14) jest: 
Nr działania/poddziałania: 1.4
Nazwa: Rozwój systemu edukacji
Program: FERS
Data rozpoczęcia: 2026-04-01
Data zakończenia: 2026-09-30

Sprawdzam status: data zakończenia to 2026-09-30. Dzisiaj jest 2026-10-01, czyli po dacie zakończenia. Zgodnie z regułami: zamknięty, gdy dzisiejsza data jest późniejsza niż data zakończenia. Więc nabór jest zamknięty.

Odpowiadam: nie, nabór jest już zamknięty, bo zakończył się 30 września 2026.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## D10 · diagnostic · as-of 2027-12-15

**Pytanie:** Które nabory „Kadry nowoczesnej gospodarki” są jeszcze otwarte?

**Wzorzec:**
- musi zawierać: open: row 29 (until 2027-12-31)
- musi zawierać: undetermined: rows 27 and 30
- NIE może zawierać: rows 25, 26, 28 or 31 presented as open

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2027-12-15**: otwarty: **1** · nieokreślony: **4** · zamknięty: **24** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **nieokreślony** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **zamknięty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **zamknięty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **zamknięty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **zamknięty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **zamknięty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **zamknięty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **zamknięty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **zamknięty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **zamknięty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **zamknięty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **zamknięty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **zamknięty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **zamknięty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **zamknięty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **zamknięty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **zamknięty** |

</details>

**Odpowiedź modelu** (34.84 s · 1463 tokenów wyjścia · finish=stop):

> Spośród naborów „Kadry nowoczesnej gospodarki” (działanie 1.3, program FERS) według stanu na **15 grudnia 2027 r.**:
>
> - **Otwarty**  
>   **Dostępność Dyrektywa EAA – oferta dla przedsiębiorców**  
>   Data zakończenia: **2027-12-31**  
>   Link: [https://fers.parp.gov.pl/component/grants/grants/dostepnosc-dyrektywa-eaa---oferta-dla-przedsiebiorcow](https://fers.parp.gov.pl/component/grants/grants/dostepnosc-dyrektywa-eaa---oferta-dla-przedsiebiorcow)
>
> - **Status nieokreślony (nieprecyzyjna data zakończenia)**  
>   **Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców**  
>   W arkuszu podano datę zakończenia: **„2026/2027”** – nie można jednoznacznie stwierdzić, czy nabór jest jeszcze otwarty.  
>   Link: [https://fers.parp.gov.pl/component/grants/grants/wsparcie-firm-w-okresowych-trudnosciach---oferta-dla-przedsiebiorcow](https://fers.parp.gov.pl/component/grants/grants/wsparcie-firm-w-okresowych-trudnosciach---oferta-dla-przedsiebiorcow)
>
> Pozostałe nabory z tej grupy (Akademia HR, Usługi rozwojowe 4.0, Dostępność szansą na rozwój, Zielone rekomendacje, GOZ – to się opłaca) są już **zamknięte**.

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Mamy datę dzisiejszą: 2027-12-15. Szukamy naborów o nazwie "Kadry nowoczesnej gospodarki" (działanie 1.3, program FERS). W katalogu w arkuszu "Aktualne_konkurencyjne" są wiersze 25-31. Sprawdźmy każdy:

- wiersz 25: "Akademia HR" – data rozpoczęcia 2024-03-25, data zakończenia 2026-11-30. 2027-12-15 > 2026-11-30, więc zamknięty.
- wiersz 26: "Usługi rozwojowe 4.0" – data rozpoczęcia 2024-02-12, data zakończenia 2026-08-31. Zamknięty.
- wiersz 27: "Wsparcie firm w okresowych trudnościach" – data rozpoczęcia 2024-06-24, data zakończenia "2026/2027". To nie jest konkretna data, tylko przedział lat. Zgodnie z regułą 3: jeśli znany jest tylko miesiąc lub przedział lat, a dzisiejsza data mieści się w tym przedziale, to status nieokreślony. Przedział 2026/2027 – czy 2027-12-15 mieści się w tym przedziale? "2026/2027" może oznaczać okres od początku 2026 do końca 2027? Ale to nieprecyzyjne. W arkuszu jest "2026/2027". Dzisiejsza data to 2027-12-15, czyli koniec 2027. Jeśli uznamy, że przedział to całe lata 2026 i 2027, to mieści się. Ale reguła mówi: "znany jest tylko miesiąc lub przedział lat, a dzisiejsza data mieści się w tym przedziale. Wtedy zacytuj dosłownie, co jest w arkuszu, i podaj link." Zatem status nieokreślony. Trzeba zacytować: data zakończenia "2026/2027" i podać link.
- wiersz 28: "Dostępność szansą na rozwój" – data rozpoczęcia 2025-02-01, data zakończenia 2027-12-01. 2027-12-15 > 2027-12-01, więc zamknięty.
- wiersz 29: "Dostępność Dyrektywa EAA" – data rozpoczęcia 2025-02-25, data zakończenia 2027-12-31. 2027-12-15 < 2027-12-31, więc otwarty. Dziś jest 2027-12-15, a koniec 2027-12-31, więc jeszcze 16 dni. Nie jest to ostatni dzień.
- wiersz 30: "Zielone rekomendacje" – data rozpoczęcia 2025-06-01, data zakończenia 2027-12-01. 2027-12-15 > 2027-12-01, zamknięty.
- wiersz 31: "GOZ - to się opłaca" – data rozpoczęcia 2024-05-01, data zakończenia 2027-01-01. 2027-12-15 > 2027-01-01, zamknięty.

Zatem tylko jeden nabór jest otwarty: "Dostępność Dyrektywa EAA – oferta dla przedsiębiorców" (wiersz 29). A jeden ma nieokreślony status: "Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców" (wiersz 27).

Odpowiedź: Spośród naborów "Kadry nowoczesnej gospodarki" tylko jeden jest otwarty: "Dostępność Dyrektywa EAA – oferta dla przedsiębiorców" (do 2027-12-31). Jeden ma nieokreślony status z powodu nieprecyzyjnej daty: "Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców" (data zakończenia "2026/2027" – zacytuję). Reszta zamknięta.

Uwzględniam, że pytanie dotyczy tylko "Kadry nowoczesnej gospodarki", więc nie wymieniam innych naborów.

</details>

**Ocena:❌** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):Dane - podany tylko miesiąc a model dostał z datą** 

---

## D11 · diagnostic · as-of 2026-09-25

**Pytanie:** Czy mogę już złożyć wniosek w naborze „Wysokiej jakości system włączenia społecznego”?

**Wzorzec:**
- musi zawierać: not yet — the call starts on 2026-09-30 (row 17)

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (13.17 s · 566 tokenów wyjścia · finish=stop):

> Nabór **„Wysokiej jakości system włączenia społecznego”** (działanie 4.13, program FERS) **jeszcze nie ruszył**.  
> Składanie wniosków będzie możliwe od **30 września 2026 r.** do **30 listopada 2026 r.**  
>
> Link do naboru (zostanie opublikowany po ogłoszeniu):  
> [https://www.funduszeunijne.gov.pl/strony/skorzystaj/nabory/#/domyslne=1/10502=3742](https://www.funduszeunijne.gov.pl/strony/skorzystaj/nabory/#/domyslne=1/10502=3742)

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Zadanie: Odpowiedzieć na pytanie użytkownika na podstawie katalogu naborów. Dzisiejsza data: 2026-09-25. Pytanie dotyczy naboru "Wysokiej jakości system włączenia społecznego".

Szukam w katalogu. W arkuszu "Aktualne_konkurencyjne" wiersz 17: 
- Nr działania: 4.13
- Nazwa: Wysokiej jakości system włączenia społecznego
- Program: FERS
- Tryb: konkuencyjny (literówka, ale to konkurencyjny)
- Data rozpoczęcia: 2026-09-30
- Data zakończenia: 2026-11-30
- Budżet: 25
- Link: Link do naboru dostępny będzie na stronie: https://www.funduszeunijne.gov.pl/strony/skorzystaj/nabory/#/domyslne=1/10502=3742
- Grupa docelowa: Podmioty ekonomii społecznej

W arkuszu "NOWE_konkurencyjne" wiersz 4: te same dane.

Status: Data rozpoczęcia to 2026-09-30, dzisiaj jest 2026-09-25. Data rozpoczęcia jest późniejsza niż dzisiejsza data, więc nabór jeszcze nie ruszył. Zgodnie z regułą 3: "jeszcze nie ruszył: data rozpoczęcia jest późniejsza niż dzisiejsza data. Podaj datę startu."

Odpowiedź: Nie można jeszcze złożyć wniosku, nabór ruszy 30 września 2026. Podaję datę startu i link.

</details>

**Ocena:✅** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):** 

---

## N12 · hard_negative · as-of 2026-09-25

**Pytanie:** Jakie są nabory w programie Fundusze Europejskie dla Śląskiego?

**Wzorzec:**
- musi zawierać: no such calls in the data — it covers national programmes only
- NIE może zawierać: any call presented as belonging to a regional programme

<details open><summary><b>Fakty z katalogu: wszystkie nabory i ich status na dzień as-of</b> (status wyliczył skrypt mentora wg ADR-0008/0009)</summary>

Na dzień **2026-09-25**: otwarty: **17** · nie ruszył: **1** · nieokreślony: **3** · zamknięty: **8** (razem 29, arkusz `Aktualne_konkurencyjne`).

| wiersz | działanie | nabór | start | koniec | status |
|---|---|---|---|---|---|
| 3 | Adaptacja do zmian klimatu, zapobieganie klęskom i katastrofom | Renaturyzacja przekształconych cieków wodnych i obszarów od wód zależn… | 2026-05-29 | 2026-09-30 | **otwarty** |
| 4 | Wspieranie ochrony krytycznej infrastruktury energetycznej oraz magazynów ciepła na poziomie systemowym | Budowa magazynów ciepła na poziomie systemowym, służących zwiększeniu … | 2026-05-29 | 2026-09-30 | **otwarty** |
| 6 (też NOWE w. 5) | Międzynarodowe Agendy Badawcze (Teaming) | Wsparcie powstawania lub rozwoju wyspecjalizowanych, wiodących w skali… | 2026-09-01 | 2026-09-30 | **otwarty** |
| 14 | Rozwój systemu edukacji | Cyfrowa edukacja w jednostkach samorządu terytorialnego - rozwiązania … | 2026-04-01 | 2026-09-30 | **otwarty** |
| 18 | Deinstytucjonalizacja długoterminowej opieki medycznej | Standard świadczenia dziennego dla osób z otępieniem | 2026-06-09 | 2026-09-30 | **otwarty** |
| 5 | Ścieżka SMART | Wsparcie projektów badawczo-rozwojowych (B+R) przedsiębiorstw na reali… | 2026-08-07 | 2026-10-16 | **otwarty** |
| 10 (też NOWE w. 8) | Współfinansowanie działań EDIH | Wsparcie zwiększania konkurencyjności MŚP w procesie transformacji cyf… | 2026-09-24 | 2026-10-28 | **otwarty** |
| 20 | Wzmocnienie cyberbezpieczeństwa oraz rozwój odpornej infrastruktury przetwarzania danych  | Lokalne Centrum Cyberbezpieczeństwa (LCC) to wspólna inicjatywa kilku … | 2026-07-31 (w arkuszu tekst) | 2026-10-30 (w arkuszu tekst) | **otwarty** |
| 24 | Polskie Mosty Technologiczne | Wsparcie procesu ekspansji zagranicznej polskich MŚP, posiadających od… | 2026-09-15 | 2026-10-30 | **otwarty** |
| 8 (też NOWE w. 6) | Rozwój oferty klastrów dla firm (nabór dla Krajowych Klastrów Kluczowych) | Wsparcie skierowane jest na wzmocnienie potencjału koordynatorów Krajo… | 2026-09-16 | 2026-11-04 | **otwarty** |
| 9 (też NOWE w. 7) | Rozwój oferty klastrów dla firm (nabór dla Ponadregionalnych Klastrów Kluczowych) | Wsparcie skierowane jest zwiększanie profesjonalizacji działalności ko… | 2026-09-22 | 2026-11-10 | **otwarty** |
| 15 (też NOWE w. 2) | Rozwój kompetencji cyfrowych | Systemowe wsparcie edukacji cyfrowej osób dorosłych – Kluby Rozwoju Cy… | 2026-08-31 | 2026-11-16 | **otwarty** |
| 25 | Kadry nowoczesnej gospodarki | Akademia HR | 2024-03-25 | 2026-11-30 | **otwarty** |
| 31 | Kadry nowoczesnej gospodarki | GOZ - to się opłaca (wsparcie przedsiębiorstw w zakresie rozwoju kompe… | 2024-05 (tylko miesiąc) | 2027-01 (tylko miesiąc) | **otwarty** |
| 28 | Kadry nowoczesnej gospodarki | Dostępność szansą na rozwój | 2025-02-01 | 2027-12-01 | **otwarty** |
| 30 | Kadry nowoczesnej gospodarki | Zielone rekomendacje | 2025-06 (tylko miesiąc) | 2027-12 (tylko miesiąc) | **otwarty** |
| 29 | Kadry nowoczesnej gospodarki | Dostępność Dyrektywa EAA – oferta dla przedsiębiorców | 2025-02-25 | 2027-12-31 | **otwarty** |
| 17 (też NOWE w. 4) | Wysokiej jakości system 
włączenia społecznego | Wsparcie procesu reintegracji w przedsiębiorstwach społecznych | 2026-09-30 | 2026-11-30 | **nie ruszył** |
| 22 | Platformy startowe dla nowych pomysłów - wsparcie ekspertów | Rozwój innowacyjnego pomysłu w rentowny produkt we współpracy z eksper… | „Zgłoszenia pomysłów do Platform startowy” | pusta | **nieokreślony** |
| 23 | Pożyczki na rozwój turystyki | Wsparcie będzie przeznaczone na unowocześnienie mikro, małych i średni… | „Pożyczki udzielane w trybie ciągłym” | pusta | **nieokreślony** |
| 27 | Kadry nowoczesnej gospodarki | Wsparcie firm w okresowych trudnościach – oferta dla przedsiębiorców | 2024-06-24 | „2026/2027” | **nieokreślony** |
| 26 | Kadry nowoczesnej gospodarki | Usługi rozwojowe 4.0 | 2024-02-12 | 2026-08-31 | **zamknięty** |
| 7 | Granty na eurogranty | Wsparcie wzrostu innowacyjności i umiędzynarodowienia polskich MŚP ora… | 2025-08-12 | 2026-09-03 | **zamknięty** |
| 12 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka innowacyjność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-06 | 2026-09-07 | **zamknięty** |
| 11 | Startup Booster Poland (program Tech Goes Dual) | Wsparcie kosztów działań operatorów związanych z zarządzaniem programa… | 2026-07-14 | 2026-09-08 | **zamknięty** |
| 13 | Fundusz wsparcia technologii krytycznych [nabór dla sektora biotechnologii (BIOTECH)] - ścieżka strategiczna niezależność | Wsparcie skierowane jest na projekty przedsiębiorców, realizujące cele… | 2026-07-13 | 2026-09-16 | **zamknięty** |
| 16 (też NOWE w. 3) | Monitorowanie i identyfikacja potrzeb kompetencyjnych na rynku pracy | Prace Sektorowych Rad ds. Kompetencji dotyczące identyfikacji luk komp… | 2026-09-03 | 2026-09-17 | **zamknięty** |
| 19 | Platformy startowe dla nowych pomysłów 
Komponent II a. 
Wsparcie rozwoju działalności gospodarczej startupów w makroregionie Polski Wschodniej | Wsparcie rozwoju działalności biznesowej startupów dla zweryfikowanych… | 2026-06-30 | 2026-09-17 | **zamknięty** |
| 2 | Ochrona przyrody i rozwój zielonej infrastruktury - wykupy gruntów w parkach narodowych | Rozwój zdolności i usprawnienie zarządzania obszarami chronionymi - wy… | 2026-06-15 | 2026-09-21 | **zamknięty** |

</details>

**Odpowiedź modelu** (9.65 s · 269 tokenów wyjścia · finish=stop):

> Nie mam informacji o naborach w programie **Fundusze Europejskie dla Śląskiego**, ponieważ katalog, z którego korzystam, obejmuje wyłącznie programy krajowe (FEnIKS, FENG, FERS, FEPW, FERC). Programy regionalne, w tym dla województwa śląskiego, nie są w nim ujęte.
>
> Aby znaleźć aktualne nabory w tym programie, proszę sprawdzić stronę:
> - https://www.funduszeue.slaskie.pl/ (oficjalna strona Funduszy Europejskich dla Śląskiego)
> - lub portal https://www.funduszeunijne.gov.pl/ (po wybraniu filtra „regionalne”).

<details><summary>Rozumowanie modelu (span 3), kliknij, żeby rozwinąć</summary>

Zauważam, że pytanie dotyczy programu regionalnego – Fundusze Europejskie dla Śląskiego. Zgodnie z definicją roli, katalog obejmuje wyłącznie programy krajowe, bez programów regionalnych. W katalogu nie ma żadnych naborów dla tego programu. Dlatego muszę odpowiedzieć, że nie wiem, bo katalog nie zawiera takich informacji.

</details>

**Ocena:❌** 

**Jeśli ❌, jedno zdanie:** 

**Warstwa (dane / logika / model):model - podał linki do innych stron i dał nawet instrukcje do nic jak filtrować** 
