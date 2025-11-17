Objectif: make CRUD operations using FastAPI

- Setup a mini database to test the operations

- define a model (User model used here)

- Set config for app to communicate with db through orm (SQLModel)

- Make CRUD operations (create, read, read_all, update, delete) on user model (Table)

note: for cases where "user_id" is not available, you should check if db has sent 'user data' or 'null'(None in python)
        i did it just for delete route in my case