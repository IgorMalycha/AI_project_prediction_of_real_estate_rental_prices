# 🧹 Raport preprocessingu danych — Predykcja cen wynajmu mieszkań

## 1. Transformacje

1. **Łączenie danych:** połączono wszystkie partycje w jeden `DataFrame` (~70 tys. rekordów).  
2. **Usuwanie duplikatów:** po `["id", "city", "squareMeters", "price"]`.  
3. **Naprawa danych nielogicznych:** np. `floor > floorCount` → `NaN`.  
4. **Czyszczenie tekstów:** usunięcie spacji i konwersja do małych liter.  
5. **Usuwanie braków danych:** imputacja medianą dla liczb i dominantą dla kategorii.  
6. **Filtrowanie outlierów:** Z-score < 3 oraz ograniczenie wartości `price`, `squareMeters`, `rooms`, `buildYear`.  
7. **Podział danych:** 70% train, 15% test, 15% val.
8. **Standaryzacja:** `StandardScaler` dla cech numerycznych.

---

## 2. Wyniki
| Etap | Rekordy | Kolumny |
|------|---------|---------|
| Po czyszczeniu | 43 966 | 28 |
| X_train | 35 172 | 27 |
| X_test  | 8 794  | 27 |


