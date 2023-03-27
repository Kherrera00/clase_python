class persona:

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
