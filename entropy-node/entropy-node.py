import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # 1. Nếu mảng rỗng, độ hỗn loạn bằng 0
    if len(y) == 0:
        return 0.0
    
    # 2. Tìm các giá trị duy nhất và số lần xuất hiện (counts) của chúng
    _, counts = np.unique(y, return_counts=True)
    
    # 3. Tính tỷ lệ (probabilities) p_i
    probabilities = counts / len(y)
    
    # 4. Tính Entropy: -sum(p * log2(p))
    # Sử dụng np.log2 trên các giá trị p > 0 để đảm bảo tính ổn định (stable)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    
    return float(entropy)