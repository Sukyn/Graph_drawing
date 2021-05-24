import sys
import unittest
sys.path.append('../')  # allows us to fetch files from the project root
from modules.image import *
import modules.open_digraph as odgraph

class PointTest(unittest.TestCase):

    def point_test(self):
        pnf092 = point(-0.9,2)
        self.assertIsInstance(pnf092, point)

    #test de normalize
    def test_normalize(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pf112 = point(1.1,2)
        pnf092 = point(-0.9,2)
        self.assertEqual(p12.n(), (1, 2))
        self.assertEqual(p00.n(), (0, 0))
        self.assertEqual(pf11f22.n(), (1, 2))
        self.assertEqual(pn12.n(), (-1, 2))
        self.assertEqual(pf112.n(), (1, 2))
        self.assertEqual(pnf092.n(), (-1, 2))

    #test de copy
    def test_copy(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pf112 = point(1.1,2)
        pnf092 = point(-0.9,2)
        self.assertEqual(p12.copy().n(), p12.n())
        self.assertEqual(p00.copy().n(), p00.n())
        self.assertEqual(pf11f22.copy().n(), pf11f22.n())
        self.assertEqual(pn12.copy().n(), pn12.n())
        self.assertEqual(pf112.copy().n(), pf112.n())
        self.assertEqual(pnf092.copy().n(), pnf092.n())

    #tests de add
    def test_add(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pf112 = point(1.1,2)
        pnf092 = point(-0.9,2)
        self.assertEqual((p12 + p00).n(), p12.n())
        self.assertEqual((pf112 + p00).n(), p12.n())
        self.assertEqual(p12.n(), (p01 + p01 + p10).n())
        self.assertEqual((pnf092 + p10 + p10).n(), pf112.n())

    #tests de sub
    def test_sub(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pnf112 = point(1.1,2)
        pnf092 = point(-0.9,2)
        self.assertEqual((p12 - p00).n(), p12.n())
        self.assertEqual((pnf112 - p00).n(), p12.n())
        self.assertEqual((p12 - p01 - p01).n(), p10.n())
        self.assertEqual(pnf092.n(), (pnf112- p10 - p10).n() )

    #tests de mul
    def test_mul(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pnf112 = point(1.1,2)
        self.assertEqual(p12.n(), (p10 + 2*p01).n())

    #tests de rotate
    def test_rotate(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pf112 = point(1.1,2)
        self.assertEqual(p01.n(), p01.rotate(math.pi/2,p01).n())
        self.assertEqual(p10.n(), p10.rotate(3*math.pi/2,p10).n())

class ImageTest(unittest.TestCase):
    #DAG visual tests
    '''width = 400
    height = 400
    centre = point(width/2, height/2)
    pasOrigine = point(61,79)

    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)

    node1 = odgraph.node(27, "aze", [], [])
    node2 = odgraph.node(13, "rty", [], [])
    node3 = odgraph.node(-27, "uio", [], [])
    node4 = odgraph.node(42, "", [], [])
    node5 = odgraph.node(18, "S", [], [])

    nodeList = [node1, node2, node3, node4, node5]
    g = odgraph.open_digraph([27], [18], nodeList)
    g.add_edges([27, 13, 18], [42, 27, 13])

    draw.graph(g,'topological_sorting',{0:point(50,20),1:point(130,70),2:point(300,250)},[point(2,2)], [point(400,400)])
    image.save("topological_sorting_test.jpg")'''

    #Bezier visual tests
    '''image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)

    point1 = point(25, 25)
    point2 = point(25, 100)
    pointaux = point(50, 50)
    draw.Bezier(point1, pointaux, point2)

    image.save("bezier_test.jpg")'''

    width = 400
    height = 400
    centre = point(width/2, height/2)
    pasOrigine = point(61,79)


if __name__ == '__main__':  # the following code is called only when
    unittest.main()         # precisely this file is run
