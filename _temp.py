screen_height = 800
screen_width = 800
line_colour = (0, 0, 205)




class PolyHedron:
    def __init__(self, n) -> None:
        self.n = n
        self.vertices = []
        self.edges = []
        self.surfaces = []


    def draw(self):
        self.fill_sides()
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(0, 0, 1)
                glVertex3fv(self.vertices[vertex])
        glEnd()
    
    def fill_sides(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3f(0.45, 0.482, 0)
                glVertex3fv(self.vertices[vertex])
        glEnd()

class SymmetryPoly(PolyHedron):
    def __init__(self, n) -> None:
        super().__init__(n)
        self.generatePoly()
        self.generateEdges()
        self.scaleEdges(1.5)

    def generatePoly(self):
        angle = 360 / self.n
        for i in range(self.n):
            p,q = math.cos(math.radians(angle * i)), math.sin(math.radians(angle * i))
            self.vertices.append([p, q, 0])
        for i in range(self.n):
            self.vertices.append([self.vertices[i][0], 0, self.vertices[i][1]])
    
    def generateEdges(self):
        n = self.n
        for i in range(n):
            self.edges.append((i, (i + 1) % n))
            self.edges.append((n+i, (i + 1) % n + n))
            self.edges.append((i, n+i))
        for i in range(1,n):
            self.edges.append((i, (2*n)-i))
    
    def scaleEdges(self, scale):
        new_vertices = list(numpy.multiply(numpy.array(self.vertices), scale))
        self.vertices = new_vertices
    

class Prism(PolyHedron):
    def __init__(self, n) -> None:
        super().__init__(n)
        self.geneatePoly(n)
        self.generateEdges(n)

    def geneatePoly(self, n):
        angle = 360 / n
        for i in range(n):
            p,q = math.cos(math.radians(angle * i)), math.sin(math.radians(angle * i))
            self.vertices.append([p, q, 1])
        for i in range(n):
            self.vertices.append([self.vertices[i][0], self.vertices[i][1], -1])

    def generateEdges(self, n):
        for i in range(n):
            self.edges.append((i, (i + 1) % n))
            self.edges.append((n+i, (i + 1) % n + n))
            self.edges.append((i, n+i))
    
    def elongate(self, scale):
        new_vertices = list(numpy.add(numpy.array(self.vertices[:self.n]), [0,0,scale]))
        new_vertices += list(numpy.add(numpy.array(self.vertices[self.n:]), [0,0,-scale]))
        self.vertices = new_vertices

class NDegSymmetryPoly(SymmetryPoly):
    def __init__(self, n, color=(0,1,1)) -> None:
        super().__init__(n)
        self.color = color
    
    def generatePoly(self):
        angle = 360 / self.n
        for i in range(self.n):
            p,q = math.cos(math.radians(angle * i)), math.sin(math.radians(angle * i))
            self.vertices.append([p, q, 0])
        
        incline = 0
        increment = 180 / 12
        for m in range(12):
            incline+= increment
            for i in range(self.n):
                self.vertices.append([self.vertices[i][0], self.vertices[i][1]*math.cos(math.radians(incline)), self.vertices[i][1]*math.sin(math.radians(incline))] )

    def generateEdges(self):
        n = self.n
        for j in range(7):
            for i in range(n):
                self.edges.append((n*j +i, (i + 1) % n + n*j))
                if j < 6 : self.edges.append((n*j + i, n*j + n + i))

    def draw(self):
        count = 0
        r,g,b = self.color
        self.fill_sides()
        glLineWidth(3)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3f(r, g, b)
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def rotate(self, angle, axis):
        angle = math.radians(angle)
        if axis == 'x':
            rotation_matrix = numpy.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
        elif axis == 'y':
            rotation_matrix = numpy.array([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
        elif axis == 'z':
            rotation_matrix = numpy.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
        new_vertices = list(numpy.matmul(numpy.array(self.vertices), rotation_matrix))
        self.vertices = new_vertices