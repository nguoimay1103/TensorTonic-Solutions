import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.empty((0,0),dtype=int)
    if max_len is None:
        L = max(len(seq) for seq in seqs)
    else:
        L = max_len
    N = len(seqs)
    result = np.full((N, L), pad_value, dtype=int)
    for i, seq in enumerate(seqs):
        # Lấy chiều dài cần copy (giới hạn bởi L để cắt bớt nếu chuỗi quá dài)
        copy_len = min(len(seq), L)
        
        # Chỉ copy nếu có dữ liệu để tránh lỗi khi chuỗi con rỗng
        if copy_len > 0:
            result[i, :copy_len] = seq[:copy_len]
            
    return result