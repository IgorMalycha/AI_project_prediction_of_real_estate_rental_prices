# WebApp Report – API + Frontend dla projektu predykcji cen nieruchomości

## 1. Architektura aplikacji

Aplikacja składa się z dwóch głównych komponentów:

---

## 🟦 1. Backend – FastAPI (API predykcyjne)

### Funkcje backendu:

- ładuje najlepszy wytrenowany model `best_model.pkl` z katalogu `data/reporting/`,
- udostępnia endpointy:
  - `GET /` – prosty healthcheck API,
  - `POST /predict` – przyjmuje dane nieruchomości w formacie JSON i zwraca przewidywaną cenę,
- wykorzystuje model zapisany podczas pipeline modeling.

### Schemat działania backendu:

1. Użytkownik wysyła dane mieszkania → JSON.
2. FastAPI zamienia je na DataFrame.
3. Przekazuje dane do modelu ML.
4. Zwraca wartość przewidywanej ceny.

---

## 🟩 2. Frontend – Streamlit

### Funkcje frontendowe:

- wyświetla prosty formularz do wprowadzania cech nieruchomości,
- wysyła te dane do API (`POST http://localhost:8000/predict`),
- wyświetla wynik predykcji w czasie rzeczywistym.

### Schemat działania frontendu:

1. Użytkownik wprowadza dane mieszkania w formularzu.
2. Streamlit wysyła zapytanie POST do FastAPI.
3. Otrzymuje wynik i wyświetla go na ekranie.

---

## 2. Instrukcja uruchomienia aplikacji lokalnie

Poniżej opis krok po kroku jak uruchomić całą aplikację (API + frontend).

---

### 🔧 Krok 1 – Uruchom backend (FastAPI)

Przejdź do katalogu projektu:

```bash
cd src

Następnie uruchom API:

uvicorn app.main:app --reload

Backend będzie dostępny pod adresem:

👉 http://localhost:8000

Swagger UI (interaktywna dokumentacja API):

👉 http://localhost:8000/docs
```

### 🖥️ Krok 2 – Uruchom frontend (Streamlit)

Przejdź do katalogu projektu:

```bash
cd src

W nowym terminalu uruchom:

streamlit run frontend/app.py

Aplikacja otworzy się pod adresem:

👉 http://localhost:8501
```

## 3. Przepływ danych (end-to-end)

Streamlit zbiera dane od użytkownika.

Wysyła JSON na /predict do FastAPI.

FastAPI:

przygotowuje DataFrame,

używa best_model.pkl do predykcji.

Model zwraca wynik ceny.

Streamlit wyświetla wynik.

## 4. Przykłądowe dane:

{
  "city": "warszawa",
  "type": "apartmentbuilding",
  "squareMeters": 52.0,
  "rooms": 2.0,
  "floor": 3.0,
  "floorCount": 3.0,
  "buildYear": 2008.0,
  "latitude": 52.24,
  "longitude": 20.96,
  "centreDistance": 1.22,
  "poiCount": 18.0,
  "schoolDistance": 0.08,
  "clinicDistance": 0.14,
  "postOfficeDistance": 0.22,
  "kindergartenDistance": 0.24,
  "restaurantDistance": 0.06,
  "collegeDistance": 0.67,
  "pharmacyDistance": 0.12,
  "ownership": "condominium",
  "buildingMaterial": "brick",
  "condition": "premium",
  "hasParkingSpace": "yes",
  "hasBalcony": "yes",
  "hasElevator": "yes",
  "hasSecurity": "no",
  "hasStorageRoom": "no"
}

{
  "city": "szczecin",
  "type": "blockofflats",
  "squareMeters": 50.5,
  "rooms": 2.0,
  "floor": 1.0,
  "floorCount": 4.0,
  "buildYear": 2022.0,
  "latitude": 53.43,
  "longitude": 14.48,
  "centreDistance": 5.29,
  "poiCount": 1.0,
  "schoolDistance": 1.30,
  "clinicDistance": 1.23,
  "postOfficeDistance": 0.86,
  "kindergartenDistance": 0.71,
  "restaurantDistance": 0.90,
  "collegeDistance": 3.20,
  "pharmacyDistance": 0.43,
  "ownership": "condominium",
  "buildingMaterial": "brick",
  "condition": "premium",
  "hasParkingSpace": "yes",
  "hasBalcony": "yes",
  "hasElevator": "yes",
  "hasSecurity": "no",
  "hasStorageRoom": "no"
}


