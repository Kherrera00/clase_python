#Funcion para cargar datos
def load_csv_py(filename):
    dataset=[]
    with open(filename, encoding='utf8') as f:
      for linea in f:
            data_line = linea.strip().split(";")  #leer lina y convertirlo a lista
            ds_elem = {"comuna": data_line[0] ,
                    "atracos": data_line[1] ,
                    "robos_viv": data_line[2] ,
                    "robos_veh": data_line[3]}
            dataset.append(ds_elem)
            print(ds_elem)
    print(dataset)
    return dataset