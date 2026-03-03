def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    dimension_count = len(points[0]) if points else 0
    new_centroids = []
    for cluster_idx in range(k):
        cluster_points = [points[i] for i in range(len(points)) if assignments[i] == cluster_idx]
        if cluster_points:
            centroid = [sum(dimension) / len(dimension) for dimension in zip(*cluster_points)]
            new_centroids.append(centroid)
        else:
            new_centroids.append([0.0] * dimension_count)
    return new_centroids