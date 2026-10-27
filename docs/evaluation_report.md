# Model Evaluation Report

## 1. Porównanie metryk (train / validation / test)

### Modele
- **Baseline model**: klasyczna regresja liniowa
- **AutoML model**: Linear Regression (wybrany przez PyCaret)

### Wyniki walidacji

| Model    | RMSE    | MAE    | R²    |
|----------|---------|--------|-------|
| Baseline | 1083.46 | 727.50 | 0.745 |
| AutoML  | 1307.47 | 810.10 | 0.628 |

Model bazowy osiąga istotnie lepsze wyniki na zbiorze walidacyjnym niż model AutoML, szczególnie pod względem RMSE i R².

### Wyniki testowe

Model bazowy został wybrany jako **best_model** i oceniony na zbiorze testowym. Metryki testowe są porównywalne z wynikami walidacyjnymi, co wskazuje na brak silnego przeuczenia oraz dobrą zdolność generalizacji.

---

## 2. Interpretacja wyników

### Feature importance

Analiza istotności cech (permutation importance) wskazuje, że największy wpływ na predykcję ceny najmu mają:

1. **city** – lokalizacja (miasto) jest najsilniejszym czynnikiem determinującym cenę  
2. **longitude** oraz **latitude** – precyzyjna lokalizacja geograficzna  
3. **squareMeters** – metraż nieruchomości  
4. **centerDistance** – odległość od centrum  

Pozostałe cechy, takie jak liczba pięter, piętro lokalu czy odległości do udogodnień (apteka, restauracje), mają znacznie mniejszy wpływ na wynik modelu.

Wyniki są zgodne z intuicją domenową – cena najmu jest w największym stopniu zależna od lokalizacji oraz wielkości mieszkania.

---

## 3. Analiza błędów

Wykres błędów predykcji (`prediction_errors.png`) pokazuje rozrzut błędów wokół zera, bez wyraźnego trendu systematycznego zawyżania lub zaniżania cen. Oznacza to, że model nie wykazuje silnego biasu.

Jednocześnie widoczny jest większy rozrzut błędów dla wyższych cen, co sugeruje, że model gorzej radzi sobie z drogimi nieruchomościami.

---

## 4. Rekomendacje dla dalszego doskonalenia modelu

1. **Zastosowanie modeli nieliniowych**  
   Rozważyć użycie RandomForestRegressor, Gradient Boosting lub XGBoost, które lepiej modelują złożone relacje.

2. **Lepsza inżynieria cech**  
   - połączenie latitude i longitude w cechy przestrzenne (np. clustering lokalizacji)  
   - logarytmizacja ceny  

3. **Obsługa wartości odstających**  
   Wysokie błędy dla drogich nieruchomości sugerują obecność outlierów.
   
