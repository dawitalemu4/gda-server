from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import json
from ..models.sale_clothes_model import sale_clothes_model
from ..utils.db import db
from ..utils.to_json import convert_data_to_json

class sale_clothes_queries(viewsets.ViewSet):
    
    def get_all_clothes(self, request):

        try:
            all_clothes = db.execute("SELECT * FROM sale_clothes")

            if all_clothes == 0:
                return Response("No clothing found.", status=status.HTTP_400_BAD_REQUEST)
            
            else:
                res = db.fetchall()
                all_clothes_data = convert_data_to_json(res, "sale")
                return Response(all_clothes_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def get_clothing_by_id(self, request, id):

        try:
            clothing_by_id = db.execute("SELECT * FROM sale_clothes WHERE id = %s", (id))
            
            if clothing_by_id == 0:
                return Response("No clothing with this id found.", status=status.HTTP_400_BAD_REQUEST)
            
            else:
                res = db.fetchall()
                clothing_by_id_data = convert_data_to_json(res, "sale")    
                return Response(clothing_by_id_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def create_clothing(self, request):
        
        try:
            input = sale_clothes_model(request.body)

            if input.validate():
                data = json.loads(request.body)
                print(json.loads(request.body))
                db.execute("INSERT INTO sale_clothes (title, description, category, size, measurements, gender, price, notes, thumbnail, gallery) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (data.title, data.description, data.category, data.size, data.measurements, data.gender, data.price, data.notes, data.thumbnail, data.gallery))
                return Response("Created Sucessfully", status=status.HTTP_201_CREATED)
            
            else:
                return Response("Could not insert clothing into database", status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def update_clothing(self, request, id):
        
        try:
            data = sale_clothes_model(request.body)
            
            if data.validate():
                db.execute("UPDATE sale_clothes SET title = %s, description = %s, category = %s, size = %s, measurements = %s, gender = %s, price = %s, notes = %s, thumbnail = %s, gallery = %s WHERE id = %s",
                (data.title, data.description, data.category, data.size, data.measurements, data.gender, data.price, data.notes, data.thumbnail, data.gallery, id))
                return Response("Update Sucessfully", status=status.HTTP_200_OK) 
           
            else:
                return Response("Could not complete this update request.", status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def delete_clothing(self, request, id):
        
        try:
            delete_clothing = db.execute("DELETE FROM sale_clothes WHERE id = %s", (id))
  
            if delete_clothing == 0:    
                return Response("Could not find clothing with this id to delete.", status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response("The piece of clothing was deleted from the database", status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)