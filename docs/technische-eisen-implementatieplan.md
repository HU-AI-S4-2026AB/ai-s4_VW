# Implementatieplan Technische Eisen (`[PROJ10]` Technische eisen en samenwerking)

**Project:** Bermvegetatie- en overgroeidetectie met AI  
**Projectgroep:** Miki Dağ, Huub van Look, Misha Leenders  
**Opdrachtgever:** VolkerWessels Infra Digital (Anahita Khosravipour & Tom)  
**Repository:** `HU-AI-S4-2026AB/ai-s4_VW`  
**Datum:** 23 november 2026

Dit document beschrijft voor elk van de vier onderdelen uit de inhoudsopgave van de slides *PROJ12 - Technische eisen* en de bijbehorende Canvas-rubric hoe wij als projectgroep daaraan voldoen richting `[PROJ-VIII] Definitief proof-of-concept (PoC)`. Per onderdeel hebben wij bestaande industriestandaarden onderzocht (met bronverwijzingen), vergeleken met de repository-richtlijn van VolkerWessels (*GitHub Repository_Structure*, Khosravipour, 2026) en vertaald naar concrete groepsafspraken die aansluiten op ons definitieve Plan van Aanpak (versie 3, 14-11-2026).

**Goedkeuring:** de zelf vastgestelde conventies in dit document (codeconventies in 2.2, docstring- en inline-commentconventies in 3.2 en branchconventies in 4.2) leggen wij ter goedkeuring voor aan de studentassistent, zoals slide 8 vraagt. De goedkeuring (wie, wanneer, eventuele aanpassingen) leggen wij vast in `docs/` en op het GitHub Projects-bord.

---

## Inhoudsopgave
1. [Reproduceerbaarheid](#1-reproduceerbaarheid)
2. [Codekwaliteit](#2-codekwaliteit)
3. [Codedocumentatie](#3-codedocumentatie)
4. [Versiebeheer en samenwerking](#4-versiebeheer-en-samenwerking)
5. [Documenteren (ontwerp)](#5-documenteren-ontwerp)
6. [Bronnenlijst](#6-bronnenlijst)

---

## 1. Reproduceerbaarheid

**Eis uit slides & Canvas-rubric:**  
*De volgende elementen zijn aanwezig, volledig en correct: `README.md`, installatie-instructies, `requirements.txt` / `environment.yml` en `.gitignore` / `.gitkeep`.*

### 1.1 Onderzoek naar bestaande standaarden
Om te zorgen dat onze code voor zowel docenten als het Data Science & AI-team van VolkerWessels direct reproduceerbaar is zonder zelf het wiel opnieuw uit te vinden, hebben wij drie bestaande standaarden onderzocht:
1. **README-opbouw:** *Make a README* (Guo, z.d.) en het *Best-README-Template* (Drew, z.d.) zijn de meest gebruikte standaarden op GitHub voor projectdocumentatie op de voorpagina. In het door Anahita aangeleverde richtlijndocument *GitHub Repository_Structure* (Khosravipour, 2026) verwijst VolkerWessels zelf expliciet naar *Best-README-Template* en schrijft zij een vaste 10-punts opbouw voor (Title, Description & Motivation, Table of Contents, Installation, Usage, Configuration, Contributing, License, Acknowledgements, Contact Information).
2. **Dependency- en omgevingsbeheer:** De *Python Packaging Authority* (PyPA, z.d.) schrijft `requirements.txt` voor om Python-packages met versienummers vast te leggen voor `pip`. Daarnaast adviseert de *Conda*-standaard (Anaconda, z.d.) een `environment.yml`-bestand waarin ook de exacte Python-versie en binaire GPU/CUDA-libraries (voor PyTorch en YOLO) worden vastgelegd. VolkerWessels werkt intern met de combinatie **PyCharm + Anaconda** en vraagt in haar richtlijn expliciet om `environment.yml` of `requirements.txt` in de root directory (Khosravipour, 2026).
3. **Git-hygiëne (`.gitignore` & `.gitkeep`):** De *Cookiecutter Data Science*-standaard (DrivenData, z.d.) en het officiële `Python.gitignore`-template van GitHub (GitHub, z.d.-a) schrijven voor dat ruwe data, getrainde modelgewichten, lokale IDE-mappen (`.idea/`, `.vscode/`) en Python-caches (`__pycache__/`) nooit in versiebeheer worden opgenomen. Omdat Git geen lege mappen bijhoudt, wordt volgens deze standaard een leeg `.gitkeep`-bestand gebruikt zodat verplichte datamappen wel direct na `git clone` bestaan.

### 1.2 Hoe wij hier als groep aan voldoen
1. **Volledige `README.md` (zie het losse bestand `documenten/README-template.md`):**
   Op de hoofdpagina van `HU-AI-S4-2026AB/ai-s4_VW` staat een `README.md` die zowel alle vier de verplichte Canvas-onderdelen (projectuitleg, Python-versie + installatiestappen, package-installatie en uitvoeringsinstructies) als de 10 secties van VolkerWessels en onze 9-staps pipeline uit Hoofdstuk 10 van het Plan van Aanpak bevat.
2. **Vastgelegde Python-versie (`3.11`, teamafspraak; staat niet in het PvA en wordt door het team bevestigd) en zowel `environment.yml` als `requirements.txt`:**
   Wij leveren beide bestanden mee in de hoofdmap zodat zowel een Anaconda/PyCharm-gebruiker bij VolkerWessels als een docent met standaard `venv` + `pip` in twee commando's exact dezelfde omgeving kan bouwen. Daarnaast leggen we in `config/config.yaml` een vaste `random_seed: 42` vast voor reproduceerbare datasplits en YOLO-trainingsruns.

   **Starttemplate `requirements.txt`:**
   ```text
   # Data-opschoning en Excel-metadata (non_damage_images.xlsx)
   numpy>=1.26.0
   pandas>=2.2.0
   openpyxl>=3.1.2

   # Beeldverwerking en YOLO Deep Learning
   torch>=2.2.0
   torchvision>=0.17.0
   ultralytics>=8.2.0
   opencv-python>=4.9.0
   Pillow>=10.2.0

   # Geodata (NWB / PDOK wegkoppeling) en configuratie
   geopandas>=0.14.3
   shapely>=2.0.3
   PyYAML>=6.0.1

   # Kwaliteitscontrole en testframework
   pytest>=8.0.0
   ruff>=0.3.0
   ```

   **Starttemplate `environment.yml`:**
   ```yaml
   name: ai-s4-vw
   channels:
     - pytorch
     - conda-forge
     - defaults
   dependencies:
     - python=3.11
     - pip
     - pip:
         - -r requirements.txt
   ```

3. **`.gitignore` en `.gitkeep`:**
   Zoals vastgelegd in Hoofdstuk 12 en 14 van ons Plan van Aanpak zetten wij de `5.910` JPG-foto's (681 MB) en het Excel-bestand `non_damage_images.xlsx` van VolkerWessels nooit in Git. Alleen de mappenstructuur (`data/raw/.gitkeep`, `data/processed/.gitkeep`, `data/sample/.gitkeep`) staat in de repository.

   **Starttemplate `.gitignore` (gebaseerd op GitHub `Python.gitignore`):**
   ```gitignore
   # Dataset van VolkerWessels en gegenereerde data (nooit in Git)
   data/raw/*
   data/processed/*
   !data/raw/.gitkeep
   !data/processed/.gitkeep
   !data/sample/.gitkeep
   !data/sample/**
   *.jpg
   *.jpeg
   *.png
   *.xlsx
   !assets/**/*.png
   !docs/**/*.png

   # Getrainde YOLO-gewichten en trainingsruns
   *.pt
   *.pth
   *.onnx
   runs/
   wandb/

   # Python cache en virtuele omgevingen
   __pycache__/
   *.py[cod]
   .venv/
   venv/
   .pytest_cache/
   .ruff_cache/

   # PyCharm, VS Code en OS-bestanden
   .idea/
   .vscode/
   .DS_Store
   Thumbs.db

   # Geheimen en API-sleutels (bijv. Mapillary token)
   .env
   *.local
   ```

---

## 2. Codekwaliteit

**Eis uit slides & Canvas-rubric:**  
*Codeconventies worden gevolgd (en goedgekeurd) en er is een validatie- en/of testframework gebruikt om de kwaliteit en werking van de code te borgen (unittests voor kernfunctionaliteiten én edge cases).*

### 2.1 Onderzoek naar bestaande standaarden
1. **Codeconventies (PEP 8):** **PEP 8** (*Style Guide for Python Code*; Van Rossum, Warsaw, & Coghlan, 2001) is de officiële standaard van de Python Software Foundation voor naamgeving, witruimte, inspringing (4 spaties), importvolgorde en regellengte. Aanvullend schrijft de *Google Python Style Guide* (Google, z.d.-a) voor om functies kort te houden, geen globale muteerbare status te gebruiken en configuratie te scheiden van logica.
2. **Modulaire mappenstructuur:** De richtlijn van VolkerWessels (Khosravipour, 2026) schrijft voor dat broncode niet in losse scripts in de hoofdmap staat, maar in `src/` met een duidelijke scheiding tussen het startpunt (`src/main.py`), herbruikbare hulpfuncties (`src/common/utils.py`), taakspecifieke functies (`src/specific/task_functions.py`) en een aparte testmap (`tests/test_utils.py`).
3. **Validatie- en testframeworks:**
   - Voor **codevalidatie (linting)** is **Ruff** (Astral, z.d.) de huidige industriestandaard in Python: het controleert automatisch op PEP 8-regels (`pycodestyle`), ongebruikte imports (`Pyflakes`) en importsortering (`isort`).
   - Voor **unittests** zijn Python's ingebouwde `unittest` en **`pytest`** (Krekel et al., z.d.) de twee standaardframeworks. Wij kiezen voor `pytest` omdat het leesbaardere tests oplevert volgens het **Arrange-Act-Assert (AAA)** patroon en met `@pytest.mark.parametrize` zeer geschikt is om dezelfde functie met meerdere randgevallen (*edge cases*) uit onze dataset te testen.

### 2.2 Hoe wij hier als groep aan voldoen
1. **Onze codeconventies (gebaseerd op PEP 8 en de VolkerWessels-richtlijn):**
   - **Naamgeving:**
     - Functies, methoden, variabelen en bestandsnamen in `snake_case` (bijv. `clean_metadata`, `crop_road_roi`, `compass_angle`).
     - Classes in `PascalCase` (bijv. `NwbRoadMatcher`, `YoloBermDetector`).
     - Constanten bovenin een module in `UPPER_CASE` (bijv. `MISSING_IMAGE_ID = 1344834780613622`).
   - **Functie-opbouw en lengte:**
     - Elke functie doet één ding (*Single Responsibility*) en telt maximaal **40 regels** code (exclusief docstring). Dit is een eigen teamafspraak; PEP 8 schrijft geen functielengte voor.
     - Maximale regellengte: **100 tekens**. Dit wijkt bewust af van PEP 8 (79 tekens) en is een eigen teamafspraak, die wij daarom expliciet laten goedkeuren. PEP 8 staat teams toe de grens tot 99 tekens te verhogen; 100 valt daar net buiten.
     - Geen hardcoded paden (zoals `C:/Users/...`) of magic numbers in de code; paden en drempelwaarden staan in `config/config.yaml`.
   - **Mappenindeling volgens Hoofdstuk 12 van ons PvA en VolkerWessels:**
     - `src/main.py`: startpunt van het programma;
     - `src/common/utils.py`: algemene functies (config inladen, padvalidatie, logging);
     - `src/specific/task_functions.py`: projectspecifieke functies voor onze pipeline (o.a. `crop_road_roi`, `is_image_usable`, `filter_predictions`; later splitsen per rit/GPS en NWB-locatiekoppeling);
     - `tests/test_utils.py`: unittests met `pytest` (bij groei splitsen we af naar `tests/test_task_functions.py`).
   - **Automatische validatie met `ruff`:** Voordat een branch gemerged wordt, draaien we `ruff check src/ tests/`. Als extra (Canvas: boven niveau) voegen we een GitHub Actions-workflow toe die `ruff` en `pytest` automatisch op elke Pull Request draait.

2. **Testplan met `pytest` (kernfunctionaliteiten + concrete edge cases uit PvA Hoofdstuk 8):**
   Wij testen elke kernfunctie uit onze 9-staps pipeline op zowel de normale werking (*happy path*) als de specifieke randgevallen die wij tijdens de data-analyse (PvA Hoofdstuk 8 en 14) in de VolkerWessels-dataset hebben ontdekt:

   | Kernfunctionaliteit (Pipeline-stap) | Normale test (Happy path) | Geteste randgevallen (Edge cases uit onze dataset) |
   |---|---|---|
   | **1. Metadata opschonen** (`clean_metadata`, stap 2) | Leest `non_damage_images.xlsx` in, koppelt rijen aan bestaande JPG's en voegt kolom `season` toe op basis van `captured_at` | - Rij met ontbrekende foto `image_id 1344834780613622` (5.911 rijen vs. 5.910 JPG's) wordt netjes verwijderd en gelogd zonder crash<br>- Volledig lege kolommen `creator` en `altitude` worden verwijderd<br>- `compass_angle > 360` (bijv. `361,1`) wordt gecorrigeerd naar `[0, 360)` |
   | **2. Beeldselectie & motorkap wegsnijden** (`crop_road_roi` / `is_image_usable`, stap 2) | Standaardbeeld (`1280x720`) wordt aan de onderkant bijgesneden (motorkap weg) en geschaald naar doelformaat | - Afwijkende resoluties uit de dataset (`1280x960`, `1280x719`, `1280x533`, `1280x1120`, `1024x576`) worden zonder vervorming verwerkt<br>- Te donker beeld (gemiddelde helderheid onder drempel, zoals A4 dec 2020) wordt gemarkeerd als onbruikbaar<br>- Ongeldige crop-ratio (`<= 0` of `>= 1`) geeft `ValueError` |
   | **3. Splitsen per rit of GPS-locatie** (`split_dataset`, stap 5) | Verdeelt beelden in train-, validatie- en testset op basis van GPS-locatie en opnamedag | - Controle dat foto's van hetzelfde wegvak of dezelfde rit nooit tegelijk in train én test voorkomen (`isdisjoint == True`)<br>- Splitsing gebruikt GPS en **niet** de foutieve `hectometer`-kolom (waar foto's met dezelfde hectometer ruim 25 km uit elkaar liggen) |
   | **4. Threshold-filtering op YOLO-detecties** (`filter_predictions`, stap 6 & 7) | Behoudt bounding boxes met `confidence >= threshold` (afgestemd op hoge recall) | - Foto zonder enige gedetecteerde begroeiing geeft een lege lijst terug zonder foutmelding<br>- Detectie exact op de grenswaarde (`confidence == threshold`) wordt meegenomen<br>- Threshold buiten `[0.0, 1.0]` geeft `ValueError` |
   | **5. GPS- en NWB-locatiekoppeling** (`match_gps_to_nwb`, stap 8) | Koppelt GPS-coördinaten van een detectie aan het dichtstbijzijnde provinciale wegvak in het NWB (bijv. N498, mediaan 2,5 m) en geeft XY-coördinaten terug | - GPS-punt ligt verder dan `nwb_max_distance_m` (config) van elke bekende weg -> geeft `None` / waarschuwing terug<br>- Ontbrekende (`NaN`) of omgewisselde `latitude`/`longitude`-waarden |

---

## 3. Codedocumentatie

**Eis uit slides & Canvas-rubric:**  
*Alle functies zijn voorzien van correcte en complete docstrings (bijv. PEP 257). Er zijn code comments waar de code onvoldoende voor zich spreekt (liever goede code dan veel comments). Er is gebruikgemaakt van Type Hinting.*

### 3.1 Onderzoek naar bestaande standaarden
1. **Docstring-standaarden (PEP 257):** **PEP 257** (*Docstring Conventions*; Goodger & Van Rossum, 2001) schrijft voor dat elke module, class en functie een docstring tussen `"""..."""` heeft die beschrijft wat de functie doet. Binnen PEP 257 zijn drie opmaakstijlen gangbaar: *Sphinx/reST* (`:param naam:`), *NumPy-stijl* en *Google-stijl* (Google, z.d.-a). In het richtlijndocument *GitHub Repository_Structure* levert VolkerWessels een eigen **Function Python Code Template** aan met de kopjes `Parameters:` (inclusief type en korte beschrijving) en `Returns:` (inclusief return-type) (Khosravipour, 2026). Dit template komt overeen met de Google-docstringstijl binnen PEP 257.
2. **Type Hinting (PEP 484 & PEP 585):** **PEP 484** (*Type Hints*; Van Rossum, Lehtosalo, & Langa, 2014) en **PEP 585** vormen de Python-standaard om verwachte types van argumenten en returnwaarden direct in de functiedefinitie (`def func(x: int) -> str:`) vast te leggen. PyCharm (de aanbevolen IDE in de VolkerWessels-richtlijn) controleert deze type hints automatisch op typefouten.
3. **Inline comment-conventies (PEP 8 & Clean Code):** Zowel **PEP 8** (Van Rossum et al., 2001) als *Clean Code* (Martin, 2008) schrijven voor dat code door heldere naamgeving zo veel mogelijk voor zichzelf moet spreken. Inline comments worden alleen geplaatst waar de code dat zelf niet kan uitdrukken: om het *waarom* van een domeinkeuze, datacorrectie of drempelwaarde uit te leggen.

### 3.2 Hoe wij hier als groep aan voldoen
1. **Docstring- en Type Hinting-standaard (PEP 257 + PEP 484 + VolkerWessels-template):**
   Elke functie in `src/` krijgt verplicht **Type Hinting** in de functiesignatuur én een **docstring** volgens het functie-template van VolkerWessels (doel, `Parameters` met type, `Returns` met type, en optioneel `Raises`).

   **Vast code- en docstring-template voor ons project:**
   ```python
   import pandas as pd


   def clean_metadata(
       df: pd.DataFrame,
       existing_filenames: set[str],
   ) -> pd.DataFrame:
       """
       Schoont het metadatabestand (non_damage_images.xlsx) op door ontbrekende foto's
       en lege kolommen te verwijderen en kompasrichtingen boven 360 graden te corrigeren.

       Parameters:
       df (pd.DataFrame): Ruwe metadata-tabel uit non_damage_images.xlsx.
       existing_filenames (set[str]): Set met bestandsnamen die daadwerkelijk in data/raw/ staan.

       Returns:
       pd.DataFrame: Opgeschoonde metadata-tabel waarbij elke rij een bestaand beeld heeft.

       Raises:
       ValueError: Als verplichte kolommen zoals 'filename' of 'compass_angle' ontbreken.
       """
       required_cols = {"filename", "compass_angle", "latitude", "longitude"}
       if not required_cols.issubset(df.columns):
           raise ValueError(f"Verplichte kolommen ontbreken: {required_cols - set(df.columns)}")

       # Verwijder kolommen die in de VolkerWessels-dataset voor 100% leeg zijn (PvA H8)
       cleaned = df.drop(columns=["creator", "altitude"], errors="ignore").copy()

       # Filter rijen waarvan de JPG ontbreekt op schijf (zoals image_id 1344834780613622)
       cleaned = cleaned[cleaned["filename"].isin(existing_filenames)].copy()

       # Sommige opnames hebben een compass_angle > 360 (tot 361.1); normaliseer naar [0, 360)
       cleaned["compass_angle"] = cleaned["compass_angle"] % 360.0
       return cleaned
   ```

2. **Onze inline comment-conventies:**
   - **Wel:** Commentaar bij domein- en dataset-specifieke beslissingen die niet uit de Python-syntax blijken (zoals in het voorbeeld hierboven: *waarom* `creator` en `altitude` worden verwijderd, *waarom* modulo 360 nodig is op `compass_angle`, of *waarom* wij GPS-coördinaten gebruiken in plaats van de foutieve kolom `road_number`).
   - **Niet:** Uitleggen wat standaard Python-code doet (`# maak een kopie van dataframe`) of oude code laten staan in comments (`# df = old_function(df)`).
   - **Opmaak:** Inline comments staan op een eigen regel boven de betreffende code, beginnen met `# ` (spatie) en een hoofdletter. Als een functie zoveel stappen heeft dat er meer dan drie tussenkopjes met commentaar nodig zijn, splitsen we de functie op in aparte hulpfuncties.

---

## 4. Versiebeheer en samenwerking

**Eis uit slides & Canvas-rubric:**  
*Het project op GitHub Projects is netjes beheerd met epics en stories. Daarbij hebben stories duidelijke acceptance criteria en een Definition of Done. Branchbeheer-conventies (zoals in het figuur uit de slides) worden gevolgd en Pull Requests zijn geaccepteerd onder toezicht van reviewers.*

### 4.1 Onderzoek naar bestaande standaarden
1. **Branching-modellen (Gitflow):** Het figuur op slide 6 van *PROJ12 - Technische eisen* (Heemskerk, 2026) en het hoofdstuk *Branches* in de richtlijn van VolkerWessels (Khosravipour, 2026) zijn beide gebaseerd op het **Gitflow Workflow**-model van Driessen (2010). Hierin blijft `main` (of `master`) altijd in een stabiele, werkende staat, fungeert `develop` als centrale integratiebranch voor lopend ontwikkelwerk, en worden nieuwe onderdelen ontwikkeld op kortlevende `feature/<naam>`-branches die vanaf `develop` worden aangemaakt en na afronding terug in `develop` worden gemerged. De `release/`- en `hotfix/`-branches uit het figuur laten wij weg: wij leveren één proof-of-concept op en hebben geen productieversie die onderhouden of met spoed gepatcht moet worden; fixes gaan via `fix/<naam>` naar `develop`.
2. **Scrum en backlogbeheer in GitHub Projects:** Volgens de *Scrum Guide* (Schwaber & Sutherland, 2020) en de documentatie van *GitHub Projects* (GitHub, z.d.-b) wordt een project beheerd via **Epics** (grote mijlpalen/thema's) en **Stories** (concrete taken binnen één sprint). Volgens de agile standaard (Wake, 2003; Schwaber & Sutherland, 2020) moet elke story toetsbare **Acceptance Criteria** hebben (specifieke voorwaarden waaraan het resultaat van die story moet voldoen) en hanteert het team één gezamenlijke **Definition of Done (DoD)** (de kwaliteitsdrempel die voor *elke* taak geldt voordat deze naar *Done* mag).
3. **Code Reviews via Pull Requests:** Volgens de *Google Engineering Practices Code Review Guide* (Google, z.d.-b) verhoogt verplichte peer review via Pull Requests de codekwaliteit en kennisdeling in het team, mits reviewers toetsen aan vooraf afgesproken teamconventies.

### 4.2 Hoe wij hier als groep aan voldoen
Onze werkwijze sluit direct aan op Hoofdstuk 12 (*Projectmanagement*) van ons Plan van Aanpak:

1. **GitHub Projects met Epics, Stories en Acceptance Criteria:**
   Wij werken in acht sprints (met sprintplanning op maandag, stand-ups op maandag en donderdag, en review/retro op vrijdag). De rol van **Repository- en kwaliteitsbeheerder** rouleert elke sprint tussen Miki Dağ, Huub van Look en Misha Leenders.
   Ons GitHub Projects-bord is ingedeeld in **Epics** die aansluiten op de fases uit ons PvA:
   - `Epic 1: Data opschonen, selecteren & NWB-locatieherstel` (Deelvraag 1 & 5)
   - `Epic 2: Labelrichtlijn & dataset labelen` (Deelvraag 2)
   - `Epic 3: YOLO baseline-model & modeliteraties` (Deelvraag 3 & 4, `PROJ-IV` t/m `PROJ-VII`)
   - `Epic 4: Prototype, GIS/XY-koppeling & Adviesrapport` (Deelvraag 5 & 6, `PROJ-VIII` & `PROJ-IX`)

   Elke **Story** op het bord krijgt bij de sprintplanning een vaste opbouw met concrete **Acceptance Criteria**:
   ```markdown
   ### Story
   Als <rol, bijv. data-analist / inspecteur> wil ik <functionaliteit>, zodat <doel voor het project>.

   ### Acceptance Criteria
   - [ ] <Toetsbaar criterium 1, bijv.: Functie `clean_metadata()` verwijdert `image_id 1344834780613622` en de lege kolommen `creator` en `altitude` en geeft precies 5.910 geldige rijen terug.>
   - [ ] <Toetsbaar criterium 2, bijv.: Alle `compass_angle`-waarden liggen na verwerking tussen 0 en 360 graden.>
   - [ ] <Toetsbaar criterium 3, bijv.: Resultaat wordt weggeschreven naar `data/processed/metadata_clean.csv`.>
   ```

2. **Onze vaste Definition of Done (DoD):**
   Hoofdstuk 12 van ons Plan van Aanpak zegt: "Een taak is af als de code via een pull request in develop staat, de code getest is en de uitleg in de documentatie staat." Voor de technische beoordeling breiden wij dat uit: een story mag op GitHub Projects pas naar de kolom **Done** wanneer aan **alle** onderstaande eisen is voldaan:
   - [ ] De code is ontwikkeld op een eigen `feature/<naam-van-taak>`-branch (afgetakt van `develop`).
   - [ ] De code staat op de juiste plek in de VolkerWessels-mappenstructuur (`src/common/` of `src/specific/`) en gebruikt instellingen uit `config/config.yaml`.
   - [ ] De code voldoet aan onze **PEP 8**-conventies en slaagt zonder fouten voor `ruff check src/ tests/`.
   - [ ] Alle nieuwe of gewijzigde functies bevatten **Type Hinting (PEP 484)** en een volledige **PEP 257 / VolkerWessels-docstring** (doel, `Parameters`, `Returns`).
   - [ ] Er zijn **unittests (`pytest`)** toegevoegd in `tests/` voor zowel de kernfunctionaliteit als de edge cases, en `pytest tests/` slaagt volledig.
   - [ ] Alle specifieke **Acceptance Criteria** van de story zijn afgevinkt.
   - [ ] De uitleg en eventuele nieuwe commando's of packages zijn bijgewerkt in `README.md` / `docs/` en `requirements.txt`.
   - [ ] De code is via een **Pull Request (PR)** gereviewd en goedgekeurd door minimaal één ander teamlid en gemerged naar `develop`.

3. **Branchbeheer en Code Reviews via Pull Requests:**
   Conform het diagram in de slides en het richtlijndocument van VolkerWessels gebruiken wij drie soorten branches:
   ```text
   main     o-----------------------------------------o (stabiele sprint-release, bijv. PROJ-IV)
             \                                       / (PR aan einde sprint)
   develop    o-------o---------------o-------------o
               \     / (PR + review)   \           / (PR + review)
   feature/*    o---o                   o----o----o
         (feature/data-cleaning)    (feature/yolo-baseline)
   ```
   - **`main`:** Bevat altijd de werkende, geteste versie van ons product. Aan het einde van elke sprint zetten wij `develop` via een gecontroleerde release-merge over naar `main` voor de Canvas-inlevering (`PROJ-IV` t/m `PROJ-VIII`).
   - **`develop`:** De centrale ontwikkelbranch waarin afgeronde taken samenkomen.
   - **`feature/<naam-van-taak>`:** Voor elke story op het scrumbord maakt het uitvoerende teamlid een nieuwe branch vanaf `develop` (bijv. `feature/data-cleaning`, `feature/nwb-locatie-koppeling`, `feature/yolo-baseline`). Voor kleine bugfixes gebruiken we `fix/<naam>`.
   - **Code review-procedure:** Niemand pusht rechtstreeks naar `main` of `develop`. Zodra een feature klaar is, opent de auteur een Pull Request naar `develop`. Minimaal **één ander teamlid** (bewaakt door de roulerende *Repository- en kwaliteitsbeheerder* van die sprint) controleert de PR aan de hand van onze *Definition of Done* (PEP 8, docstrings, type hints, `pytest` inclusief edge cases en geen ruwe data in Git) en laat reviewcommentaar achter voordat de PR wordt geaccepteerd.

---

## 5. Documenteren (ontwerp)

**Eis uit Canvas:**  
*Maak vooraf een ontwerp (bijv. pipeline, klassendiagram of flowchart), werk ermee en houd het bij, zodat er aan het einde een ontwerp is dat up-to-date is met de code.*

### 5.1 Hoe wij hier als groep aan voldoen
1. **Ontwerp vooraf:** het ontwerp staat al in Hoofdstuk 10 (*Ontwerp oplossing*) van ons Plan van Aanpak: een 9-staps pipeline (data verzamelen, data controleren, labelafspraken maken, beelden labelen, data verdelen, YOLO-model trainen, model testen, locaties koppelen, eindresultaat) met een schema. Wij kiezen een pipeline omdat ons project uit losse, opeenvolgende stappen bestaat en weinig classes kent.
2. **In de repository:** het schema staat als `docs/pipeline.png` in de repo, en de `README.md` verwijst ernaar. Elke functie in `src/specific/task_functions.py` en elke test in de tabel van 2.2 noemt de pipeline-stap waar hij bij hoort.
3. **Bijhouden:** wijkt de code af van het ontwerp (bijv. een extra stap of een ander model), dan passen wij `docs/pipeline.png` in dezelfde Pull Request aan. Reviewers controleren dit als onderdeel van de Definition of Done ("de uitleg staat in de documentatie", PvA H12). Zo sluit het ontwerp aan het einde van het project aan op de code.

---

## 6. Bronnenlijst

- Anaconda. (z.d.). *Managing environments — Conda documentation*. Geraadpleegd op 23 november 2026, van https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- Astral. (z.d.). *Ruff: An extremely fast Python linter and code formatter*. Geraadpleegd op 23 november 2026, van https://docs.astral.sh/ruff/
- Drew, O. (z.d.). *Best-README-Template*. GitHub. Geraadpleegd op 23 november 2026, van https://github.com/othneildrew/Best-README-Template
- Driessen, V. (2010, 5 januari). *A successful Git branching model*. nvie.com. https://nvie.com/posts/a-successful-git-branching-model/
- DrivenData. (z.d.). *Cookiecutter Data Science*. Geraadpleegd op 23 november 2026, van https://cookiecutter-data-science.drivendata.org/
- GitHub. (z.d.-a). *Python.gitignore template*. GitHub. Geraadpleegd op 23 november 2026, van https://github.com/github/gitignore/blob/main/Python.gitignore
- GitHub. (z.d.-b). *Best practices for repositories & About Projects*. GitHub Docs. Geraadpleegd op 23 november 2026, van https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- Goodger, D., & Van Rossum, G. (2001, 29 mei). *PEP 257 – Docstring Conventions*. Python Enhancement Proposals. https://peps.python.org/pep-0257/
- Google. (z.d.-a). *Google Python Style Guide*. Geraadpleegd op 23 november 2026, van https://google.github.io/styleguide/pyguide.html
- Google. (z.d.-b). *Google Engineering Practices Documentation: How to do a code review*. Geraadpleegd op 23 november 2026, van https://google.github.io/eng-practices/review/reviewer/
- Guo, D. (z.d.). *Make a README*. Geraadpleegd op 23 november 2026, van https://www.makeareadme.com/
- Heemskerk, J. (2026). *BB8 – Technische Beoordeling* [Collegeslides, bestand "PROJ12 - Technische eisen"]. Hogeschool Utrecht.
- Khosravipour, A. (2026, 30 oktober). *GitHub Repository_Structure (004)* [Richtlijndocument VolkerWessels Infra Digital].
- Krekel, H., Oliveira, B., Pfannschmidt, R., Bruynooghe, F., Laugher, B., & Bruhin, F. (z.d.). *pytest: helps you write better programs*. Geraadpleegd op 23 november 2026, van https://docs.pytest.org/
- Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
- Python Packaging Authority [PyPA]. (z.d.). *Requirements File Format — pip documentation*. Geraadpleegd op 23 november 2026, van https://pip.pypa.io/en/stable/reference/requirements-file-format/
- Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. https://scrumguides.org/
- Van Rossum, G., Lehtosalo, J., & Langa, Ł. (2014, 29 september). *PEP 484 – Type Hints*. Python Enhancement Proposals. https://peps.python.org/pep-0484/
- Van Rossum, G., Warsaw, B., & Coghlan, N. (2001, 5 juli). *PEP 8 – Style Guide for Python Code*. Python Enhancement Proposals. https://peps.python.org/pep-0008/
- Wake, W. C. (2003). *INVEST in Good Stories, and SMART Tasks*. XP123. https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/
