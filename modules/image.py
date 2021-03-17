from PIL import Image, ImageDraw
import math
import random
import sys
sys.path.append('../')
import modules.utils
import modules.open_digraph as odgraph

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def n(self):
        return (round(self.x), round(self.y))

    def __repr__(self):
        return f"x : {self.x}, y : {self.y}"

    def copy(self):
        '''
        **TYPE** point
        function that returns a copy of the point'''
        return point(self.x,self.y)

    def __add__(self, p2):
        '''
        **TYPE** point
        function that defines how to add two points'''
        return point(self.x + p2.x, self.x + p2.y)

    def __rmul__(self, s):
        '''
        **TYPE** point
        function that defines how to multiplicate a point with a scalar
        using __rmul__ allows commutativity, because the scalar does not know how to
        multiply itself by a point'''
        return point(self.x * s, self.y * s)

    def __sub__(self, p2):
        '''
        **TYPE** point
        function that defines the substraction of two points'''
        return point(self.x - p2.x, self.x - p2.y)

    def rotate(self, theta, c = None):
        '''
        **TYPE**: point
        theta : float; rotation angle in radian
        c : point; rotation center
        function that calculates the position of the point after rotation angle theta around the center c
        '''
        if c is None:
            c = point(width/2,height/2)
        x_t = self.x - c.x
        y_t = self.y - c.y

        x =  x_t*math.cos(theta) + y_t*math.sin(theta) + c.x
        y = -x_t*math.sin(theta) + y_t*math.cos(theta) + c.y
        return (x, y)

def drawarrows(self, p1, p2, n = O, m = O):
    '''method that describes how to make an arrow from point p1 to point p2'''
    #the class must have a line() method, ImageDraw has it, it draws a black line from p1.n() to p2.n()
    self.line([p1.n(), p2.n()], 'black')

    #pas fini, non testé
    angle = slope_angle(p1,p2)
    if(n>0):
        p1a = p1.sub(point(10,0))
        p1b = p1.sub(point(10,0))
        p1a.rotate(abs(angle-(math.pi/4)),p1)
        p1b.rotate(abs(angle-(math.pi/4))+math.pi/2,p1)
        self.line([p1.n(), p1a.n()], 'black')
        self.line([p1.n(), p1b.n()], 'black')
    if(m>0):
        p2a = p2.sub(point(10,0))
        p2b = p2.sub(point(10,0))
        p2a.rotate(abs(angle-(math.pi/4)),p2)
        p2b.rotate(abs(angle-(math.pi/4))+math.pi/2,p2)
        self.line([p2.n(), p2a.n()], 'black')
        self.line([p2.n(), p2b.n()], 'black')
    #we define the method 'arrows' from the function 'arrows' above

ImageDraw.ImageDraw.arrows = drawarrows


def drawnode(self, node, point, verbose = False):
    '''method that draws a node at a point'''
    txt = node.get_label()
    # Ellipse takes two parameters : the top left corner, and the bottom right one
    # We define them such as the text is centered (depends on the length of the node label)
    top_left = (point.x-len(txt)*5, point.y-len(txt)*5)
    if (len(txt) == 1):                         # The text is defined by the top left of his first letter, if it is
        bottom_right = (point.x+15, point.y+15) # only one char length, it is different because we want our char to be in the circle
    else :
        bottom_right = (point.x+len(txt)*5, point.y+len(txt)*5)
    self.ellipse([top_left, bottom_right], fill ='white', outline='black')
    self.text((point.x + 5 - len(txt)*3, point.y - len(txt)*5 + (bottom_right[0]-top_left[0])/2 - 5), txt, fill='black')

    if(verbose): # verbose shows the value of the node
        if (len(txt) == 1): # again we want it to be centered
            self.text((point.x,point.y + 20), str(node.get_id()), fill ='black')
        else :
            self.text((point.x-5,point.y + 20), str(node.get_id()), fill ='black')

ImageDraw.ImageDraw.drawnode = drawnode

def drawgraph(self, g, method='manual', node_pos=None, input_pos=None, output_pos=None):
    '''method that draws nodes from g with the position list node_pos
    '''
    if(method == 'random'):
        random = random_layout(g)
        node_pos = random[0]
        input_pos = random[1]
        output_pos = random[2]
    elif (method == 'circle'):
        circle = circle_layout(g)
        node_pos = circle[0]
        input_pos = circle[1]
        output_pos = circle[2]

    for input in range(len(input_pos)):
        self.arrows(input_pos[input], node_pos[g.get_input_ids()[input]])
    for output in range(len(output_pos)):
        self.arrows(output_pos[output], node_pos[g.get_output_ids()[output]])

    for node in g.get_nodes():
        for parent in node.get_parent_ids():
            self.arrows(node_pos[parent], node_pos[node.get_id()])
    for id in list(node_pos.keys()):
        self.drawnode(g.get_node_by_id(id), node_pos[id])

ImageDraw.ImageDraw.graph = drawgraph



width = 400
height = 400


def random_layout(graph):
    node_ids = graph.get_node_ids() #node ids list
    nbr = len(node_ids)             #number of node
    node_pos = {}
    for i in range(nbr):
        node_pos[node_ids[i]] = point(random.randrange(width), random.randrange(height))
    input_pos = [ point(random.randrange(width),random.randrange(height)) for i in graph.get_input_ids() ]      #position of input
    output_pos = [ point(random.randrange(width),random.randrange(height)) for i in graph.get_output_ids() ]    #position of output
    return (node_pos, input_pos, output_pos)

def circle_layout(graph):
    '''
    **TYPE**: point list * point list * point list
    function that returns positions for nodes in a graph such that these positions are uniformly distributed on a circle around the center of the image
    '''
    node_ids = graph.get_node_ids() #node ids list
    nbr_node = len(node_ids) #number of node
    angle = (2.*math.pi)/nbr_node
    node_pos = {}

    radius = height/3
    origin = point(width/2, height/2+radius)
    for i in range(nbr_node):
        node_pos[node_ids[i]] = point(*origin.rotate(angle*i))
    input_pos = []
    output_pos = []
    for i in graph.get_input_ids() :
        pos_x = node_pos[node_ids[i]].n()[0]
        pos_y = node_pos[node_ids[i]].n()[1]
        dot = point(pos_x, pos_y+50)
        (x, y) = dot.rotate(random.randrange(360), c=node_pos[node_ids[i]])
        input_pos.append(point(x, y))     #position of input
    for i in graph.get_output_ids() :
        pos_x = node_pos[node_ids[i]].n()[0]
        pos_y = node_pos[node_ids[i]].n()[1]
        dot = point(pos_x, pos_y+50)
        (x, y) = dot.rotate(random.randrange(360), c=node_pos[node_ids[i]])
        output_pos.append(point(x, y))     #position of output
    return (node_pos, input_pos, output_pos)


def slope_angle(p1,p2):
    '''
    **TYPE** float
    p1: point; the first point
    p2: point; the second point
    calculation of the angle between the abscissa axe and the
    '''
    coeff_direct = (p1.y - p2.y)/(p1.x - p2.x) #leading coefficient calculation
    ordonne_origine = p1.y - coeff_direct* p1.x #origin ordinate calculation

    y = coeff_direct                    #calculation of the two intersection with the ordinate
    x = -ordonne_origine/coeff_direct   #and the abscissa
    return math.atan(y/x)            #the angle calculate by arctan(opp/adj)




image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)

node = odgraph.node(27, "Noé", [], [])
centre = point(width/2, height/2)
#draw.drawnode(node, centre,True)

n0list = [odgraph.node(i, '{}'.format(i), [], [1]) for i in range(8)]
g = odgraph.open_digraph([1], [2], n0list)
g.add_edge(1, 2)
<<<<<<< HEAD
=======
#draw.graph(g,'random')
draw.graph(g,'circle',{0:point(50,20),1:point(130,70),2:point(300,250)},[point(2,2)], [point(400,400)])
>>>>>>> c50a23eb41c3c7e75e97ffc45b5a948cbb5d11f4
pasOrigine = point(61,79)
#draw.arrows(pasOrigine,centre)
#draw.drawnode(node, pasOrigine,True)

image.save("test.jpg")
