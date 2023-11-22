# watsonx.ai-lab

## Watsonx.ai prompt lab
Open this link and create a new project
https://dataplatform.cloud.ibm.com/wx/home?context=wx

Create a new prompt lab

Instruction:
```
Gyűjtsd ki a jelzálogkötelezett adatait a lenti szövegből.
```

Examples (input):
```
másrészről Név: Nagy Mária
Születési családi és utónév: Nagy Mária
Születési hely, év, hó, nap: Veszprém, 1971.01.01.
Anyja születési neve: Nagy Ilona
Lakóhely: 1021 Budapest, Labanc ú. 1.
Állampolgársága: Magyar
Személyi azonosító száma: 005286RA
Személyazonosító okmány típusa: Magyar
Személyazonosító okmány száma: 005286RA
Lakcímkártya száma: ASDBRA1234
Levelezési cím: 1021 Budapest, Labanc u. 1.
mint Zálogkötelezett,
```
Examples (output):
```
másrészről Név: Nagy Mária
Születési családi és utónév: Nagy Mária
Születési hely, év, hó, nap: Veszprém, 1971.01.01.
Anyja születési neve: Nagy Ilona
Lakóhely: 1021 Budapest, Labanc ú. 1.
Állampolgársága: Magyar
Személyi azonosító száma: 005286RA
Személyazonosító okmány típusa: Magyar
Személyazonosító okmány száma: 005286RA
Lakcímkártya száma: ASDBRA1234
Levelezési cím: 1021 Budapest, Labanc u. 1.
mint Zálogkötelezett,
```

Test your prompt (input):
```
Fogyasztói jelzálogszerződés ingatlanra


Számlaszám: 11111111-2222222222

Fogyasztói jelzálogszerződés ingatlanra


amely egyrészről az Demó Jelzálogbank Zártkörűen Működő Részvénytársaság (1011 Budapest, Váci utca 1.; cégjegyzékszám: 01-10-044659, bejegyezve a Fővárosi Törvényszék Cégbíróságán, statisztikai számjele: 12715524-6492-114-01) jelzálog- hitelintézet, Zálogjogosult és Hitelező - a továbbiakban Zálogjogosult, Hitelező valamint Jelzálogbank képviseletében meghatalmazottként eljár az Demó Bank Nyrt. (1081 Budapest, Kossuth u. 16., cégjegyzékszám: 01-10-044659, bejegyezve a Fővárosi Törvényszék Cégbíróságán, statisztikai számjele: 12715524-6492-114-01), a továbbiakban Bank

másrészről Név: Kiss Géza
Születési családi és utónév: Kiss Géza
Születési hely, év, hó, nap: Budapest, 1991.01.01.
Anyja születési neve: Nagy Ilona
Lakóhely: 1021 Budapest, Budakeszi út 1.
Állampolgársága: Magyar
Személyi azonosító száma: 005286RA
Személyazonosító okmány típusa: Magyar
Személyazonosító okmány száma: 005286RA
Lakcímkártya száma: ASDBRA1234
Levelezési cím: 1021 Budapest, Budakeszi út 1.
mint Zálogkötelezett, 


Név: Nagy Piroska
Születési családi és utónév: Nagy Piroska
Születési hely, év, hó, nap: Budapest, 1989.12.01.
Anyja születési neve: Nagy Mária
Lakóhely: 1041 Budapest, Kossuth út 1.
Állampolgársága: Magyar
Személyi azonosító száma: 005287RW
Személyazonosító okmány típusa: Magyar
Személyazonosító okmány száma: 005287RW
Lakcímkártya száma: RW123456
Levelezési cím: 1041 Budapest, Kossuth út 1.
mint Haszonélvező,

között az alulírott napon és helyen az alábbi feltételekkel jött létre. Ahol a jelen szerződés Zálogkötelezettről ír, eltérő rendelkezés hiányában ott a szerződést aláíró valamennyi zálogkötelezettet
 
kell érteni.1 Ahol a jelen szerződés Haszonélvezőről ír, eltérő rendelkezés hiányában ott a szerződést aláíró valamennyi haszonélvezőt kell érteni.
```


