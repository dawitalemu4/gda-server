This API was built with [**Django**](https://www.djangoproject.com/), [**Django Rest Framework**](https://www.django-rest-framework.org/), and [**GraphQL**](https://graphql.org/) [**(Graphene)**](https://docs.graphene-python.org/en/latest/) connected to a MySQL database for an e-commerce site that sells and displays traditional ethiopian clothing called [Genet's Designs and Alterations](https://genetdesigns.vercel.app), a small business run by a tailor named Genet Bekele.

# GraphQL Examples

Our use case for GraphQL was to easily filter through sale_/sold_clothes data using the different filter options defined in our models, which is the `schema.py`. This data is then sent to our Remix.js (React) frontend.

    CATEGORIES = [
        ("CT", "Clothing, Top"),
        ("CB", "Clothing, Bottom"),
        ("CO", "Clothing, Other"),
        ...
    ]
    SIZES = [
        ("XXS", "Extra Extra Small"),
        ("XS", "Extra Small"),
        ("S", "Small"),
        ...
    ]
    GENDERS = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unisex")
    ]

### Example of fetching all from the sale_clothes table:

![gql](https://github.com/GDA-dev/GDAserver/assets/106638403/f2617f87-23f1-4a23-8774-e88d078b5478)

### Example of GraphQL type (Django model) being applied properly:

![gqlError](https://github.com/GDA-dev/GDAserver/assets/106638403/5321e172-eba2-4e66-a4d0-caad2d321e22)

# DRF Examples

Following this routing schema:

    x_clothes_urls = {
        "get_all_clothes": "x_clothes/",
        "get_clothing_by_id": "x_clothes/id/<str:id>/",
        "create_clothing": "x_clothes/new/",
        "update_clothing": "x_clothes/update/<str:id>/",
        "delete_clothing": "x_clothes/delete/<str:id>/"
    }

## Get All

![GET](https://github.com/GDA-dev/GDAserver/assets/106638403/09977281-0642-4a4a-86b1-964f6d32d754)

## Get By id

![GET by id](https://github.com/GDA-dev/GDAserver/assets/106638403/651bae25-b55a-4919-bb93-41e3817700f6)

## Create

![POST](https://github.com/GDA-dev/GDAserver/assets/106638403/9ffde1f7-d7ee-4f30-bde8-56f5439a3776)

## Update (PUT)

![PUT](https://github.com/GDA-dev/GDAserver/assets/106638403/df7fc247-c908-42f7-b60e-affb413d6cee)

## Delete

![DELETE](https://github.com/GDA-dev/GDAserver/assets/106638403/bb646762-c7be-4040-8d90-d25a1fbdaaa4)


# Notes

To start the Django live server, use the `local` branch and run `python manage.py runserver`.

The `main` and `dev` branches are tweaked for Vercel's serverless deployment and don't work locally. 

Built by Genet Bekele's nephew [Michael Girma](https://github.com/michaelgirma) and his friends.