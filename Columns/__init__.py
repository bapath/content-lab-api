import azure.functions as func
from database_connector import Database

db = Database()
app = func.FunctionApp()

def main(req: func.HttpRequest) -> func.HttpResponse:
    table_name = req.headers.get('table_name')
    return  func.HttpResponse(f"{db.get_column_names(table_name)}")
    