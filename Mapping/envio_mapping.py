import os
Mapping = os.getcwd()

import pandas as pd
from datetime import datetime
import aux_mapping_items 
os.chdir(Mapping)
import listar_items_fecha
import C003_enviar_correo as correo


os.chdir(Mapping)
print("Enviando correo a ... Destinatarios")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

Destinatarios = pd.read_excel("Destinatarios.xlsx", index_col=0)
Destinatarios = list(Destinatarios.index)
Destinatarios = ";".join(Destinatarios)

path_fotos = open('path.txt', 'r').readline()
path_fotos = path_fotos.replace("Ã­", "í")
path_out = os.path.join(Mapping + '\out\Mapping.csv')
path_out2 = os.path.join(Mapping + '\out\items_dates.csv')
# path_out3 = os.path.join(Mapping + '\out\Mapping.xlsx')

#for destinatario in Destinatarios.index:
    #    destinatario =  ["fcolin@shasa.com", "fagoaga@shasa.com"]
    #    correo.enviar_correo(to=destinatario, 
    #              subject="Mapping " + dt_string, 
    #              body = "Archivos en "+path_fotos, 
    #              attachment= path_out,
    #              attachment2= path_out2 )

correo.enviar_correo(to=Destinatarios,   
              subject="Mapping " + dt_string, 
              body = "Archivos en: "+ path_fotos, 
              attachment= path_out,
              attachment2= path_out2)