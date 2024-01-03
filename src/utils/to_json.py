def convert_data_to_json(data, type):

    if type == "sold":

        col = ["id", "title", "description", "category", "size", "measurements", "gender", "notes", "thumbnail", "gallery"]
        res = []

        for i in data:
            item = dict(zip(col, i))
            item['gallery'] = item['gallery'].split(",") 
            res.append(item)

        return res
        
    elif type == "sale":
        
        col = ["id", "title", "description", "category", "size", "measurements", "gender", "price", "notes", "thumbnail", "gallery"]
        res = []

        for i in data:
            item = dict(zip(col, i))
            item['gallery'] = item['gallery'].split(",") 
            res.append(item)

        return res
