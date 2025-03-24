# serializer for a single todo
def individual_serial(todo) -> dict:

    return {
        "id": str(todo["_id"]),
        "title": str(todo["title"]),
        "description": str(todo["description"]),
        "completed": bool(todo["completed"]),
    }

#Serializer for all todo lists
def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
