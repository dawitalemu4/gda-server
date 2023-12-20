def sold_clothes_urls():

    getAllClothes: str
    getClothingByID: str
    createClothing: str
    updateClothing: str
    deleteClothing: str

    urls = {
        getAllClothes: "/sold_clothes",
        getClothingByID: "/sold_clothes/<int:id>",
        createClothing: "/sold_clothes/new",
        updateClothing: "/sold_clothes/update",
        deleteClothing: "/sold_clothes/delete"
    }

    return urls