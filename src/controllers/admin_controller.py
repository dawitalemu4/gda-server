from models.admin_model import admin

class admin_queries:

    def check_credentials():
        admin.objects.raw("SELECT * FROM myapp_person")