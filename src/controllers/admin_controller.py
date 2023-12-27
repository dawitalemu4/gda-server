from rest_framework import viewsets
from rest_framework.response import Response
import logging
from ..models.admin_model import admin

class admin_queries(viewsets.ModelViewSet):

    def check_credentials(creds):
        try:
            admin.objects.raw("SELECT * FROM admin WHERE email = %s AND password = %s", 
            [creds.email, creds.password])
            return Response('true', status=200)
        except creds.DoesNotExist:
            logging.warning("Incorrect email and password combination")
            return Response("Incorrect email and password combination", status=400)
        except Exception as e:
            logging.warning(f"Server error: {e}")
            return Response(f"Server error: {e}", status=500)