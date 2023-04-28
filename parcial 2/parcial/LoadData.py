#Funcion para cargar datos
def load_csv_py(filename):
    dataset=[]
    with open(filename, encoding='utf8') as f:
      for linea in f:
            data_line = linea.strip().split(";")  #leer lina y convertirlo a lista
            ds_elem = {"Artista": data_line[0] ,
                    "Cancion": data_line[1] ,
                    "Genero": data_line[2] ,
                    "Duracion": data_line[3]}
            dataset.append(ds_elem)
            print(ds_elem)
    print(dataset)
    return dataset