import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    assignments = []
    
    for p in points:
        min_dist = float('inf')
        closest_idx = 0

        for i, c in enumerate(centroids):
            squared_dist = 0
            for d in range(len(p)):
                squared_dist += (p[d] - c[d]) ** 2
            
            if squared_dist < min_dist:
                min_dist = squared_dist
                closest_idx = i
        
        assignments.append(closest_idx)
        
    return assignments