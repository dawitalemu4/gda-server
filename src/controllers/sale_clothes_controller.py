from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import json
from ..models.sale_clothes_model import sale_clothes_model
from ..utils.db import connection, db
from ..utils.map_object import map_object

class sale_clothes_queries(viewsets.ViewSet):

    keys = ['id', 'title', 'description', 'category', 'size', 'measurements', 'gender', 'price', 'notes', 'thumbnail', 'gallery']

    def get_all_clothes(self, request):

        try:
            db.execute("SELECT * FROM sale_clothes")
            all_clothes = db.fetchall()

            if len(all_clothes) == 0:
                return Response("No clothing found.", status=status.HTTP_200_OK)

            else:
                res = [map_object(clothing, self.keys) for clothing in all_clothes]
                connection.commit()
                return Response(res, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_clothing_by_id(self, request, id):

        try:
            db.execute("SELECT * FROM sale_clothes WHERE id = " + id)
            clothing_by_id = db.fetchone()

            if clothing_by_id == None:
                return Response("No clothing with this id found.", status=status.HTTP_400_BAD_REQUEST)

            else:
                res = map_object(clothing_by_id, self.keys)
                connection.commit()
                return Response(res, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create_clothing(self, request):

        try:
            data = json.loads(request.body)
            input = sale_clothes_model(title=data['title'], description=data['description'], category=data['category'], size=data['size'], measurements=data['measurements'], gender=data['gender'], price=data['price'], notes=data['notes'], thumbnail=data['thumbnail'], gallery=data['gallery'])

            if input.validate():
                db.execute("INSERT INTO sale_clothes (title, description, category, size, measurements, gender, price, notes, thumbnail, gallery) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (data['title'], data['description'], data['category'], data['size'], data['measurements'], data['gender'], data['price'], data['notes'], data['thumbnail'], data['gallery']))
                connection.commit()
                return Response("Created Successfully", status=status.HTTP_201_CREATED)

            else:
                return Response("Could not insert clothing into database, input is not valid.", status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update_clothing(self, request, id):

        try:
            data = json.loads(request.body)
            input = sale_clothes_model(title=data['title'], description=data['description'], category=data['category'], size=data['size'], measurements=data['measurements'], gender=data['gender'], price=data['price'], notes=data['notes'], thumbnail=data['thumbnail'], gallery=data['gallery'])

            if input.validate():
                db.execute("UPDATE sale_clothes SET title = %s, description = %s, category = %s, size = %s, measurements = %s, gender = %s, price = %s, notes = %s, thumbnail = %s, gallery = %s WHERE id = %s",
                (data['title'], data['description'], data['category'], data['size'], data['measurements'], data['gender'], data['price'], data['notes'], data['thumbnail'], data['gallery'], id))
                connection.commit()
                return Response("Updated Successfully", status=status.HTTP_200_OK)

            else:
                return Response("Could not complete this update request, input is not valid.", status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete_clothing(self, request, id):

        try:
            delete_clothing = db.execute("DELETE FROM sale_clothes WHERE id = " + id)

            if delete_clothing.rowcount == 0:
                return Response("Could not find clothing with this id to delete.", status=status.HTTP_400_BAD_REQUEST)

            else:
                connection.commit()
                return Response("The piece of clothing was deleted from the database", status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
