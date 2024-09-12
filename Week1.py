# Implementasi Normalisasi
def norm_data(data):
    '''
    Melakukan normalisasi data.
    
    Parameters:
        data (list): Data yang akan dinormalisasi
        
    Returns:
        data (list): Data hasil normalisasi    
    '''
    
    data_max = max(data)
    data_min = min(data)
    data_len = len(data)
    
    for i in range(0, data_len):
        data[i] = (data[i] - data_min) / (data_max - data_min)
        
    return data