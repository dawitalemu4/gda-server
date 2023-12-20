def sale_clothes_urls():

    getAllClothes: str
    getClothingByID: str
    createClothing: str
    updateClothing: str
    deleteClothing: str

    urls = {
        getAllClothes: "/sale_clothes",
        getClothingByID: "/sale_clothes/<int:id>",
        createClothing: "/sale_clothes/new",
        updateClothing: "/sale_clothes/update",
        deleteClothing: "/sale_clothes/delete"
    }

    return urls