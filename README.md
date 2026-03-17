Velkommen til vårt FireGuard prosjekt!



--
Dette under er litt utdatert no, helst ikkje gjer dette lengre, for det bør skjes automatisk. Eg trur også at python programmet kjøres på ein litt anna måte no, som ikkje opptar ubuntu terminalen 17.03.2026 -Martin
Github actions tar automatisk å oppdaterer nrec og restarter python på nrec maskina når det skjer noko med main branch.
--

For å kjøre på ubuntu-serveren skriv:
1. " source ADA502-FireGuard/.fire/bin/activate ", her går man inn i et virituelt python environment
2. " python ADA502-FireGuard/src/ada502_fireguard/main.py ", her kjører man programmet

Har du oppdatert i GitHub og skal oppdatere NREC-en, gjør følgende:
1. Trykk CTRL + C, dette stopper det kjørende programmet
2. " deactivate ", dette får deg ut av det virituelle python environmentet i NREC-en
3. " cd ADA502-FireGuard ", nå er du i prosjektet
4. " git pull origin main ", her oppdaterer du prosjektet med de nye filene fra github
5. " cd ", nå går du ut av prosjektet
Nå har du oppdatert prosjektet og kan kjøre programmet som vist tidligere.
