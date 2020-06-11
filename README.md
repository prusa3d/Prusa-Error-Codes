# Prusa-Error-Codes

## Složení chybového kódu <ErrorCode>

#XXYZZ

\# - pro označení sekvence chybového kódu
- XX - číslo tiskárny dle USB PID
- Y - kategorie chyby (společné pro všechny tiskárny)
- ZZ - číslo specifické chyby (liší se dle tiskárny)

Například: #12201

12 - tiskárna číslo 12: Original Prusa MINI

2 - kategorie chyby: chyba při měření teplot

01 - číslo chyby: nahřívání podložky selhalo

## Kategorie chyb
1. Mechanické - motory XYZ, tower, rozsah OS
2. Měření teplot - termistory/nahřívání 
3. Elektronické - MINDA, FINDA, Motion Controller, …
4. Konektivita - Wi-Fi, LAN, Prusa Connect Cloud
5. Systémové - BSOD, …
6. Bootloader
7. Warnings
