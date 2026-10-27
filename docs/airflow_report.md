# Airflow Report – Integracja Apache Airflow z projektem Kedro

## 1. Struktura DAG-u

W projekcie zaimplementowano jeden DAG o nazwie **`kedro_project_pipeline`**, którego zadaniem jest uruchamianie pipeline’ów projektu Kedro w określonej kolejności.

DAG zawiera trzy zadania odpowiadające pipeline’om:

### - eda_pipeline
Pipeline wykonujący eksploracyjną analizę danych (EDA).  
Uruchamiany poleceniem:

```bash
python3 -m kedro run --pipeline=eda
```

### - preprocessing_pipeline
Pipeline odpowiedzialny za przygotowanie danych (czyszczenie, transformacje, feature engineering):

```bash
python3 -m kedro run --pipeline=preprocessing
```

### - modeling_pipeline
Pipeline trenujący model uczenia maszynowego i zapisujący wyniki:

```bash
python3 -m kedro run --pipeline=modeling
```

### - evaluation_pipeline
Pipeline oceniający model i zapisujący wyniki:

```bash
python3 -m kedro run --pipeline=evaluation
```

### - Zależności między zadaniami

Zadania wykonywane są w następującej kolejności:

```
EDA → Preprocessing → Modeling → evaluation
```

## 2. Harmonogram uruchamiania

DAG posiada konfigurację harmonogramu:

```
0 8 * * *
```

co oznacza:

- **automatyczne uruchomienie codziennie o godzinie 08:00**,  
- możliwość ręcznego uruchomienia z interfejsu Airflow.

---

## 3. Logi i napotkane błędy podczas konfiguracji

Podczas pracy nad integracją pojawiło się kilka problemów, które zostały rozwiązane:

---

### - Niezgodność wersji Pythona z PyCaret**

Airflow w kontenerze używał Python **3.12**, a PyCaret wspiera jedynie **3.8–3.11**.

Błąd:

```
RuntimeError: Pycaret only supports Python 3.9, 3.10, 3.11...
```

**Rozwiązanie:**  
Zbudowano customowy obraz Airflow z Pythonem **3.10**.

---

### - Problemy z instalacją zależności**

Podczas instalacji `requirements.txt` pojawiały się błędy:

- brak kompatybilnych wersji bibliotek,
- konflikty scikit-learn z pycaret.

**Rozwiązanie:**  
Ujednolicono wersje bibliotek i dopasowano do PyCaret.

---

### - Brak dostępu Airflow do plików projektu**

Początkowo katalog Kedro nie był widoczny w kontenerze.

**Przyczyna:** błędne mountowanie katalogów.

**Rozwiązanie:**  
W docker-compose zamontowano cały projekt:

```
./:/opt/airflow/project
```

---

### - Problemy z uprawnieniami**

Airflow nie miał dostępu do wykonywania polecenia `kedro`.

**Rozwiązanie:**  
Instalacja zależności jako użytkownik airflow oraz nadanie praw katalogom.

---

## 4. Wnioski i pomysły na usprawnienia

### - Automatyczny retraining modeli

Można dodać pipeline, który:

- pobiera nowe dane,
- wykonuje preprocessing,
- trenuje nowy model
- automatycznie publikuje nową wersję modelu.

### - Notyfikacje o statusie zadań

Można dodać integracje:

- EmailOperator,  
- Teams Webhook.

Przykładowe zastosowania:

- powiadomienie o statusie wykonanego zadania,
- alert o błędzie.

### - Automatyczne raportowanie

Można generować:

- wykresy z EDA.

### - Usprawnienie obsługi błędów

Można dodać:

- timeouty,
- dodatkowe retry,
- logikę warunkową.

---


