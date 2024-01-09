This API was built with [**Django**](https://www.djangoproject.com/) and the [**Django Rest Framework**](https://www.django-rest-framework.org/) for an e-commerce site that sells and displays traditional ethiopian clothing called [Genet's Designs and Alterations](https://genetdesigns.vercel.app), a small business run by a tailor named Genet .

# Examples

Following this routing schema:

    x_clothes_urls = {
        "get_all_clothes": "x_clothes/",
        "get_clothing_by_id": "x_clothes/id/<str:id>/",
        "create_clothing": "x_clothes/new/",
        "update_clothing": "x_clothes/update/<str:id>/",
        "delete_clothing": "x_clothes/delete/<str:id>/"
    }

## Get All

## Get By id

## Create

## Update (PUT)

## Delete

To start the live server, use the local branch and run `python manage.py runserver`

Built by Genet's nephew [Michael Girma](https://github.com/michaelgirma) and his friends.