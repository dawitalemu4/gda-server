def sold_clothes_urls():

    get_all_clothes: str
    get_clothing_by_id: str
    create_clothing: str
    update_clothing: str
    delete_clothing: str

    urls = {
        get_all_clothes: "/sold_clothes",
        get_clothing_by_id: "/sold_clothes/<int:id>",
        create_clothing: "/sold_clothes/new",
        update_clothing: "/sold_clothes/update",
        delete_clothing: "/sold_clothes/delete"
    }

    return urls