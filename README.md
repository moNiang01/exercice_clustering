# exercice_clustering

Analyse de Données Marketing avec Python

Description

Ce projet implémente une analyse de données marketing en utilisant Python et des bibliothèques populaires comme pandas, scikit-learn, et matplotlib. L'objectif est d'appliquer l'algorithme de clustering k-Means pour regrouper des produits en trois catégories de performance : Faible, Moyen, et Élevé, sur la base de leurs prix, catégories et inventaires disponibles.

Fonctionnalités

Chargement des données : Lecture des données marketing à partir d'un fichier CSV.

Prétraitement :

Conversion des colonnes en types numériques appropriés.

Gestion des valeurs manquantes par remplissage avec la médiane.

Normalisation des colonnes numériques pour un traitement optimal.

Clustering avec k-Means :

Regroupement des produits en clusters.

Attribution des étiquettes (Faible, Moyen, Élevé) à chaque cluster.

Visualisation :

Diagramme de dispersion montrant les clusters sur les axes "Prix" et "Catégorie".

Résumé des Clusters : Tableau présentant les moyennes des caractéristiques principales pour chaque cluster.

Prérequis

Python 3.x

Bibliothèques Python nécessaires :

pandas

scikit-learn

matplotlib

Installez les dépendances avec la commande :

pip install pandas scikit-learn matplotlib

Utilisation

Clonez ce dépôt :

git clone <url_du_dépôt>

Placez le fichier CSV des données dans le même répertoire que le script Python.

Exécutez le script :

python exercice1.py

Consultez :

Le diagramme de dispersion des clusters.

Le tableau de résumé affiché dans la console.

Résultats

Diagramme de dispersion : Visualisation des clusters étiquetés comme Faible, Moyen, ou Élevé.

Tableau de résumé : Moyennes des prix, catégories et niveaux d'inventaire pour chaque cluster, permettant une analyse rapide des performances des produits.

Structure du projet

exercice1.py : Script principal du projet.

marketing_sample_for_walmart_com.csv : Fichier de données (non inclus, à fournir).

Auteur

Ce projet a été réalisé dans le cadre d'un exercice de fouille de données.

