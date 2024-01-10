CREATE TABLE sale_clothes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    size TEXT NOT NULL,
    measurements TEXT NOT NULL,
    gender TEXT NOT NULL,
    price INTEGER NOT NULL,
    notes TEXT,
    thumbnail TEXT NOT NULL,
    gallery TEXT NOT NULL
)

CREATE TABLE sold_clothes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    size TEXT NOT NULL,
    measurements TEXT NOT NULL,
    gender TEXT NOT NULL,
    notes TEXT,
    thumbnail TEXT NOT NULL,
    gallery TEXT NOT NULL
)

--- test postman request body: {"title":"new","description":"desc","category":"CT","size":"S","measurements":"me","gender":"M","price":1,"notes":"n","thumbnail":"h","gallery":"hi,bye,cry,die"}