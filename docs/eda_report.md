#  EDA Report — Analiza danych o cenach wynajmu mieszkań w Polsce

## 1. 📁 Opis danych
Zbiór danych składa się z połączonych 8 miesięcznych plików CSV (listopad 2023 – czerwiec 2024).
Łącznie: **70 847 rekordów** i **28 kolumn**.

### Główne grupy zmiennych:
| Typ danych | Przykładowe kolumny | Opis |
|-------------|--------------------|------|
| Identyfikatory | `id` | Unikalny identyfikator ogłoszenia |
| Lokalizacja | `city`, `latitude`, `longitude`, `centreDistance` | Miasto, współrzędne, odległość od centrum |
| Parametry mieszkania | `squareMeters`, `rooms`, `floor`, `floorCount`, `buildYear`, `type`, `buildingMaterial`, `condition` | Cechy fizyczne mieszkania |
| Udogodnienia | `hasParkingSpace`, `hasBalcony`, `hasElevator`, `hasSecurity`, `hasStorageRoom` | Dostępność elementów infrastruktury |
| Udogodnienia lokalne | `schoolDistance`, `clinicDistance`, `postOfficeDistance`, `kindergartenDistance`, `restaurantDistance`, `collegeDistance`, `pharmacyDistance`, `poiCount` | Odległość do najbliższych punktów usługowych |
| Cena | `price` | Cena wynajmu w złotych |

---

## 2. 📊 Podstawowe statystyki

| Wskaźnik | Wartość |
|-----------|----------|
| Liczba obserwacji | 70 847 |
| Liczba zmiennych | 28 |
| Średnia cena | **3853 zł** |
| Mediana ceny | **3100 zł** |
| Min / Max cena | 346 zł / 23 000 zł |
| Średnia powierzchnia | 55,3 m² |
| Średnia liczba pokoi | 2,38 |
| Średni rok budowy | 1998 |
| Średnia odległość od centrum | 3,86 km |

Rozkład cen ma **prawostronną asymetrię** — większość ofert skupia się w przedziale 2 000–4 500 zł, natomiast występuje niewielka liczba bardzo drogich mieszkań (outliery).

---

## 3. ⚠️ Jakość danych

### Braki danych:
| Kolumna | Liczba braków | % braków |
|----------|----------------|-----------|
| `condition` | 51 665 | 73% |
| `buildingMaterial` | 28 997 | 41% |
| `buildYear` | 19 682 | 28% |
| `type` | 16 762 | 24% |
| `floor` | 8 613 | 12% |
| `hasElevator` | 3 924 | 5,5% |
| Pozostałe kolumny (odległości, poiCount itp.) | <1% | marginalne |

💡 **Wniosek:** zmienne `condition`, `buildingMaterial`, `buildYear`, `type` zawierają dużo braków i będą wymagały imputacji lub usunięcia.

### Duplikaty:
- Liczba duplikatów: **26 265 rekordów (37%)**
- Możliwe, że dotyczą tego samego ogłoszenia w różnych miesiącach → wymagana deduplikacja po `id`.

### Wartości odstające:
- Wykryto **~12 500 rekordów (ok. 18%)** z wartościami odstającymi (Z-score > 3), głównie w:
  - `price` – bardzo wysokie czynsze w Warszawie i Trójmieście,
  - `squareMeters` – nieliczne duże apartamenty powyżej 150 m²,
  - `centreDistance` – mieszkania >15 km od centrum.

---

## 4. 🧠 Wstępne obserwacje

- Dane obejmują **15 miast** — największy udział ma Warszawa (40%), następnie Kraków, Wrocław, Gdańsk i Poznań.
- **Typ zabudowy (`type`)** to głównie `apartmentBuilding` i `blockOfFlats`.
- **Większość mieszkań ma 2–3 pokoje** i powierzchnię w zakresie 35–65 m².
- **Nowe mieszkania (po 2010 r.)** stanowią ok. 20% próby.
- **Cena silnie koreluje** z:
  - powierzchnią (`squareMeters`, r ≈ 0.72),
  - liczbą pokoi (`rooms`, r ≈ 0.68),
  - rokiem budowy (`buildYear`, r ≈ 0.43),
  - odległością od centrum (`centreDistance`, r ≈ -0.55).
- Cechy binarne (`hasBalcony`, `hasElevator`, `hasParkingSpace`) mogą mieć znaczenie, lecz są współzależne z typem zabudowy.

---

## 5. 🧰 Rekomendacje – dalsze kroki

### 🧹 Czyszczenie danych
- Usunąć duplikaty (`id`).
- Imputować brakujące wartości (`buildYear`, `type`, `floor`) medianą lub kategorią „unknown”.
- Usunąć lub zakodować `condition` i `buildingMaterial` – zbyt wiele braków.
- Zweryfikować nietypowe wartości cen (np. >15 000 zł).

### ⚙️ Standaryzacja i przygotowanie
- Przeskalować zmienne numeryczne (`StandardScaler` lub `RobustScaler`).
- Zakodować zmienne kategoryczne (`city`, `type`, `ownership`, `hasBalcony`, itd.).
- Ewentualnie utworzyć nowe cechy, np.:
  - `price_per_m2 = price / squareMeters`
  - `is_new_building = buildYear > 2015`
  - `city_encoded` jako wskaźnik wielkości miasta.

### 🧪 Modelowanie
- Możliwe modele regresyjne: **XGBoost, Random Forest, LightGBM, CatBoost**