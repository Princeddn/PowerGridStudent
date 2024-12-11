
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        t= Terrain()
        fichier_test='terrains/t1.txt'
        t.charger(fichier_test)
        
        self.assertEqual(t.largeur,21)
        self.assertEqual(t.hauteur,10)
        
        
        self.assertEqual(t[9][17],Case.ENTREE)
        self.assertEqual(t[2][10], Case.CLIENT)
        self.assertEqual(t[4][17],Case.CLIENT)
        self.assertEqual(t[7][6], Case.CLIENT)
        
        
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[6][9],Case.VIDE)
        
        
        self.assertEqual(t[4][10], Case.OBSTACLE)
        self.assertEqual(t[6][11], Case.OBSTACLE)
        

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

