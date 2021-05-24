from PIL import Image, ImageDraw
import math
import random
import numpy as np
import sys
sys.path.append('../')
import modules.utils
import modules.open_digraph as odgraph


class point:
    def __init__(self, x, y):
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
        return point(self.x, self.y)

    def __add__(self, p2):
        '''
        **TYPE** point
        function that defines how to add two points'''
        return point(self.x + p2.x, self.y + p2.y)

    def __rmul__(self, s):
        '''
        **TYPE** point
        function that defines how to multiplicate a point with a scalar
        using __rmul__ allows commutativity, because
        the scalar does not know how to
        multiply itself by a point'''
        return point(self.x * s, self.y * s)

    def __sub__(self, p2):
        '''
        **TYPE** point
        function that defines the substraction of two points'''
        return point(self.x - p2.x, self.y - p2.y)

    def equal(self, p2):
        '''
        **TYPE** bool
        function that tests if two points are equal'''
        return self.x == p2.x and self.y == p2.y

    def rotate(self, theta, c=None):
        '''
        **TYPE** point
        theta : float; rotation angle in radian
        c : point; rotation center
        function that calculates the position of the point after
        rotation angle theta around the center c
        '''
        if c is None:
            c = point(200, 200)
        x_t = self.x - c.x
        y_t = self.y - c.y

        x = x_t*math.cos(theta) + y_t*math.sin(theta) + c.x
        y = -x_t*math.sin(theta) + y_t*math.cos(theta) + c.y
        return point(x, y)


def drawarrows(self, p1, p2, edge_number_1_to_2=1, edge_number_2_to_1=0):
    '''
    **TYPE** void
    p1 : point 1
    p2: point 2
    edge_number_1_to_2 = number of edges from p1 to p2
    edge_number_2_to_1 = number of edges from p2 to p1
    method that describes how to make an arrow from point p1 to point p2
    '''
    # the class must have a line() method, ImageDraw has it,
    # it draws a black line from p1.n() to p2.n()
    if not(p1.equal(p2)):
        # no need to draw the arrows if the points are merged
        self.line([p1.n(), p2.n()], 'black')
        # we calculate the slope angle for
        # the rotation of the ends of the arrows
        a = -slope_angle(p1, p2)
        # we place the ends of the arrows on the points
        # p1 and p2, in the direction of the right or the left according
        # to their position on the x axis
        if(p1.x > p2.x):
            p1a = point(p1.x-10, p1.y-10)
            p1b = point(p1.x-10, p1.y+10)
            p2a = point(p2.x+10, p2.y-10)
            p2b = point(p2.x+10, p2.y+10)
        else:
            p1a = point(p1.x+10, p1.y-10)
            p1b = point(p1.x+10, p1.y+10)
            p2a = point(p2.x-10, p2.y-10)
            p2b = point(p2.x-10, p2.y+10)
        if(edge_number_2_to_1 > 0):
            # we give a rotation to the ends of the arrows
            # according to the line between p1 and p2
            p1a = point(*p1a.rotate(a, p1))
            p1b = point(*p1b.rotate(a, p1))
            self.line([p1.n(), p1a.n()], 'red')
            self.line([p1.n(), p1b.n()], 'red')
            self.text((p1.x, p1.y + 20), str(edge_number_2_to_1), fill='black')
        if(edge_number_1_to_2 > 0):
            # we give a rotation to the ends of the arrows
            # according to the line between p1 and p2
            p2a = point(*p2a.rotate(a, p2))
            p2b = point(*p2b.rotate(a, p2))
            self.line([p2.n(), p2a.n()], 'blue')
            self.line([p2.n(), p2b.n()], 'blue')
            self.text((p2.x, p2.y + 20), str(edge_number_1_to_2), fill='black')
    # we define the method 'arrows' from the function 'arrows' above


ImageDraw.ImageDraw.arrows = drawarrows


def drawnode(self, node, point, verbose=False):
    '''
    **TYPE** void
    node : the node to draw
    point : the point where we draw the node
    verbose : boolean, true if we reveal the node's label
    method that draw a node at the point's coordinates
    '''
    txt = node.get_label()
    # Ellipse takes two parameters : the top left corner,
    # and the bottom right one
    # We define them such as the text is centered
    # (depends on the length of the node label)
    top_left = (point.x-len(txt)*5, point.y-len(txt)*5)
    # The text is defined by the top left of his first letter, if it is
    # only one char length, it is different because we want
    # our char to be in the circle
    if (len(txt) == 1):
        bottom_right = (point.x+15, point.y+15)
    else:
        bottom_right = (point.x+len(txt)*5, point.y+len(txt)*5)
    self.ellipse([top_left, bottom_right], fill='white', outline='black')
    self.text((point.x + 5 - len(txt)*3,
               point.y - len(txt)*5 + (bottom_right[0]-top_left[0])/2 - 5),
              txt, fill='black')

    if(verbose):  # verbose shows the value of the node
        if (len(txt) == 1):  # again we want it to be centered
            self.text((point.x, point.y + 20), str(node.get_id()),
                      fill='black')
        else:
            self.text((point.x-5, point.y + 20), str(node.get_id()),
                      fill='black')


ImageDraw.ImageDraw.drawnode = drawnode


def drawgraph(self, g, method='manual', width=1, height=1,
              node_pos=None,
              input_pos=None,
              output_pos=None):
    '''
    **TYPE** void
    g : the graph to draw
    method : string - 'random' : give random positions
                                 for the graph's components
                    - 'circle' : draw the graph around a centered circle
                    - 'topological_sorting' : take the topological
                                 sorting coordinates
                    - 'manual' : the user has to give himself the coordinates
    node_pos : point list of the node positions
    input_pos : point list of the input positions
    output_pos : point list of the ouput positions
    method that draws nodes from g with the position list node_pos
    '''
    if(method == 'random'):
        random = random_layout(g, width, height)
        node_pos = random[0]
        input_pos = random[1]
        output_pos = random[2]
    elif (method == 'circle'):
        circle = circle_layout(g, )
        node_pos = circle[0]
        input_pos = circle[1]
        output_pos = circle[2]
    elif(method == 'topological_sorting'):
        DAG = DAG_layout(g)
        node_pos = DAG[0]
        input_pos = DAG[1]
        output_pos = DAG[2]

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


def random_layout(graph, width, height):
    '''
    **TYPE** point list * point list * point list
    function that returns random positions for nodes in a graph
    '''
    node_ids = graph.get_node_ids()  # node ids list
    nbr = len(node_ids)              # number of node
    node_pos = {}
    for i in range(nbr):
        node_pos[node_ids[i]] = point(random.randrange(width),
                                      random.randrange(height))
    input_pos = [point(random.randrange(width), random.randrange(height))
                 for i in graph.get_input_ids()]      # position of input
    output_pos = [point(random.randrange(width), random.randrange(height))
                  for i in graph.get_output_ids()]    # position of output
    return (node_pos, input_pos, output_pos)


def circle_layout(graph):
    '''
    **TYPE** point list * point list * point list
    function that returns positions for nodes in a graph such that these
    positions are uniformly distributed on a circle
    around the center of the image
    '''
    node_ids = graph.get_node_ids()  # node ids list
    nbr_node = len(node_ids)  # number of node
    angle = (2.*math.pi)/nbr_node
    node_pos = {}

    radius = height/3
    origin = point(width/2, height/2+radius)
    for i in range(nbr_node):
        node_pos[node_ids[i]] = point(*origin.rotate(angle*i))
    input_pos = []
    output_pos = []
    for i in graph.get_input_ids():
        pos_x = node_pos[i].n()[0]
        pos_y = node_pos[i].n()[1]
        dot = point(pos_x, pos_y+50)
        (x, y) = dot.rotate(random.randrange(360), c=node_pos[i])
        input_pos.append(point(x, y))     # position of input
    for i in graph.get_output_ids():
        pos_x = node_pos[i].n()[0]
        pos_y = node_pos[i].n()[1]
        dot = point(pos_x, pos_y+50)
        (x, y) = dot.rotate(random.randrange(360), c=node_pos[i])
        output_pos.append(point(x, y))     # position of output
    return (node_pos, input_pos, output_pos)


def DAG_layout(graph):
    # documentation
    # TYPE, arguments, what it does
    '''
    **TYPE** point list * point list * point list
    function that returns positions for nodes in a graph such that these
    positions are distributed on layers
    '''

    node_pos = {}
    sorted_nodes = graph.topological_sorting()
    nbr_layers = len(sorted_nodes)

    for i in range(nbr_layers):
        for id, node in enumerate(sorted_nodes[i]):
            node_pos[node] = point((id+1)*200/len(sorted_nodes[i]),
                                   (i+1)*200/len(sorted_nodes))

    input_pos = []
    output_pos = []
    for i in graph.get_input_ids():
        pos_x = node_pos[i].n()[0]
        pos_y = node_pos[i].n()[1]
        dot = point(pos_x, pos_y-50)
        input_pos.append(dot)     # position of input
    for i in graph.get_output_ids():
        pos_x = node_pos[i].n()[0]
        pos_y = node_pos[i].n()[1]
        dot = point(pos_x, pos_y+50)
        output_pos.append(dot)    # position of output
    return (node_pos, input_pos, output_pos)


def slope_angle(p1, p2):
    '''
    **TYPE** float
    p1: point; the first point
    p2: point; the second point
    calculation of the angle in radian
    between the abscissa axe and the line from p1 to p2
    '''
    # if the line from p1 to p2 is perpendicular to the x-axis
    if (p1.x == p2.x):
        return -(math.pi)/2
    else:
        # leading coefficient calculation
        coeff_direct = (p1.y - p2.y)/(p1.x - p2.x)
        return math.atan(coeff_direct)


def Bezier(self, p0, paux, p1, dt=0.01):
    '''
    **TYPE** void
    p0 :    point; start
    paux :  point; auxiliary point of the curve
    p1 :    point; finish
    draws a Bezier curve
    '''
    for t in np.arange(0, 0.9, dt) :
        B = (1-t)*((1-t)*p0 + t*paux) + t*((1-t)*paux + t*p1)
        Bsuiv = (1-(t+dt))*((1-(t+dt))*p0 + (t+dt)*paux) + (t+dt)*((1-(t+dt))*paux + (t+dt)*p1)
        self.line([B.n(), Bsuiv.n()], 'black')

ImageDraw.ImageDraw.Bezier = Bezier
