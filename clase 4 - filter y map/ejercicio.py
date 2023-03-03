def filterData_genero(dic):
    return dic ["genero"] == "rock"


playlist = [{"titulo":"far hehind", "artista":"candlebox", "genero":"rock"}, 
            {"titulo":"paranold", "artista":"black sabbash", "genero":"metal"},
            {"titulo":"far", "artista":"djf", "genero":"salsa"},
            {"titulo":"lagrimas negras", "artista":"diego", "genero":"flamenco"}]



for register in playlist:
    print(register["titulo"])
    print(register["artista"])
    print(register["genero"])
    register["duracion"] = 4.5

print(playlist)

playlist_filtrada = list(filter(filterData_genero, playlist))
print(playlist_filtrada)

playlist_filtrada_lambda = list(filter(lambda dic: dic ["genero"] == "salsa" ,playlist))
print(playlist_filtrada_lambda)

playlist_f_list_comprehesion = [d for d in playlist if d["genero"] == "flamenco"]