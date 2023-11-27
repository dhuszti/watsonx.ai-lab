# watsonx.ai-lab

## Watsonx.ai prompt lab 1
Open this link and create a new project
https://dataplatform.cloud.ibm.com/wx/home?context=wx

Create a new prompt lab

### First prompt lab about meta-data extraction from long text
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
Születési hely: Veszprém
Születési időpont: 1971.01.01.
Anyja születési neve: Nagy Ilona
Lakcím: 1021 Budapest, Labanc utca 1.
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

között az alulírott napon és helyen az alábbi feltételekkel jött létre. Ahol a jelen szerződés Zálogkötelezettről ír, eltérő rendelkezés hiányában ott a szerződést aláíró valamennyi zálogkötelezettet kell érteni. 1 Ahol a jelen szerződés Haszonélvezőről ír, eltérő rendelkezés hiányában ott a szerződést aláíró valamennyi haszonélvezőt kell érteni.
```

Use these parameters on the right pane of the screen:

* Change token lenght to 100.

* Use model: LLAMA2-CHAT-70b

* Stop sequence: két enter


### Second prompt lab
Keep the same
```
Gyűjtsd ki a karakterisztikus kifejezéseket a lenti szövegből.
```
Test your prompt (input):
```
Néhány napja már kiderült, hogy Soros György neve is előkerül majd a kormány új nemzeti konzultációjában, mégpedig a homofóbbá eltérített pedofiltörvényről szóló kérdésben.


A kormány hivatalos Facebook-oldalán csütörtökön nyilvánosságra hozták a nemzeti konzultáció összes, szám szerint 14 kérdését is. A kérdőívek postázása csütörtökön kezdődik, a válaszokat augusztus 25-ig küldhetik vissza azok, akik ezt kitöltik. A kérdések érintik a minimálbér szintjét, a családtámogatásokat, a migrációt, a hitelmoratóriumot és az adókat is, Soros György neve pedig két kérdésben is felmerül.

A kérdések fele a „vannak, akik...” fordulattal kezdődik, ezek a járványkezelésre, a minimálbér-emelésre, a családtámogatásokra, a munkát terhelő adókra, a gyerekes szülők adóvisszatérítésére, a hitelmoratórium meghosszabbítására és a mingránsstopra vonatkozik.

Ezeket követik az olyan megállapításokkal megtűzdelt kérdések, hogy Soros György a járvány után újra meg fogja támadni Magyarországot, de Brüsszellel kapcsolatos kérdések is szép számmal szerepelnek a konzultációban.

A kérdések a következők:


Az első kérdés szerint többen úgy vélik, hogy a járvány után a világ sok tekintetben megváltozott, egy veszélyesebb korszak kezdődött. Magyarországot meg kell erősíteni, hogy meg tudjon felelni az új kihívásoknak. Mások szerint minden újra olyan lesz, mint a járvány előtt, így nincs erre szükség.

„Vannak, akik azt mondják, Magyarország megerősítését a minimálbér megemelésével kell kezdeni. A minimálbért 200 ezer forintra kell emelni, mert ez is biztosítja, hogy a gazdasági növekedésből ne csak a vállalatok, hanem a magyar emberek is részesüljenek. Mások szerint erre nincs szükség” – folytatódik a kérdések sora.

Egy újabb kérdés szerint vannak, akik azt mondják, Magyarországot úgy lehet megerősíteni, ha alkotmányos védelmet adunk a családtámogatásoknak, a munkát terhelő alacsony adóknak és a nyugdíjaknak, hogy válságok alatt egyetlen kormány se vehesse el azokat az emberektől. Mások szerint erre nincs szükség, a válságok árát fizessék meg az emberek.

„Vannak, akik azt mondják, Magyarország megerősítéséhez fontos lenne, hogy arra törekedjünk, Európában Magyarországon legyenek a legkisebbek a munkát terhelő adók. Mások szerint erre nincs szükség, vissza kell térni a Gyurcsány-korszak politikájához, és emelni kellene a munkát terhelő adókat” – a kormány ennek eldöntésére is kéri az embereket.

„Vannak, akik azt javasolják, hogy ha sikerül a kormánynak a gazdasági növekedés mértékét 5,5 százalék fölé emelni, akkor a gyermeket nevelő szülők kapják vissza a 2021. évben befizetett adójukat (az átlagbér adószintjéig), mivel ők viselték a legnagyobb terhet a járvány alatt. Mások szerint erre nincs szükség” – szerepel a konzultációban.


A kérdések sora úgy folytatódik:„"vannak, akik szerint a hitelmoratóriumot 2021 szeptemberétől jövő év júliusáig meg kell hosszabbítani, hogy azok a családok és vállalkozások, melyek rászorulnak, továbbra is felmentést kapjanak a hitel visszafizetése alól. A bankok szerint erre nincs szükség, a hitelmoratóriumot meg kell szüntetni és mindenkinek törlesztenie kell”.

„Brüsszel a járvány után újra vissza fog élni a hatalmával, eljárásokat indít hazánk ellen, hogy rákényszerítse a magyarokra az akaratát. Vannak, akik azt gondolják, Magyarországnak vállalnia kell a vitákat, és ki kell állnia az emberekért. Mások szerint Magyarországnak engednie kell Brüsszelnek” – tartalmazza a kérdőív.

„Brüsszel új adókat akar ránk kényszeríteni, hogy a multinacionális vállalatok által okozott környezetszennyezés és a klímaváltozás költségeit magasabb rezsiárakon keresztül a magyar családokkal fizettesse meg” – a kormány erről is megkérdezi az emberek véleményét, ahogy arról is: a „Soros György által finanszírozott szervezetek széles körű nemzetközi támadást indítottak Magyarország ellen a gyermekek védelméről szóló törvény miatt. Ez a törvény megtiltja a gyermekekre irányuló szexuális tartalmú propagandát az óvodákban, az iskolákban és a gyermekek számára elérhető médiában.”

„Soros György a járvány után újra meg fogja támadni Magyarországot, mert a magyarok ellenzik az illegális migrációt. Vannak, akik szerint ellen kell állni a Soros-szervezetek nyomásgyakorlásának, mások szerint Magyarországnak engednie kell a migrációs vitában” – folytatódik a kérdéssor.

Egy újabb kérdés arról szól: „sokak szerint a járványok korában óriási veszélyt jelent, ha mindenki szabadon beutazhat Magyarországra. Fenn kell tartani annak a lehetőségét, hogy újabb járványhullámok felbukkanása esetén járványügyi korlátozásokat lehessen előírni, és a járványok által sújtott országokból csak egészségügyi vízummal lehessen belépni Magyarországra. Mások szerint a járvány véget ért, a szabad beutazás lehetőségét minden országból korlátlanul biztosítani kell.”
```


### Third prompt lab
Intruction:
```
Gyűjtsd ki a karakterisztikus kifejezéseket és a hozzájuk tartozó szentimentet.
```
Examples (input):
```
A Környezetvédelmi Alapnál tett le nyertes pályázatot Kovászna város önkormányzata, amelynek köszönhetően kicserélhetik az utcai lámpák jelenlegi égőit LED-es
```
Examples (output):
```
Kovászna város önkormányzata: pozitív, energiatakarékos: pozitív
```
Test (input):
```
Néhány napja már kiderült, hogy Soros György neve is előkerül majd a kormány új nemzeti konzultációjában, mégpedig a homofóbbá eltérített pedofiltörvényről szóló kérdésben.


A kormány hivatalos Facebook-oldalán csütörtökön nyilvánosságra hozták a nemzeti konzultáció összes, szám szerint 14 kérdését is. A kérdőívek postázása csütörtökön kezdődik, a válaszokat augusztus 25-ig küldhetik vissza azok, akik ezt kitöltik. A kérdések érintik a minimálbér szintjét, a családtámogatásokat, a migrációt, a hitelmoratóriumot és az adókat is, Soros György neve pedig két kérdésben is felmerül.

A kérdések fele a „vannak, akik...” fordulattal kezdődik, ezek a járványkezelésre, a minimálbér-emelésre, a családtámogatásokra, a munkát terhelő adókra, a gyerekes szülők adóvisszatérítésére, a hitelmoratórium meghosszabbítására és a mingránsstopra vonatkozik.

Ezeket követik az olyan megállapításokkal megtűzdelt kérdések, hogy Soros György a járvány után újra meg fogja támadni Magyarországot, de Brüsszellel kapcsolatos kérdések is szép számmal szerepelnek a konzultációban.

A kérdések a következők:


Az első kérdés szerint többen úgy vélik, hogy a járvány után a világ sok tekintetben megváltozott, egy veszélyesebb korszak kezdődött. Magyarországot meg kell erősíteni, hogy meg tudjon felelni az új kihívásoknak. Mások szerint minden újra olyan lesz, mint a járvány előtt, így nincs erre szükség.

„Vannak, akik azt mondják, Magyarország megerősítését a minimálbér megemelésével kell kezdeni. A minimálbért 200 ezer forintra kell emelni, mert ez is biztosítja, hogy a gazdasági növekedésből ne csak a vállalatok, hanem a magyar emberek is részesüljenek. Mások szerint erre nincs szükség” – folytatódik a kérdések sora.

Egy újabb kérdés szerint vannak, akik azt mondják, Magyarországot úgy lehet megerősíteni, ha alkotmányos védelmet adunk a családtámogatásoknak, a munkát terhelő alacsony adóknak és a nyugdíjaknak, hogy válságok alatt egyetlen kormány se vehesse el azokat az emberektől. Mások szerint erre nincs szükség, a válságok árát fizessék meg az emberek.

„Vannak, akik azt mondják, Magyarország megerősítéséhez fontos lenne, hogy arra törekedjünk, Európában Magyarországon legyenek a legkisebbek a munkát terhelő adók. Mások szerint erre nincs szükség, vissza kell térni a Gyurcsány-korszak politikájához, és emelni kellene a munkát terhelő adókat” – a kormány ennek eldöntésére is kéri az embereket.

„Vannak, akik azt javasolják, hogy ha sikerül a kormánynak a gazdasági növekedés mértékét 5,5 százalék fölé emelni, akkor a gyermeket nevelő szülők kapják vissza a 2021. évben befizetett adójukat (az átlagbér adószintjéig), mivel ők viselték a legnagyobb terhet a járvány alatt. Mások szerint erre nincs szükség” – szerepel a konzultációban.


A kérdések sora úgy folytatódik:„"vannak, akik szerint a hitelmoratóriumot 2021 szeptemberétől jövő év júliusáig meg kell hosszabbítani, hogy azok a családok és vállalkozások, melyek rászorulnak, továbbra is felmentést kapjanak a hitel visszafizetése alól. A bankok szerint erre nincs szükség, a hitelmoratóriumot meg kell szüntetni és mindenkinek törlesztenie kell”.

„Brüsszel a járvány után újra vissza fog élni a hatalmával, eljárásokat indít hazánk ellen, hogy rákényszerítse a magyarokra az akaratát. Vannak, akik azt gondolják, Magyarországnak vállalnia kell a vitákat, és ki kell állnia az emberekért. Mások szerint Magyarországnak engednie kell Brüsszelnek” – tartalmazza a kérdőív.

„Brüsszel új adókat akar ránk kényszeríteni, hogy a multinacionális vállalatok által okozott környezetszennyezés és a klímaváltozás költségeit magasabb rezsiárakon keresztül a magyar családokkal fizettesse meg” – a kormány erről is megkérdezi az emberek véleményét, ahogy arról is: a „Soros György által finanszírozott szervezetek széles körű nemzetközi támadást indítottak Magyarország ellen a gyermekek védelméről szóló törvény miatt. Ez a törvény megtiltja a gyermekekre irányuló szexuális tartalmú propagandát az óvodákban, az iskolákban és a gyermekek számára elérhető médiában.”

„Soros György a járvány után újra meg fogja támadni Magyarországot, mert a magyarok ellenzik az illegális migrációt. Vannak, akik szerint ellen kell állni a Soros-szervezetek nyomásgyakorlásának, mások szerint Magyarországnak engednie kell a migrációs vitában” – folytatódik a kérdéssor.

Egy újabb kérdés arról szól: „sokak szerint a járványok korában óriási veszélyt jelent, ha mindenki szabadon beutazhat Magyarországra. Fenn kell tartani annak a lehetőségét, hogy újabb járványhullámok felbukkanása esetén járványügyi korlátozásokat lehessen előírni, és a járványok által sújtott országokból csak egészségügyi vízummal lehessen belépni Magyarországra. Mások szerint a járvány véget ért, a szabad beutazás lehetőségét minden országból korlátlanul biztosítani kell.”
```

### Run first python script
Download watsonxai_RAG_simple.py from GitHub. Please copy the API_key and project_id from the Box link (found at watsonx.ai slides).

Run it with following command: 
```
python watsonxai_RAG_simple.py
```

Ask these questions (one by one):
```
* Mi a Citibank utódja?
* Mi a Citibank Europe plc székhelye?
* Citibank Europe plc magyarországi címe?
* Mi történik a Citibanknál felvett hitelemmel?
* Mi a törlesztőrészlet?
```

### Run your first interactive python app
Download watsonxai_RAG_firstapp.py from GitHub. Please copy the API_key and project_id from the Box link (found at watsonx.ai slides).

Run it from command line:
```
streamlit run watsonxai_RAG_firstapp.py
```
It should open a new browser tab on this url:
http://localhost:8501/

Ask same questions like before.



