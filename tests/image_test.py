import sys
sys.path.append('../')# allows us to fetch files from the project root
import unittest
from modules.image import *
import modules.open_digraph as odgraph

class PointTest(unittest.TestCase):

    def point_test(self):
        p12 = point(1,2)
        p00 = point(0,0)
        p01 = point(0,1)
        p10 = point(1,0)
        pf11f22 = point(1.1,2.2)
        pn12 = point(-1,2)
        pf112 = point(1.1,2)
        pnf092 = point(-0.9,2)
        self.assertIsInstance(pnf092, point)

        #test de normalize
        def test_normalize(self):
            self.assertEqual(p12.n(), (1, 2))
            self.assertEqual(p00.n(), (0, 0))
            self.assertEqual(pf11f22.n(), (1, 2))
            self.assertEqual(pn12.n(), (-1, 2))
            self.assertEqual(pf112.n(), (1, 2))
            self.assertEqual(pnf092.n(), (0, 2))

        #test de copy
        def test_copy(self):
            self.assertEqual(p12.copy(), p12)
            self.assertEqual(p00.copy(), p00)
            self.assertEqual(pf11f22.copy(), pf11f22)
            self.assertEqual(pn12.copy(), pn12)
            self.assertEqual(ppf112.copy(), ppf112)
            self.assertEqual(pnf092.copy(), pnf092)

        #tests de add
        def test_add(self):
            self.assertEqual(p12 + p00, p12)
            self.assertEqual(pnf112 + p00, p12)
            self.assertEqual(p12, p01 + p01 + p10)
            self.assertEqual(pnf092 + p10 + p10, pf112)

        #tests de sub
        def test_sub(self):
            self.assertEqual(p12 - p00, p12)
            self.assertEqual(pnf112 - p00, p12)
            self.assertEqual(p12 - p01 - p01, p10)
            self.assertEqual(pnf092, pf112- p10 - p10 )

        #tests de mul
        def test_mul(self):
            self.assertEqual(p12 * 0, p00)
            self.assertEqual(pnf112 * 1, pnf112)
            self.assertEqual(p12, p10 + 2*p01)

        #tests de rotate
        def test_rotate(self):
            self.assertEqual(p00, p00.rotate(23))
            self.assertEqual(p01, p10.rotate(math.pi/2))
            self.assertEqual(p10, p01.rotate(3*math.pi/2))

class ImageTest(unittest.TestCase):
    width = 400
    height = 400
    centre = point(width/2, height/2)
    pasOrigine = point(61,79)

    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)

    nodeNoe = odgraph.node(27, "Noé", [], [])
    nodeLongName = odgraph.node(13, "Very", [], [])
    nodeHpotrsuob = odgraph.node(-27, "èoN", [], [])
    nodeAnon = odgraph.node(42, "", [], [])
    nodeS = odgraph.node(18, "S", [], [])

    nodeList = [nodeNoe, nodeLongName, nodeHpotrsuob, nodeAnon, nodeS]
    g = odgraph.open_digraph([27], [18], nodeList)
    g.add_edges([27, 13, 18], [42, 27, 13])

    draw.graph(g,'topological_sorting',{0:point(50,20),1:point(130,70),2:point(300,250)},[point(2,2)], [point(400,400)])

    image.save("test.jpg")
    draw.drawnode(node, centre,True)
    draw.graph(g,'random')
    draw.arrows(pasOrigine,centre)
    draw.drawnode(node, pasOrigine,True)





















    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)

    node = odgraph.node(27, "Noé", [], [])
    centre = point(width/2, height/2)
    # draw.drawnode(node, centre, True)

    n0list = [odgraph.node(i, '{}'.format(i), [], [1]) for i in range(8)]
    g = odgraph.open_digraph([1], [2], n0list)
    # g.add_edge(1, 2)
    # draw.graph(g,'random')
    # draw.graph(g,'circle',{0:point(50,20),1:point(130,70),2:point(300,250)},[point(2,2)], [point(400,400)])
    pasOrigine = point(33, 200)
    # draw.arrows(pasOrigine,centre, 4, 1)
    draw.drawnode(node, pasOrigine, True)

    image.save("test.jpg")
