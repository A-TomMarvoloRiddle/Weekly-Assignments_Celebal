from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd

# Load the dataset
print("Loading 20 Newsgroups dataset...")

# Remove headers, footers, quotes for cleaner content
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
documents = newsgroups.data
targets = newsgroups.target
target_names = newsgroups.target_names

print(f"Loaded {len(documents)} documents.")
print("Sample document snippet:")
print(documents[0][:500])  # preview a snippet

# TF-IDF Vectorization
print("\nVectorizing documents with TF-IDF...")

vectorizer = TfidfVectorizer(
    max_df=0.5,
    min_df=2,
    stop_words='english',
    max_features=10000
)

X = vectorizer.fit_transform(documents)
print(f"TF-IDF matrix shape: {X.shape}")

# K-Means clustering
num_clusters = 20
print(f"\nRunning K-Means with {num_clusters} clusters...")
km = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
km.fit(X)

clusters = km.labels_
print("Clustering complete.")

# Top terms per cluster
print("\nTop terms per cluster:")
terms = vectorizer.get_feature_names_out()
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    top_terms = [terms[ind] for ind in order_centroids[i, :10]]
    print(f"Cluster {i}: {', '.join(top_terms)}")

# Assign documents to clusters
# Show cluster assignments for first few docs:
print("\nSample documents and assigned clusters:")
for i in range(10):
    print(f"Document {i} assigned to cluster {clusters[i]}")
    print("Text preview:", documents[i][:200].replace("\n", " "), "\n")

# Cluster sizes
cluster_sizes = pd.Series(clusters).value_counts().sort_index()
print("\nCluster sizes:")
print(cluster_sizes)

# Evaluate clustering
# Check how well clusters match true newsgroups
nmi = metrics.normalized_mutual_info_score(targets, clusters)
print("\nNormalized Mutual Information (NMI): ",nmi*100,"%")

# Save results to CSV
# Save cluster labels and document excerpts for further analysis
results = pd.DataFrame({
    "document_snippet": [doc[:200].replace("\n", " ") for doc in documents],
    "cluster": clusters,
    "true_newsgroup": [target_names[i] for i in targets]
})

results.to_csv("newsgroups_results.csv", index=False)
print("\nResults saved to newsgroups_results.csv")
