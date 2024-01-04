from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from ..models.admin_model import admin_model
from ..utils.db import db

class admin_queries(viewsets.ViewSet):

    def check_credentials(self, request, name, password):
        try:
            creds = admin_model(name=name, password=password)

            if creds.validate():
                res = db.execute("SELECT * FROM admin WHERE name = %s AND password = %s", (name, password))

                if res == 0:
                    return Response({'res': "Incorrect name and password combination"}, status=status.HTTP_403_FORBIDDEN)
                
                else:
                    return Response({'res': 'true'}, status=status.HTTP_200_OK)
                
            else:
                return Response({'res': "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'res': f"Server error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)