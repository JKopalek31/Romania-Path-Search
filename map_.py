from city import city


class map_:
    def __init__(self):
        self.Oradea     =   city ("Oradea", 380)
        self.Zerind     =   city ("Zerind", 374)
        self.Arad       =	city ("Arad", 366)
        self.Timisoara  =	city ("Timisoara", 329)
        self.Lugoj      =	city ("Lugoj", 244)
        self.Mehadia    =	city ("Mehadia", 241)
        self.Drobeta    =	city ("Drobeta", 242)
        self.Craiova    =	city ("Craiova", 160)
        self.Rimnicu    =	city ("Rimnicu", 193)
        self.Sibiu      =	city ("Sibiu", 253)
        self.Pitesi     =	city ("Pitesi", 100)
        self.Fagaras    =	city ("Fagaras", 176)
        self.Bucharest  =	city ("Bucharest", 0)
        self.Giurgiu    =	city ("Giurgiu", 77)
        self.Hirsova    =	city ("Hirsova", 151)
        self.Eforie     =	city ("Eforie", 161)
        self.Urziceni   =	city ("Urziceni", 80)
        self.Vaslui     =	city ("Vaslui", 199)
        self.Iasi       =	city ("Iasi", 226)
        self.Neamt      =	city ("Neamt", 234)
        
        # And the mapping. I think one of these is incorrect, but
        # it doesn't matter for the homework
        self.Oradea.addconnection (self.Zerind, 71)
        self.Oradea.addconnection (self.Sibiu, 151)

        self.Zerind.addconnection (self.Oradea, 71)
        self.Zerind.addconnection (self.Arad, 75)

        self.Arad.addconnection (self.Sibiu, 140)
        self.Arad.addconnection (self.Zerind, 75)
        self.Arad.addconnection (self.Timisoara, 118)

        self.Timisoara.addconnection (self.Arad, 118)
        self.Timisoara.addconnection (self.Lugoj, 111)

        self.Lugoj.addconnection (self.Timisoara, 111)
        self.Lugoj.addconnection (self.Mehadia, 70)

        self.Mehadia.addconnection (self.Drobeta, 75)
        self.Mehadia.addconnection (self.Lugoj, 70)

        self.Drobeta.addconnection (self.Mehadia, 75)
        self.Drobeta.addconnection (self.Craiova, 120)

        self.Craiova.addconnection (self.Drobeta, 120)
        self.Craiova.addconnection (self.Rimnicu, 146)
        self.Craiova.addconnection (self.Pitesi, 120)

        self.Rimnicu.addconnection (self.Craiova, 146)
        self.Rimnicu.addconnection (self.Sibiu, 80)
        self.Rimnicu.addconnection (self.Pitesi, 97)

        self.Sibiu.addconnection (self.Arad, 140)
        self.Sibiu.addconnection (self.Oradea, 151)
        self.Sibiu.addconnection (self.Fagaras, 99)
        self.Sibiu.addconnection (self.Rimnicu, 80)

        self.Pitesi.addconnection (self.Craiova, 120)
        self.Pitesi.addconnection (self.Rimnicu, 97)
        self.Pitesi.addconnection (self.Bucharest, 101)

        self.Fagaras.addconnection (self.Sibiu, 99)
        self.Fagaras.addconnection (self.Bucharest, 211)

        self.Bucharest.addconnection (self.Fagaras, 211)
        self.Bucharest.addconnection (self.Pitesi, 101)
        self.Bucharest.addconnection (self.Giurgiu, 90)
        self.Bucharest.addconnection (self.Urziceni, 85)

        self.Giurgiu.addconnection (self.Bucharest, 90)

        self.Urziceni.addconnection (self.Hirsova, 98)
        self.Urziceni.addconnection (self.Bucharest, 85)
        self.Urziceni.addconnection (self.Vaslui, 142)

        self.Hirsova.addconnection (self.Eforie, 86)
        self.Hirsova.addconnection (self.Urziceni, 98)

        self.Eforie.addconnection (self.Hirsova, 86)

        self.Vaslui.addconnection (self.Urziceni, 142)
        self.Vaslui.addconnection (self.Iasi, 92)

        self.Iasi.addconnection (self.Vaslui, 92)
        self.Iasi.addconnection (self.Neamt, 87)

        self.Neamt.addconnection (self.Iasi, 87)
        