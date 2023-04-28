
class XMLInterface:

    def getData(self):
        pass

    def setData(self):
        pass

# class JSONInterface:

#     def getData(self):
#         pass

#     def setData(self):
#         pass
# class TXTInterface:

#     def getData(self):
#         pass

#     def setData(self):
#         pass


class Source(XMLInterface):
    def getData(self):
        return "<XML>data</XML>"

# interfaz destino
class TxtInterface():
    def getData(self):
        pass
    def setData(self):
        pass

class Adapter (TxtInterface):
    __Source = None

    def __init__(self, source):
        self.__Source = source

    def getData(self):
        return "plain text data"
    
class Client_TXT:
    _sourceType = None

    def __init__(self, sourceType):
        self.__sourceType = sourceType

    def getClientData(self):
        if self.__sourceType.getData() == "plan text data":
            print ("Datos correctos")
        else: 
            print("datos incorrectos")

fuenteXML = Source()
adaptador = Adapter(fuenteXML)
miCliente = Client_TXT(adaptador)

miCliente.getClientData()


# class adaptarXML(XMLInterface):
#     def getData(self):
#         return "<XML>data</XML>"
    
# class adaptarJSON(JSONInterface):
#     def getData(self):
#         return "data1: 'value'" 

# class adaptarTXT(TXTInterface):
#     def getData(self):
#         return "plain text data"

#solo admite una instancia a la vez
class Session:

    __instance = None

    def getInstance():
        if Session.__instance == None:
            Session()
        return Session.__instance
        

    def __init__(self):
        if Session.__instance != None:
            raise Exception("ya se ha creado una instancia de esta clase")
        else:
            Session.__instance = self


"""class persona:

    #atributos de clase
    maxCourses = 100
    campus = "Pampalinda"


    #atributos de instancia, metodo
    def __init__(self, name, document):
        self.name = name
        self.document = document

    #sobre carga de datos
    def __str__(self):
        return f"nombre: {self.name},documento:{self.document}, campus: {self.campus}"

    def printInfo():
        print(self.maxCourses)
        print(self.campus)
        print(self.name)
        print(self.document)

    #sub clase persona
    class Student(persona):
        pass

    class operativeEmp(persona):
        pass

    class ManagementEmp(persona):
        pass
        """