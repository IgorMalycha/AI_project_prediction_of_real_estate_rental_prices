# 🏙️ Projekt: Predykcja cen wynajmu mieszkań w Polsce

## 🎯 Opis problemu

Celem projektu jest stworzenie modelu uczenia maszynowego do **predykcji cen wynajmu mieszkań w różnych miastach w Polsce**.  
Model ma za zadanie przewidywać przybliżoną cenę wynajmu mieszkania na podstawie jego cech, takich jak:
- miasto i dzielnica,
- metraż (powierzchnia w m²),
- liczba pokoi,
- piętro,
- rok budowy.

**Typ problemu:** regresja (predykcja wartości ciągłej).

---

## 💡 Wartość biznesowa

Projekt dostarcza **praktyczne narzędzie analityczne dla rynku nieruchomości**, które umożliwia:
- oszacowanie realistycznej ceny wynajmu mieszkania,  
- porównanie ofert dostępnych na rynku,  
- wspieranie decyzji zarówno osób poszukujących mieszkań, jak i wynajmujących.

Rozwiązanie może znaleźć zastosowanie w:
- aplikacjach do wyceny nieruchomości,  
- portalach ogłoszeniowych,  
- analizach rynkowych i raportach cenowych.

---

## 📊 Dane

Do projektu wykorzystano dane pochodzące z publicznego zbioru dostępnego na Kaggle:  
**Źródło:** [Apartment Prices in Poland (Kaggle)](https://www.kaggle.com/datasets/krzysztofjamroz/apartment-prices-in-poland/data)  
**Zakres:** informacje o mieszkaniach w Polsce, m.in. lokalizacja, powierzchnia, liczba pokoi, rok budowy oraz cena.

## 🧱 Struktura katalogów 

````

ai-project-prediction-of-real-estate-rental-prices/
│
├── conf/
│   └── base/
│       └── catalog.yml
│
├── data/
│   ├── raw/
│   │   ├── datasets.csv
│   |   └── ...
│   ├── intermediate/
│   │   └── clean_data.csv
│   ├── primary/
│   │   └── scaled_data.csv
│   └── model_input/
│       ├── train.csv
│       ├── val.csv
│       └── test.csv
│   └── reporting/
│       ├── baseline_model.pkl
│       ├── automl_model.pkl
│       ├── automl_results.csv
│       ├── model_comparison.json
│       └── baseline_metrics.json
│
├── notebooks/
│   └── EDA_prediction_of_real_estate_rental_prices.ipynb
│
├── src/
│   └── ai-project-prediction-of-real-estate-rental-prices/
│       ├── pipelines/
│       │   └── eda/
|       |       ├── __init__.py
│       │       ├── nodes.py
│       │       └── pipeline.py
│       │   └── preprocessing/
│       │       ├── nodes.py
│       │       └── pipeline.py
│       │   └── modeling/
│       │       ├── nodes.py
│       │       └── pipeline.py
│       ├── pipeline_registry.py
|       └── __init__.py
|
├── src/tests/pipelines/preprocessing/
│   └── test_nodes.py
│
├── docs/
│   ├── eda_report.md
│   ├── modeling_report.md
│   ├── preprocessing_report.md
│   └── architecture_diagram.png
│
├── .gitignore
├── requirements.txt
├── LICENSE
├── pyptoject.toml
└── README.md

````

## 🧑‍💻 Członkowie zespołu

| Imię i nazwisko | Rola w projekcie | GitHub login |
|------------------|------------------|---------------|
|                  |                  |               |
| Igor Małycha     |   właściciel projektu      |  [@IgorMalycha](https://github.com/IgorMalycha)  |
|                  |                  |               |

---

## 🧭 Linki projektu

- 📦 Repozytorium GitHub: [link do repozytorium](https://github.com/PJATK-ASI-2024/ai_project_prediction_of_real_estate_rental_prices) 
- 🗂️ GitHub Project Board: [link do GitHub project board](https://github.com/orgs/PJATK-ASI-2024/projects/190)  
- 📜 Dokumentacja / diagram architektury: [link do dokumentacji](docs/) 
- 📘 Notebook EDA: [link do notebook EDA](notebooks/)
- 📄 Raport EDA: [link do raportu eda](docs/)
- 📄 Raport preprocessingowy: [link do raportu preprocessingu](docs/)
- 🧪 Testy jednostkowe: [link do testów](src/tests/pipelines/preprocessing)

---
