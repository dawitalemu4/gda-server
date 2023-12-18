def clothes_urls():

    getAllClothes: str
    getClothingByID: str
    createClothing: str
    updateClothing: str
    deleteClothing: str

    url = {
        getAllClothes: "/clothes",
        getClothingByID: "/clothes/<id>",
        createClothing: "/clothes/new",
        updateClothing: "/clothes/update",
        deleteClothing: "/clothes/delete"
    }

    return url