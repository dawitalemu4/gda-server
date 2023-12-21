from django.db import connection
from django.http import HttpResponse
import logging
from ..models.sale_clothes_model import sale_clothes

class sold_clothes_queries:
    
    def get_all_clothes():
        try:
            with connection.cursor() as cursor:
                all_clothes_data = cursor.execute("SELECT * FROM sale_clothes")   
            return HttpResponse(all_clothes_data, status=200)
        except all_clothes_data.DoesNotExist:
            logging.warning("No clothing found.", status=400)
            return HttpResponse("No clothing found.")
        except Exception as e:
            logging.warning(f"Server error: {e}")
            return HttpResponse(f"Server error: {e}", status=500)
    
    def get_clothing_by_id(id):
        try:
            with connection.cursor() as cursor:
                clothing_by_id = cursor.execute("SELECT * FROM sale_clothes WHERE id = %s", [id])
            return HttpResponse(clothing_by_id, status=200)
        except clothing_by_id.DoesNotExist:
            logging.warning("No clothing with this id found.", status=400)
            return HttpResponse("No clothing with this id found.")
        except Exception as e:
            logging.warning(f"Server error: {e}")
            return HttpResponse(f"Server error: {e}", status=500)

    def create_clothing(data):
        try:
            create_clothing = sale_clothes.object.raw("INSERT INTO sale_clothes (title, description, category, size, measurements, gender, price, notes, thumbnail, gallery) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [data.title, data.description, data.category, data.size, data.measurements, data.gender, data.price, data.notes, data.thumbnail, data.gallery])
            return HttpResponse("Created Sucessfully", status=200)
        except create_clothing.DoesNotExist:
            logging.warning("Could not insert clothing into database")
            return HttpResponse("Could not insert clothing into database", status=400)
        except Exception as e:
            logging.warning(f"Server error: {e}")
            return HttpResponse(f"Server error: {e}", status=500)
    
    def update_clothing(id, data):
        try:
            update_clothing = sale_clothes.object.raw("UPDATE sale_clothes SET title = %s, description = %s, category = %s, size = %s, measurements = %s, gender = %s, price = %s, notes = %s, thumbnail = %s, gallery = %s WHERE id = %s", [id])
            return HttpResponse("Update Sucessfully", status=200) 
        except update_clothing.DoesNotExist:
            logging.warning("Could not complete this update request.")
            return HttpResponse("Could not complete this update request.", status=400)
        except Exception as e:
            logging.warning(f"Server error: {e}")
            return HttpResponse(f"Server error: {e}", status=500)
    
    def delete_clothing(id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE sale_clothes WHERE id = %s", [id])
        except sale_clothes.DoesNotExist:    
            logging.warning("Could not find clothing with this id to delete.")
            return HttpResponse("Could not find clothing with this id to delete.", status=400)
        except Exception as e:
            logging.warning(f"Server error: {e}")
            return HttpResponse(f"Server error: {e}", status=500)