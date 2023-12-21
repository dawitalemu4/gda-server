def sale_clothes_urls():

    get_all_clothes: str
    get_clothing_by_id: str
    create_clothing: str
    update_clothing: str
    delete_clothing: str

    urls = {
        get_all_clothes: "/sale_clothes",
        get_clothing_by_id: "/sale_clothes/<int:id>",
        create_clothing: "/sale_clothes/new",
        update_clothing: "/sale_clothes/update",
        delete_clothing: "/sale_clothes/delete"
    }

    return urls