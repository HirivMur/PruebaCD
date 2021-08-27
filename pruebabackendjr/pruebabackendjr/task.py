import xlrd 
import threading
from info.models import Estado, Municipio, Colonia
class task:
    load_data_task = None

    def __init__(self) -> None:
        self.load_data_task = threading.Thread(name='run', target=self.run)
        self.load_data_task.start()

    def run(self):
        file = 'CPdescarga.xls'
        
        file_export = xlrd.open_workbook(file) 
        for sheet in file_export.sheets():
            if sheet.name=='Nota':
                continue
            else:
                try:
                    if Estado.objects.filter(d_estado=sheet.name).exists() ==  False:
                        e= Estado(d_estado=sheet.name)
                        e.save()
                    for i in range(1,sheet.nrows):
                        #print(sheet.cell_value(i,1),'____',sheet.cell_value(i,2),'____',sheet.cell_value(i,3),'____',sheet.cell_value(i,6))
                        municipio=sheet.cell_value(i,3)
                        colonia = sheet.cell_value(i,1)
                        tipo_asenta = sheet.cell_value(i,2)
                        cp=sheet.cell_value(i,6)
                        if Municipio.objects.filter(D_mnpio=municipio).exists() ==  False:
                            estado=Estado.objects.filter(d_estado=sheet.name).first()
                            m= Municipio(D_mnpio=municipio, estado=estado)
                            m.save()
                        municipio_db=Municipio.objects.filter(D_mnpio=municipio).first()
                        if Colonia.objects.filter(d_asenta=colonia, municipio=municipio_db).exists() ==  False:
                            c=Colonia(d_asenta=colonia, d_tipo_asenta=tipo_asenta, d_CP= cp, municipio=municipio_db)
                            c.save()
                except Exception as e:
                    print(e)