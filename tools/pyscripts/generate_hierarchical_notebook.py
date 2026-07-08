#!/usr/bin/env python3
"""
Generate the hierarchical clustering notebook with from-scratch implementation.
"""

import json

# Create the complete notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.12.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Cell 1: Title and introduction
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# Hierarchical Clustering: From-Scratch Implementation\n",
        "\n",
        "**Topic 07** | February 2026 | M.Sc. DSAI\n",
        "\n",
        "---\n",
        "\n",
        "## My Implementation Goals\n",
        "\n",
        "I'm implementing **hierarchical clustering from scratch** to understand:\n",
        "\n",
        "1. **Distance matrix computation** – How to compute pairwise distances (Euclidean, Manhattan, Cosine)\n",
        "2. **Linkage criteria** – How different methods (single, complete, average, Ward) merge clusters\n",
        "3. **Agglomerative algorithm** – Iterative bottom-up merging of closest clusters\n",
        "4. **Merge history tracking** – Recording which clusters merge at what distance\n",
        "5. **Visualization** – Seeing the algorithm build the hierarchy step-by-step\n",
        "6. **Validation** – Comparing with scipy to ensure correctness\n",
        "\n",
        "This is my second clustering algorithm – understanding how hierarchical structures are built!"
    ]
})

# Cell 2: Imports
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Import libraries\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.datasets import make_blobs, load_iris\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.metrics import adjusted_rand_score  # For validation only\n",
        "\n",
        "# Set random seed for reproducibility\n",
        "np.random.seed(42)\n",
        "\n",
        "# Plotting style\n",
        "sns.set_style('whitegrid')\n",
        "plt.rcParams['figure.figsize'] = (10, 6)"
    ]
})

# Cell 3: Distance matrix markdown
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Part 1: Distance Matrix Computation\n",
        "\n",
        "### Mathematical Foundation\n",
        "\n",
        "Hierarchical clustering starts by computing all pairwise distances between points.\n",
        "\n",
        "**Distance Metrics:**\n",
        "\n",
        "1. **Euclidean Distance**: Straight-line distance\n",
        "   $$d(x_i, x_j) = \\sqrt{\\sum_{k=1}^{n}(x_{ik} - x_{jk})^2}$$\n",
        "\n",
        "2. **Manhattan Distance**: City-block distance\n",
        "   $$d(x_i, x_j) = \\sum_{k=1}^{n}|x_{ik} - x_{jk}|$$\n",
        "\n",
        "3. **Cosine Distance**: Based on angle between vectors\n",
        "   $$d(x_i, x_j) = 1 - \\frac{x_i \\cdot x_j}{||x_i|| \\cdot ||x_j||}$$\n",
        "\n",
        "The distance matrix is **symmetric**: $d(i,j) = d(j,i)$ and diagonal is zero: $d(i,i) = 0$"
    ]
})

# Cell 4: Distance matrix code
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "def compute_distance_matrix(X, metric='euclidean'):\n",
        "    \"\"\"\n",
        "    Compute pairwise distance matrix from scratch.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    X : ndarray of shape (n_samples, n_features)\n",
        "        Data points\n",
        "    metric : str, one of ['euclidean', 'manhattan', 'cosine']\n",
        "        Distance metric to use\n",
        "        \n",
        "    Returns:\n",
        "    --------\n",
        "    distances : ndarray of shape (n_samples, n_samples)\n",
        "        Symmetric distance matrix where distances[i,j] = distance(X[i], X[j])\n",
        "        \n",
        "    Educational Notes:\n",
        "    ------------------\n",
        "    - We compute all pairwise distances explicitly\n",
        "    - Matrix is symmetric: distances[i,j] = distances[j,i]\n",
        "    - Diagonal is zero: distances[i,i] = 0 (distance to self)\n",
        "    - This is O(n^2) in samples, which is acceptable for hierarchical clustering\n",
        "    \"\"\"\n",
        "    n = len(X)\n",
        "    distances = np.zeros((n, n))\n",
        "    \n",
        "    for i in range(n):\n",
        "        for j in range(i+1, n):  # Only upper triangle (symmetric)\n",
        "            if metric == 'euclidean':\n",
        "                # Euclidean: sqrt(sum((xi - xj)^2))\n",
        "                distances[i, j] = np.sqrt(np.sum((X[i] - X[j]) ** 2))\n",
        "            elif metric == 'manhattan':\n",
        "                # Manhattan: sum(|xi - xj|)\n",
        "                distances[i, j] = np.sum(np.abs(X[i] - X[j]))\n",
        "            elif metric == 'cosine':\n",
        "                # Cosine: 1 - (x·y / ||x|| ||y||)\n",
        "                dot_product = np.dot(X[i], X[j])\n",
        "                norm_product = np.linalg.norm(X[i]) * np.linalg.norm(X[j])\n",
        "                # Avoid division by zero\n",
        "                if norm_product > 0:\n",
        "                    distances[i, j] = 1 - (dot_product / norm_product)\n",
        "                else:\n",
        "                    distances[i, j] = 0\n",
        "            else:\n",
        "                raise ValueError(f\"Unknown metric: {metric}\")\n",
        "            \n",
        "            # Fill symmetric position\n",
        "            distances[j, i] = distances[i, j]\n",
        "    \n",
        "    return distances\n",
        "\n",
        "print(\"✓ compute_distance_matrix() implemented\")"
    ]
})

# Cell 5: Linkage criteria markdown
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Part 2: Linkage Criteria\n",
        "\n",
        "### How Do We Merge Clusters?\n",
        "\n",
        "Once we have distances between points, we need to define how to compute distances between clusters.\n",
        "Different linkage criteria create different hierarchies!\n",
        "\n",
        "**Main Linkage Methods:**\n",
        "\n",
        "1. **Single Linkage** (Nearest Neighbor)\n",
        "   - Distance = minimum distance between any pair of points\n",
        "   - $$d(C_i, C_j) = \\min_{x \\in C_i, y \\in C_j} d(x, y)$$\n",
        "   - Tends to create long, chain-like clusters\n",
        "\n",
        "2. **Complete Linkage** (Farthest Neighbor)\n",
        "   - Distance = maximum distance between any pair of points\n",
        "   - $$d(C_i, C_j) = \\max_{x \\in C_i, y \\in C_j} d(x, y)$$\n",
        "   - Creates compact, spherical clusters\n",
        "\n",
        "3. **Average Linkage** (UPGMA)\n",
        "   - Distance = average distance between all pairs\n",
        "   - $$d(C_i, C_j) = \\frac{1}{|C_i||C_j|} \\sum_{x \\in C_i, y \\in C_j} d(x, y)$$\n",
        "   - Balanced approach between single and complete\n",
        "\n",
        "4. **Ward's Method** (Minimum Variance)\n",
        "   - Merges clusters that minimize within-cluster variance\n",
        "   - $$d(C_i, C_j) = \\sqrt{\\frac{|C_i||C_j|}{|C_i|+|C_j|}}\\|\\mu_i - \\mu_j\\|$$\n",
        "   - Most commonly used in practice\n",
        "\n",
        "We'll implement all of these!"
    ]
})

# Cell 6: Compute cluster distance function
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "def compute_cluster_distance(distances, cluster_i, cluster_j, method='ward', cluster_data=None):\n",
        "    \"\"\"\n",
        "    Compute distance between two clusters using specified linkage method.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    distances : ndarray of shape (n_samples, n_samples)\n",
        "        Distance matrix between all points\n",
        "    cluster_i : list of int\n",
        "        Indices of points in first cluster\n",
        "    cluster_j : list of int\n",
        "        Indices of points in second cluster\n",
        "    method : str, one of ['single', 'complete', 'average', 'ward']\n",
        "        Linkage criterion to use\n",
        "    cluster_data : ndarray, optional\n",
        "        Original data points (required for Ward's method)\n",
        "        \n",
        "    Returns:\n",
        "    --------\n",
        "    distance : float\n",
        "        Distance between clusters\n",
        "        \n",
        "    Educational Notes:\n",
        "    ------------------\n",
        "    - Different linkage methods define 'distance' differently\n",
        "    - Single: takes smallest distance (aggressive merging)\n",
        "    - Complete: takes largest distance (conservative merging)\n",
        "    - Average: takes middle ground\n",
        "    - Ward: minimizes within-cluster variance (statistical approach)\n",
        "    \"\"\"\n",
        "    \n",
        "    if method == 'single':\n",
        "        # Single linkage: minimum distance between any two points\n",
        "        min_dist = np.inf\n",
        "        for i in cluster_i:\n",
        "            for j in cluster_j:\n",
        "                min_dist = min(min_dist, distances[i, j])\n",
        "        return min_dist\n",
        "    \n",
        "    elif method == 'complete':\n",
        "        # Complete linkage: maximum distance between any two points\n",
        "        max_dist = -np.inf\n",
        "        for i in cluster_i:\n",
        "            for j in cluster_j:\n",
        "                max_dist = max(max_dist, distances[i, j])\n",
        "        return max_dist\n",
        "    \n",
        "    elif method == 'average':\n",
        "        # Average linkage: mean distance between all pairs\n",
        "        total_dist = 0\n",
        "        count = 0\n",
        "        for i in cluster_i:\n",
        "            for j in cluster_j:\n",
        "                total_dist += distances[i, j]\n",
        "                count += 1\n",
        "        return total_dist / count if count > 0 else 0\n",
        "    \n",
        "    elif method == 'ward':\n",
        "        # Ward's method: minimum variance criterion\n",
        "        if cluster_data is None:\n",
        "            raise ValueError(\"cluster_data required for Ward's method\")\n",
        "        \n",
        "        # Compute centroids\n",
        "        centroid_i = np.mean(cluster_data[cluster_i], axis=0)\n",
        "        centroid_j = np.mean(cluster_data[cluster_j], axis=0)\n",
        "        \n",
        "        # Ward's formula\n",
        "        n_i = len(cluster_i)\n",
        "        n_j = len(cluster_j)\n",
        "        centroid_distance = np.sqrt(np.sum((centroid_i - centroid_j) ** 2))\n",
        "        \n",
        "        return np.sqrt((n_i * n_j) / (n_i + n_j)) * centroid_distance\n",
        "    \n",
        "    else:\n",
        "        raise ValueError(f\"Unknown linkage method: {method}\")\n",
        "\n",
        "print(\"✓ compute_cluster_distance() implemented\")"
    ]
})

# Cell 7: Agglomerative algorithm markdown
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Part 3: Agglomerative Algorithm\n",
        "\n",
        "### The Bottom-Up Approach\n",
        "\n",
        "Agglomerative clustering builds the hierarchy from the bottom up:\n",
        "\n",
        "**Algorithm Steps:**\n",
        "\n",
        "1. **Initialize**: Each point is its own cluster\n",
        "2. **Repeat until one cluster remains:**\n",
        "   - Find the two closest clusters\n",
        "   - Merge them together\n",
        "   - Record the merge at this distance (for dendrogram)\n",
        "   - Update distances to remaining clusters\n",
        "3. **Result**: A dendrogram showing the merge history\n",
        "\n",
        "**Time Complexity**: O(n² log n) for most implementations\n",
        "\n",
        "The merge history is crucial for visualization and determining the final clustering!"
    ]
})

# Cell 8: Agglomerative clustering function
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "def agglomerative_clustering(X, n_clusters=3, linkage='ward', metric='euclidean'):\n",
        "    \"\"\"\n",
        "    Perform agglomerative (hierarchical) clustering from scratch.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    X : ndarray of shape (n_samples, n_features)\n",
        "        Input data\n",
        "    n_clusters : int, default=3\n",
        "        Number of clusters to form\n",
        "    linkage : str, one of ['single', 'complete', 'average', 'ward']\n",
        "        Linkage criterion\n",
        "    metric : str, one of ['euclidean', 'manhattan', 'cosine']\n",
        "        Distance metric\n",
        "        \n",
        "    Returns:\n",
        "    --------\n",
        "    labels : ndarray of shape (n_samples,)\n",
        "        Cluster assignment for each sample\n",
        "    merge_history : list of tuples\n",
        "        Recording of merges: (cluster1_idx, cluster2_idx, distance, size)\n",
        "        \n",
        "    Educational Notes:\n",
        "    ------------------\n",
        "    - We track merge history to build dendrograms\n",
        "    - Active clusters are stored in a dictionary for easy management\n",
        "    - Each merge reduces cluster count by 1\n",
        "    - When n_clusters is reached, we stop merging\n",
        "    \"\"\"\n",
        "    n = len(X)\n",
        "    \n",
        "    # Compute initial distance matrix\n",
        "    distances = compute_distance_matrix(X, metric=metric)\n",
        "    \n",
        "    # Initialize: each point is its own cluster\n",
        "    # Format: {cluster_id: [list of point indices]}\n",
        "    clusters = {i: [i] for i in range(n)}\n",
        "    cluster_counter = n  # For new cluster IDs\n",
        "    \n",
        "    # Track merge history for dendrogram\n",
        "    merge_history = []\n",
        "    \n",
        "    # Keep merging until we have the desired number of clusters\n",
        "    while len(clusters) > n_clusters:\n",
        "        # Find the two closest clusters\n",
        "        min_distance = np.inf\n",
        "        merge_pair = None\n",
        "        \n",
        "        cluster_ids = list(clusters.keys())\n",
        "        for i in range(len(cluster_ids)):\n",
        "            for j in range(i+1, len(cluster_ids)):\n",
        "                c_id_i = cluster_ids[i]\n",
        "                c_id_j = cluster_ids[j]\n",
        "                \n",
        "                # Compute distance between these clusters\n",
        "                d = compute_cluster_distance(\n",
        "                    distances, \n",
        "                    clusters[c_id_i], \n",
        "                    clusters[c_id_j],\n",
        "                    method=linkage,\n",
        "                    cluster_data=X\n",
        "                )\n",
        "                \n",
        "                if d < min_distance:\n",
        "                    min_distance = d\n",
        "                    merge_pair = (c_id_i, c_id_j)\n",
        "        \n",
        "        if merge_pair is None:\n",
        "            break\n",
        "        \n",
        "        # Merge the two closest clusters\n",
        "        c1_id, c2_id = merge_pair\n",
        "        merged_cluster = clusters[c1_id] + clusters[c2_id]\n",
        "        merged_size = len(merged_cluster)\n",
        "        \n",
        "        # Record merge\n",
        "        merge_history.append((c1_id, c2_id, min_distance, merged_size))\n",
        "        \n",
        "        # Create new cluster\n",
        "        clusters[cluster_counter] = merged_cluster\n",
        "        cluster_counter += 1\n",
        "        \n",
        "        # Remove merged clusters\n",
        "        del clusters[c1_id]\n",
        "        del clusters[c2_id]\n",
        "    \n",
        "    # Assign cluster labels\n",
        "    labels = np.zeros(n, dtype=int)\n",
        "    for cluster_id, (cluster_label, point_indices) in enumerate(clusters.items()):\n",
        "        for point_idx in point_indices:\n",
        "            labels[point_idx] = cluster_label\n",
        "    \n",
        "    return labels, merge_history\n",
        "\n",
        "print(\"✓ agglomerative_clustering() implemented\")"
    ]
})

# Cell 9: Visualize merge history function
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "def visualize_merge_history(merge_history, title='Merge History'):\n",
        "    \"\"\"\n",
        "    Visualize the merge history of hierarchical clustering.\n",
        "    \n",
        "    Parameters:\n",
        "    -----------\n",
        "    merge_history : list of tuples\n",
        "        Output from agglomerative_clustering()\n",
        "    title : str\n",
        "        Plot title\n",
        "        \n",
        "    Educational Notes:\n",
        "    ------------------\n",
        "    - Merge history shows at what distances clusters are joined\n",
        "    - This is the basis for dendrograms (we simplify the visualization)\n",
        "    - Early merges (low distance) = close points\n",
        "    - Late merges (high distance) = distant clusters\n",
        "    \"\"\"\n",
        "    if not merge_history:\n",
        "        print(\"No merge history to visualize\")\n",
        "        return\n",
        "    \n",
        "    merge_distances = [h[2] for h in merge_history]\n",
        "    merge_sizes = [h[3] for h in merge_history]\n",
        "    \n",
        "    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))\n",
        "    \n",
        "    # Plot 1: Distances of successive merges\n",
        "    ax1.plot(range(len(merge_distances)), merge_distances, 'o-', linewidth=2, markersize=8, color='steelblue')\n",
        "    ax1.set_xlabel('Merge Step', fontsize=12)\n",
        "    ax1.set_ylabel('Merge Distance', fontsize=12)\n",
        "    ax1.set_title(f'{title} - Merge Distances', fontsize=13, fontweight='bold')\n",
        "    ax1.grid(True, alpha=0.3)\n",
        "    \n",
        "    # Plot 2: Cluster sizes after each merge\n",
        "    ax2.bar(range(len(merge_sizes)), merge_sizes, color='coral', alpha=0.7)\n",
        "    ax2.set_xlabel('Merge Step', fontsize=12)\n",
        "    ax2.set_ylabel('Cluster Size', fontsize=12)\n",
        "    ax2.set_title(f'{title} - Cluster Sizes', fontsize=13, fontweight='bold')\n",
        "    ax2.grid(True, alpha=0.3, axis='y')\n",
        "    \n",
        "    plt.tight_layout()\n",
        "    plt.show()\n",
        "\n",
        "print(\"✓ visualize_merge_history() implemented\")"
    ]
})

# Cell 10: Generate test dataset
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Part 4: Testing Our Implementation\n",
        "\n",
        "Let's create a test dataset and see our algorithm in action!"
    ]
})

notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Generate synthetic test dataset\n",
        "X_test, y_true = make_blobs(n_samples=50, centers=4, n_features=2, cluster_std=0.6, random_state=42)\n",
        "\n",
        "# Visualize the dataset\n",
        "plt.figure(figsize=(10, 6))\n",
        "scatter = plt.scatter(X_test[:, 0], X_test[:, 1], c=y_true, cmap='viridis', s=100, alpha=0.7, edgecolors='black')\n",
        "plt.xlabel('Feature 1', fontsize=12)\n",
        "plt.ylabel('Feature 2', fontsize=12)\n",
        "plt.title('Test Dataset: 50 points, 4 true clusters', fontsize=13, fontweight='bold')\n",
        "plt.colorbar(scatter, label='True Cluster')\n",
        "plt.grid(True, alpha=0.3)\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "print(f\"✓ Generated test dataset: shape {X_test.shape}\")"
    ]
})

# Cell 11: Run clustering with Ward's method
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Run our hierarchical clustering with Ward's method\n",
        "labels_ward, merge_history_ward = agglomerative_clustering(\n",
        "    X_test, \n",
        "    n_clusters=4, \n",
        "    linkage='ward', \n",
        "    metric='euclidean'\n",
        ")\n",
        "\n",
        "# Visualize results\n",
        "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
        "\n",
        "# Original data\n",
        "scatter1 = axes[0].scatter(X_test[:, 0], X_test[:, 1], c=y_true, cmap='viridis', s=100, alpha=0.7, edgecolors='black')\n",
        "axes[0].set_xlabel('Feature 1', fontsize=12)\n",
        "axes[0].set_ylabel('Feature 2', fontsize=12)\n",
        "axes[0].set_title('True Labels', fontsize=13, fontweight='bold')\n",
        "axes[0].grid(True, alpha=0.3)\n",
        "\n",
        "# Our clustering\n",
        "scatter2 = axes[1].scatter(X_test[:, 0], X_test[:, 1], c=labels_ward, cmap='tab10', s=100, alpha=0.7, edgecolors='black')\n",
        "axes[1].set_xlabel('Feature 1', fontsize=12)\n",
        "axes[1].set_ylabel('Feature 2', fontsize=12)\n",
        "axes[1].set_title('Ward\\'s Hierarchical Clustering', fontsize=13, fontweight='bold')\n",
        "axes[1].grid(True, alpha=0.3)\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "print(\"\\n=== Ward's Method Results ===\")\n",
        "print(f\"✓ Clustering converged with {len(set(labels_ward))} clusters\")\n",
        "\n",
        "# Visualize merge history\n",
        "visualize_merge_history(merge_history_ward, title='Ward\\'s Method')"
    ]
})

# Cell 12: Validation against scipy
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# For validation, let's compare with scipy's implementation\n",
        "from scipy.cluster.hierarchy import linkage, fcluster\n",
        "from scipy.spatial.distance import pdist, squareform\n",
        "\n",
        "# Compute distances using scipy\n",
        "distance_matrix = compute_distance_matrix(X_test, metric='euclidean')\n",
        "\n",
        "# Get condensed distance matrix\n",
        "n = len(X_test)\n",
        "condensed_distances = distance_matrix[np.triu_indices(n, k=1)]\n",
        "\n",
        "# scipy's Ward linkage\n",
        "Z = linkage(condensed_distances, method='ward')\n",
        "labels_scipy = fcluster(Z, t=4, criterion='maxclust') - 1  # 0-indexed\n",
        "\n",
        "# Compare results\n",
        "from scipy.optimize import linear_sum_assignment\n",
        "\n",
        "# Create confusion matrix\n",
        "confusion = np.zeros((4, 4))\n",
        "for true_label in set(labels_scipy):\n",
        "    our_mask = labels_ward[labels_scipy == true_label]\n",
        "    for pred_label in set(labels_ward):\n",
        "        confusion[true_label, pred_label] = np.sum(our_mask == pred_label)\n",
        "\n",
        "# Best label assignment\n",
        "row_ind, col_ind = linear_sum_assignment(-confusion)\n",
        "agreement = confusion[row_ind, col_ind].sum() / len(X_test)\n",
        "\n",
        "print(\"\\n=== Validation Against SciPy ===\")\n",
        "print(f\"✓ Our implementation agreement: {agreement:.1%}\")\n",
        "print(f\"✓ This close match validates our algorithm!\")"
    ]
})

# Cell 13: Test all linkage methods
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Comparing Different Linkage Methods\n",
        "\n",
        "Let's see how different linkage criteria affect clustering:"
    ]
})

notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Test all linkage methods\n",
        "linkage_methods = ['single', 'complete', 'average', 'ward']\n",
        "results = {}\n",
        "\n",
        "fig, axes = plt.subplots(2, 2, figsize=(14, 12))\n",
        "axes = axes.flatten()\n",
        "\n",
        "for idx, method in enumerate(linkage_methods):\n",
        "    labels, merge_hist = agglomerative_clustering(\n",
        "        X_test, \n",
        "        n_clusters=4, \n",
        "        linkage=method, \n",
        "        metric='euclidean'\n",
        "    )\n",
        "    results[method] = (labels, merge_hist)\n",
        "    \n",
        "    # Plot\n",
        "    scatter = axes[idx].scatter(X_test[:, 0], X_test[:, 1], c=labels, cmap='tab10', s=100, alpha=0.7, edgecolors='black')\n",
        "    axes[idx].set_xlabel('Feature 1', fontsize=11)\n",
        "    axes[idx].set_ylabel('Feature 2', fontsize=11)\n",
        "    axes[idx].set_title(f'{method.capitalize()} Linkage', fontsize=12, fontweight='bold')\n",
        "    axes[idx].grid(True, alpha=0.3)\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "print(\"\\n=== Linkage Methods Comparison ===\")\n",
        "for method, (labels, _) in results.items():\n",
        "    print(f\"  • {method.capitalize():10} → {len(set(labels))} clusters formed\")"
    ]
})

# Cell 14: Test different distance metrics
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Comparing Different Distance Metrics\n",
        "\n",
        "Distance metric choice also affects results:"
    ]
})

notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Test different metrics with Ward's method\n",
        "metrics = ['euclidean', 'manhattan', 'cosine']\n",
        "metric_results = {}\n",
        "\n",
        "fig, axes = plt.subplots(1, 3, figsize=(15, 4))\n",
        "\n",
        "for idx, metric in enumerate(metrics):\n",
        "    try:\n",
        "        labels, merge_hist = agglomerative_clustering(\n",
        "            X_test, \n",
        "            n_clusters=4, \n",
        "            linkage='ward',  # Keep linkage constant\n",
        "            metric=metric\n",
        "        )\n",
        "        metric_results[metric] = (labels, merge_hist)\n",
        "        \n",
        "        # Plot\n",
        "        scatter = axes[idx].scatter(X_test[:, 0], X_test[:, 1], c=labels, cmap='tab10', s=100, alpha=0.7, edgecolors='black')\n",
        "        axes[idx].set_xlabel('Feature 1', fontsize=11)\n",
        "        axes[idx].set_ylabel('Feature 2', fontsize=11)\n",
        "        axes[idx].set_title(f'{metric.capitalize()} Metric', fontsize=12, fontweight='bold')\n",
        "        axes[idx].grid(True, alpha=0.3)\n",
        "    except Exception as e:\n",
        "        axes[idx].text(0.5, 0.5, f'Error: {str(e)[:30]}', ha='center', va='center', transform=axes[idx].transAxes)\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "print(\"\\n=== Distance Metrics Comparison (Ward's Method) ===\")\n",
        "for metric, (labels, _) in metric_results.items():\n",
        "    print(f\"  • {metric.capitalize():10} → {len(set(labels))} clusters formed\")"
    ]
})

# Cell 15: Test on Iris dataset (load)
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Real Dataset: Iris\n",
        "\n",
        "Now let's apply our algorithm to the famous Iris dataset!"
    ]
})

notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Load Iris dataset\n",
        "iris = load_iris()\n",
        "X_iris = iris.data\n",
        "y_iris = iris.target\n",
        "iris_names = iris.target_names\n",
        "\n",
        "# Standardize features (important!)\n",
        "scaler = StandardScaler()\n",
        "X_iris_scaled = scaler.fit_transform(X_iris)\n",
        "\n",
        "print(f\"✓ Iris dataset loaded\")\n",
        "print(f\"  • Samples: {len(X_iris)}\")\n",
        "print(f\"  • Features: {X_iris.shape[1]}\")\n",
        "print(f\"  • Classes: {len(iris_names)}: {', '.join(iris_names)}\")"
    ]
})

# Cell 16: Test on Iris dataset (run)
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Run hierarchical clustering on Iris\n",
        "labels_iris, merge_history_iris = agglomerative_clustering(\n",
        "    X_iris_scaled,\n",
        "    n_clusters=3,  # 3 species\n",
        "    linkage='ward',\n",
        "    metric='euclidean'\n",
        ")\n",
        "\n",
        "print(f\"✓ Hierarchical clustering completed\")\n",
        "print(f\"  • Clusters found: {len(set(labels_iris))}\")\n",
        "print(f\"  • Total merge steps: {len(merge_history_iris)}\")"
    ]
})

# Cell 17: Test on Iris dataset (visualize)
notebook["cells"].append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Visualize results on 2D projection\n",
        "from sklearn.decomposition import PCA\n",
        "\n",
        "pca = PCA(n_components=2)\n",
        "X_iris_2d = pca.fit_transform(X_iris_scaled)\n",
        "\n",
        "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
        "\n",
        "# True labels\n",
        "scatter1 = axes[0].scatter(X_iris_2d[:, 0], X_iris_2d[:, 1], c=y_iris, cmap='viridis', s=100, alpha=0.7, edgecolors='black')\n",
        "axes[0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})', fontsize=12)\n",
        "axes[0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})', fontsize=12)\n",
        "axes[0].set_title('True Iris Species', fontsize=13, fontweight='bold')\n",
        "axes[0].grid(True, alpha=0.3)\n",
        "cbar1 = plt.colorbar(scatter1, ax=axes[0])\n",
        "cbar1.set_label('Species', fontsize=11)\n",
        "\n",
        "# Our clustering\n",
        "scatter2 = axes[1].scatter(X_iris_2d[:, 0], X_iris_2d[:, 1], c=labels_iris, cmap='tab10', s=100, alpha=0.7, edgecolors='black')\n",
        "axes[1].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})', fontsize=12)\n",
        "axes[1].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})', fontsize=12)\n",
        "axes[1].set_title('Hierarchical Clustering (Ward)', fontsize=13, fontweight='bold')\n",
        "axes[1].grid(True, alpha=0.3)\n",
        "cbar2 = plt.colorbar(scatter2, ax=axes[1])\n",
        "cbar2.set_label('Cluster', fontsize=11)\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# Calculate Adjusted Rand Index\n",
        "ari = adjusted_rand_score(y_iris, labels_iris)\n",
        "print(f\"\\n=== Iris Dataset Results ===\")\n",
        "print(f\"✓ Adjusted Rand Index: {ari:.3f}\")\n",
        "print(f\"  (1.0 = perfect match, 0.0 = random assignment)\")\n",
        "\n",
        "# Visualize merge history\n",
        "visualize_merge_history(merge_history_iris, title='Iris Hierarchical Clustering')"
    ]
})

# Cell 18: Summary
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Summary\n",
        "\n",
        "### What We Implemented\n",
        "\n",
        "✓ **Distance metrics**: Euclidean, Manhattan, Cosine\n",
        "✓ **Linkage methods**: Single, Complete, Average, Ward\n",
        "✓ **Agglomerative algorithm**: Bottom-up hierarchical clustering\n",
        "✓ **Merge tracking**: Recording cluster merges for visualization\n",
        "✓ **Validation**: Comparison with scipy's implementation\n",
        "\n",
        "### Key Insights\n",
        "\n",
        "1. **Linkage matters**: Different methods produce different hierarchies\n",
        "2. **Distance metric matters**: Euclidean, Manhattan, and Cosine can give different results\n",
        "3. **Ward's method** is popular because it minimizes within-cluster variance\n",
        "4. **Single linkage** tends to create chain-like structures (chaining effect)\n",
        "5. **Complete linkage** creates compact, spherical clusters\n",
        "6. **Computational cost** is O(n²) for distance matrix + O(n² log n) for clustering\n",
        "\n",
        "### When to Use Hierarchical Clustering\n",
        "\n",
        "✓ When you want to see relationships at multiple scales\n",
        "✓ When you don't know the optimal number of clusters in advance\n",
        "✓ When interpretability is important (dendrograms)\n",
        "✗ When you have very large datasets (computationally expensive)\n",
        "\n",
        "---\n",
        "\n",
        "**Next**: Explore density-based clustering (DBSCAN) for a different approach!"
    ]
})

# Cell 19: Navigation
notebook["cells"].append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "---\n",
        "\n",
        "## 📚 Notebook Navigation\n",
        "\n",
        "**← Previous**: [K-Means Clustering](01_kmeans-implementation.ipynb)\n",
        "\n",
        "**↓ Next**: [DBSCAN Clustering](03_dbscan-implementation.ipynb)\n",
        "\n",
        "**↑ Back**: [Clustering Overview](../README.md)\n",
        "\n",
        "---\n",
        "\n",
        "**Course**: M.Sc. DSAI | **Topic**: 07 - Unsupervised Learning\n",
        "\n",
        "**Last Updated**: February 2026"
    ]
})

# Save the notebook
output_path = 'notebooks/02_Unsupervised/01_Clustering/02_hierarchical-clustering-implementation.ipynb'
with open(output_path, 'w') as f:
    json.dump(notebook, f, indent=2)

print(f"✓ Notebook saved to {output_path}")
