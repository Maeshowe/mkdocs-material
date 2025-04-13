# 📘 GPT Portfolio White Paper bemutatása

A GPT Portfolio egy mesterséges intelligencia által vezérelt befektetési stratégia, amely nagy nyelvi modellek (LLM-ek), például a ChatGPT analitikai képességeit használja fel arra, hogy részvényeket és iparágakat válasszon befektetési célokra. A stratégia célja, hogy strukturált, objektív és adatvezérelt megközelítést alkalmazzon a befektetések összeállításában, ezzel versenyképes teljesítményt nyújtva a hagyományos hedge fundokkal szemben.

## 🧠 Az AI-alapú elemzési rendszer működése

Mivel a GPT Trader (GPT Portfolio) közvetlenül nem rendelkezik valós idejű piaci adatokkal, külső adatforrásokat integrálva dolgozik. A rendszer elemzi a következő három fő területet:

- **Makrogazdasági elemzés**: Gazdasági indikátorok, kamatok, infláció, GDP-adatok, foglalkoztatási adatok és egyéb releváns globális események értékelése.
- **Szektor-specifikus elemzés**: Az adott szektor legfrissebb híreinek, technológiai innovációinak, szabályozási változásainak elemzése.
- **Vállalati szintű információk**: Egyes részvényekhez kapcsolódó aktuális pénzügyi teljesítmény, vállalati jelentések, technikai indikátorok, hírek és piaci hangulat elemzése.

## 🧩 Hogyan áll össze a portfólió?

A GPT Portfolio stratégia havi rendszerességgel fut, a következő lépések szerint:

1. **Makrogazdasági elemzés**: Aktuális gazdasági helyzet értékelése.
2. **Szektorértékelés**: Szektorok AI-alapú értékelése és rangsorolása, majd a top 5 szektor kiválasztása.
3. **Egyedi részvények kiválasztása**: Elemzés alapján kiválasztja a legjobb potenciállal rendelkező 10 vállalatot.
4. **Portfólió kiegyensúlyozása**: A kiválasztott részvényekből álló portfólió összeállítása és kétheti újraegyensúlyozása.

## 🛡️ Kockázatkezelés

A GPT Portfolio stratégia több eszközzel is védi a befektetések biztonságát:

- Diverzifikáció különböző szektorok és vállalatok között
- Kétheti rendszerességű újraegyensúlyozás
- Objektív, AI által generált pontozás
- Több adatforrás integrálása a döntéshozatali folyamat során

## 💬 Promptok, amelyek alapján működik a stratégia

A következő promptokat alkalmazza a GPT Portfolio:

### Szektor Prompt:

```
Képzeld el, hogy pénzügyi szakértő vagy részvényajánlási tapasztalattal.
Beszélj harmadik személyben.
Ne említsd a képesítéseidet.
Makrogazdasági adatok a kontextushoz: {macro_state}
Ma van: {today}.
A legfrissebb pénzügyi adatok és hírek alapján kérlek, adj egy pontszámot (1-től 100-ig) a szektor befektetési értékére.
Először írj egy jelentést a szektor gazdasági kilátásairól a hírek alapján.
Oszd meg a jelentést a következő részekre: legfrissebb hírek, gazdasági kilátások, politikai kihívások és technológiai fejlesztések.
Ezután új sorban írd: Pontszám: X.
Ne ajánlj alternatívákat.
Ne említsd a 'rendelkezésre álló' szót; használd helyette a 'legfrissebb' vagy 'aktuális' kifejezéseket.
Ne beszélj közvetlenül a befektetőkhöz, és ne ajánlj cselekvéseket.
Kezdd a 'Szektor befektetési jelentés:' címmel.
Végül új sorban írd: Pontszám: X.
```

### Vállalati Prompt:

```
Képzeld el, hogy pénzügyi elemző vagy, aki részvényeket értékel.
Beszélj harmadik személyben.
Ne említsd a képesítéseidet.
Makrogazdasági adatok a kontextushoz: {macro_state}
Szektor-specifikus adatok: {sector_state}
Vállalati adatok: {company_state}
Ma van: {today}.
A legfrissebb pénzügyi adatok és hírek alapján kérlek, adj egy pontszámot (1-től 100-ig) a vállalat befektetési értékére.
Először írj egy jelentést a vállalat gazdasági kilátásairól a hírek alapján.
Oszd meg a jelentést a következő részekre: legfrissebb hírek, gazdasági kilátások, politikai kihívások és technológiai fejlesztések.
Ezután új sorban írd: Pontszám: X.
Ne ajánlj alternatívákat.
Ne említsd a 'rendelkezésre álló' szót; használd helyette a 'legfrissebb' vagy 'aktuális' kifejezéseket.
Ne beszélj közvetlenül a befektetőkhöz, és ne ajánlj cselekvéseket.
Kezdd a 'Vállalati befektetési jelentés:' címmel.
Végül új sorban írd: Pontszám: X.
```

## 📈 Kövesd élőben az eredményeket!

A GPT Trader valós időben mutatja meg, hogyan teljesít a befektetési stratégia. A portfólió eredményeit kéthetente publikáljuk, így folyamatosan nyomon követheted az AI-alapú döntések hatékonyságát és teljesítményét.

**Légy részese te is az AI-alapú befektetések jövőjének!**