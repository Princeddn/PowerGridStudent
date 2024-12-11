
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeud_entree = -1
        noeuds = {}
        arcs = []

        # Parcours du terrain pour identifier les nœuds et l'entrée
        for i, ligne in enumerate(t.cases):
            for j, case in enumerate(ligne):
                if case == Case.ENTREE:
                    noeud_entree = len(noeuds)
                    noeuds[noeud_entree] = (i, j)
                elif case == Case.CLIENT:
                    noeuds[len(noeuds)] = (i, j)
        
        # Création des arcs (ici un simple exemple, à ajuster selon logique)
        for noeud1, pos1 in noeuds.items():
            for noeud2, pos2 in noeuds.items():
                if noeud1 != noeud2 and self.sont_voisins(pos1, pos2):
                    arcs.append((noeud1, noeud2))

        return noeud_entree, noeuds, arcs

    def sont_voisins(self, pos1: tuple[int, int], pos2: tuple[int, int]) -> bool:
        """Vérifie si deux positions sont voisines (c'est-à-dire qu'elles partagent une côté)."""
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2) == 1  # Vérification de la proximité (voisinage direct)

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeud_entree = -1
        noeuds = {}
        arcs = []

        # Recherche d'un emplacement pour l'entrée
        for i, ligne in enumerate(t.cases):
            for j, case in enumerate(ligne):
                if case == Case.ENTREE and noeud_entree == -1:
                    noeud_entree = len(noeuds)
                    noeuds[noeud_entree] = (i, j)

                if case == Case.CLIENT:
                    noeuds[len(noeuds)] = (i, j)

        # Création des arcs automatiquement entre nœuds voisins
        for noeud1, pos1 in noeuds.items():
            for noeud2, pos2 in noeuds.items():
                if noeud1 != noeud2 and self.sont_voisins(pos1, pos2):
                    arcs.append((noeud1, noeud2))

        return noeud_entree, noeuds, arcs

    def sont_voisins(self, pos1: tuple[int, int], pos2: tuple[int, int]) -> bool:
        """Vérifie si deux positions sont voisines."""
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2) == 1  # Vérification de la proximité (voisinage direct)
