# Modeling Report

## 1. Cel
Celem eksperymentu było porównanie trzech podejść modelowania:
- **Baseline model**
- **AutoML**
- (opcjonalnie) model własny — brak wyników, więc w raporcie porówniono dwa dostępne podejścia.

Analiza dotyczy zadania **regresji**, dlatego zastosowane metryki to:
- **RMSE**
- **MAE**
- **R²**

---

## 2. Wyniki metryk

### 2.1 Tabela porównawcza

| Podejście | RMSE | MAE | R² |
|-----------|------|------|------|
| **Baseline** | **1083.46** | **727.50** | **0.7449** |
| **AutoML (best model: Linear Regression)** | 1307.47 | 810.10 | 0.6276 | 

---

## 3. Interpretacja wyników

### 3.1 Baseline
Model bazowy osiągnął **najlepsze rezultaty**:
- najniższy RMSE,
- najniższy MAE,
- najwyższy R².

Może to oznaczać, że:
- zależność w danych jest stosunkowo prosta,
- dane znajdują się blisko przestrzeni dobrze opisanej modelem liniowym,
- AutoML nie wykonał lepszej optymalizacji niż baseline.

### 3.2 AutoML
AutoML wybrał jako najlepszy model **Linear Regression**, jednak jego wyniki są słabsze niż baseline:
- wyższe RMSE i MAE,
- niższy R².

Możliwe powody:
- AutoML optymalizował inną metrykę,
- modele złożone overfitują dane,
- preprocessing danych mógłby być lepszy.

---

## 4. Wnioski

1. **Najlepszy model: Baseline.**  
   Uzyskał najlepsze metryki i przewyższył AutoML we wszystkich ocenach jakości.

2. AutoML nie poprawił wyników — wskazuje to, że:
   - dane silnie preferują model liniowy,
   - potrzebne są dalsze eksperymenty z preprocessingiem.

---
