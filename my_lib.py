
def list_avg(vals):
    if vals == None:
        return None
    if vals == []:
        return None
    if not isinstance(vals,list):
        raise TypeError("Not correct data type")
    
    total = 0.0
    
    for val in vals:
        total += val
        
    avg = total/len(vals)
    return avg

def load_sample():
    filename = 'test.csv'
    open(filename)
    return None