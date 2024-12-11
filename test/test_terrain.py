
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        # Crée un fichier de test temporaire
        with open("terrains/test.txt", "w") as f:
            f.write("E~~\n")
            f.write("CCC\n")

        # Crée une instance de Terrain et charge le fichier
        t = Terrain()
        t.charger("terrains/test.txt")

        # Vérifie que le terrain a bien été chargé avec les bonnes dimensions et cases
        self.assertEqual(t.largeur, 3)  # Largeur : 3 (3 colonnes)
        self.assertEqual(t.hauteur, 2)  # Hauteur : 2 (2 lignes)
        self.assertEqual(t[0][0], Case.ENTREE)  # Première case : ENTREE
        self.assertEqual(t[0][1], Case.VIDE)  # Deuxième case : VIDE
        self.assertEqual(t[0][2], Case.VIDE)  # Troisième case : VIDE
        self.assertEqual(t[0][10], Case.CLIENT)  # Première case de la deuxième ligne : CLIENT
        self.assertEqual(t[1][17], Case.CLIENT)  # Deuxième case : CLIENT
        self.assertEqual(t[1][2], Case.CLIENT)  # Troisième case : CLIENT

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

