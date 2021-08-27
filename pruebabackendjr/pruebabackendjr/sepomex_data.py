import xlrd 
from info.models import Estado, Municipio, Colonia
from pruebabackendjr.task import task

def load_data(self):
    print('hola')
    task()
    return self