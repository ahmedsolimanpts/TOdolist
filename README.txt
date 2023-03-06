# TODO LIST

- " host/api/task/ " :
    method:
        - GET , POST
    description:
        - can send get to the url to get all tasks
        - can send post to the url to add new task
    Request Json For POST :
            {
                "id": , # NUMBER ITERATOR_CREATE_BY_DEFAULT
                "description": "", # STRING OPTIONAL
                "status": "", # STRING REQUIERD
                "name": "", # STRING REQUIERD
                "created_at": "", # DATE_TIME CREATE_BY_DEFAULT
                "day": "2020-01-01" # DATE REQUIERD
            }
- " host/api/task/pk :
    meta_data:
        - pk in the url is the primary key for the record to update or delete or retreive"Dynamic"
    method:
        - GET , PUT ,DELETE
    description:
        - can send GET to the url to get specific task with match id
        - can send PUT to the url to add update task
        - can send DELETE to the url to add delete task

    Request Json For PUT :
            {
                "id": , # NUMBER ITERATOR_CREATE_BY_DEFAULT
                "description": "", # STRING OPTIONAL
                "status": "", # STRING REQUIERD
                "name": "", # STRING REQUIERD
                "created_at": "", # DATE_TIME CREATE_BY_DEFAULT
                "day": "2020-01-01" # DATE REQUIERD
            }