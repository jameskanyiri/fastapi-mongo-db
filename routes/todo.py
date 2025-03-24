from fastapi import APIRouter
from config.database import todo_collection
from schema.todo_schema import list_serial, individual_serial
from models.todos import Todo
from bson import ObjectId

todo_router = APIRouter()

#Get all todo list
@todo_router.get("/todos")
async def get_all_todos():
    
    #fetch all the todos
    todos = todo_collection.find()
    
    #serialize the data
    data = list_serial(todos)
    
    #prepare response
    response =  {
        "success": "true",
        "message": "Todo list successfully retrieved",
        "data": data
    }
    
    #return response
    return response
    

#Create a new todo list
@todo_router.post("/todos/create")
async def create_todo(todo: Todo):
    
    #insert the todo into the database
    result =  todo_collection.insert_one(dict(todo))
    
    #retrieve inserted document
    inserted_document = todo_collection.find_one({"_id": result.inserted_id})
    
    #serialize the data
    todo = individual_serial(inserted_document)
    
    #prepare response
    response = {
        "success": "true",
        "message": "Todo created successfully",
        "data": todo
    }
    
    #return response
    return response

@todo_router.put("/todos/update/{id}")
async def update_todo(id: str, todo: Todo):
    #Check if the todo exist
    todo_exists = todo_collection.find_one({"_id": ObjectId(id)})
    
    if todo_exists:
        #update the todo in the database
        result = todo_collection.update_one({"_id": ObjectId(id)}, {"$set": dict(todo)})
        
        #retrieve updated document
        updated_document = todo_collection.find_one({"_id": ObjectId(id)})
        
        #serialize the data
        todo = individual_serial(updated_document)
        
        #prepare response
        response = {
            "success": "true",
            "message": "Todo updated successfully",
            "data": todo
        }
        
        #return response
        return response
    else:
        #prepare response
        response = {
            "success": "false",
            "message": "Todo not found"
        }
        
        #return response
        return response
    
    
@todo_router.delete("/todo/delete/{id}")
async def delete_todo(id: str):
    #Check if the todo exist
    todo_exist = todo_collection.find_one({"_id": ObjectId(id)})
    
    if todo_exist:
        #Delete the todo
        result = todo_collection.delete_one({"_id": ObjectId(id)})
        
        #prepare response
        response = {
            "success": "true",
            "message": "Todo deleted successfully"
        }
        
        #return response
        return response
    
    else:
        #prepare response
        response = {
            "success": "false",
            "message": "Todo not found"
        }
        
        #return response
        return response