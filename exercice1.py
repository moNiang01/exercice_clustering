from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Charger le jeu de données
data = pd.read_csv('marketing_sample_for_walmart_com-walmart_com_product_review__20200701_20201231__5k_data.csv')

# Convertir la colonne "Product Price" en numérique et remplir les NaN par la médiane
data['Product Price'] = pd.to_numeric(data['Product Price'], errors='coerce')
data['Product Price'] = data['Product Price'].fillna(data['Product Price'].median())

# Encoder la colonne "Product Category"
label_encoder = LabelEncoder()
data['Product Category'] = label_encoder.fit_transform(data['Product Category'].fillna('Unknown'))

# Remplir les valeurs manquantes dans "Product Available Inventory" par une médiane
if data['Product Available Inventory'].isna().all():
    print("Attention : Toutes les valeurs de 'Product Available Inventory' sont nulles.")
else:
    data['Product Available Inventory'] = data['Product Available Inventory'].fillna(data['Product Available Inventory'].median())

# Vérifie les valeurs brutes
print("Valeurs brutes de 'Product Available Inventory':\n", data['Product Available Inventory'].value_counts())

# Si toutes les valeurs sont identiques, exclure cette colonne
if data['Product Available Inventory'].nunique() <= 1:
    print("Aucune variation dans 'Product Available Inventory'. La colonne sera exclue.")
    features = data[['Product Price', 'Product Category']]
else:
    # Normalisation des colonnes numériques
    scaler = MinMaxScaler()
    data[['Product Price', 'Product Category', 'Product Available Inventory']] = scaler.fit_transform(
        data[['Product Price', 'Product Category', 'Product Available Inventory']]
    )
    features = data[['Product Price', 'Product Category', 'Product Available Inventory']]

# Vérifie les données normalisées
print("Données après normalisation :\n", data[['Product Price', 'Product Category', 'Product Available Inventory']].head())

# Appliquer k-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(features)

# Mapper les clusters à des étiquettes (0 -> Faible, 1 -> Moyen, 2 -> Élevé)
cluster_labels = {0: 'Faible', 1: 'Moyen', 2: 'Élevé'}
data['Performance'] = data['Cluster'].map(cluster_labels)

# Visualisation des Clusters
plt.figure(figsize=(10, 6))
for cluster, color in zip(['Faible', 'Moyen', 'Élevé'], ['red', 'blue', 'green']):
    subset = data[data['Performance'] == cluster]
    plt.scatter(subset['Product Price'], subset['Product Category'], label=cluster, alpha=0.6)

plt.title('Clusters de Performance des Produits')
plt.xlabel('Price (Normalisé)')
plt.ylabel('Category (Normalisé)')
plt.legend(title='Performance')
plt.grid(True)
plt.show()

# Résumé des clusters
summary = data.groupby('Performance')[['Product Price', 'Product Category', 'Product Available Inventory']].mean()
summary.rename(columns={
    'Product Price': 'Avg_Price',
    'Product Category': 'Avg_Product_Category',
    'Product Available Inventory': 'Avg_Inventory'
}, inplace=True)

print("\nRésumé des Clusters :\n", summary)
