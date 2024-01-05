def to_array(data):

    res = []

    for obj in data:
        obj['gallery'] = obj['gallery'].split(",")
        res.append(obj)
        
    return res

def to_string(data):
    
    data['gallery'] = ','.join(data['gallery'])

    return data['gallery']