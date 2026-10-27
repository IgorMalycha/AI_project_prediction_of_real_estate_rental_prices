import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_merge_data(partitioned_data: dict) -> pd.DataFrame:
    """Łączy dane z wielu plików CSV w jeden DataFrame."""
    dfs = []

    for key, loader in partitioned_data.items():
        df = loader()  # <- wywołujemy funkcję loadera, która zwraca DataFrame
        dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)
    print(f"Połączono {len(dfs)} plików. Wymiary danych: {merged_df.shape}")
    return merged_df

def perform_eda(df: pd.DataFrame) -> None:
    """Podstawowa eksploracja danych."""
    print("\nPodstawowe informacje o danych:")
    print(df.info())
    print("\nStatystyki opisowe:")
    print(df.describe(include='all'))

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
    plt.title("Macierz korelacji")
    plt.show()
