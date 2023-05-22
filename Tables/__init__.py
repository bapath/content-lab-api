import azure.functions as func
import logging
from database_connector import Database

db = Database()
app = func.FunctionApp()

def main(req: func.HttpRequest) -> func.HttpResponse:
    return  func.HttpResponse(f"{db.get_table_names()}")