import json

def convert_data_to_json(data, type):
    if type == "sold":
        col = ["id", "title", "description", "category", "size", "measurements", "gender", "notes", "thumbnail", "gallery"]
        arr = []

        for i in data:
            item = dict(zip(col, i))
            item['gallery'] = json.loads(item['gallery'])
            arr.append(item)

        res = json.dumps(arr)
        return res
        
    elif type == "sale":
        col = ["id", "title", "description", "category", "size", "measurements", "gender", "price", "notes", "thumbnail", "gallery"]
        arr = []

        for i in data:
            item = dict(zip(col, i))
            item['price'] = int(item['price'])
            item['gallery'] = []
            arr.append(item)

        res = json.dumps(arr)
        return res
