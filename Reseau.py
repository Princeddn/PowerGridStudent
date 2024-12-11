
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        # Vérifie si un nœud d'entrée est défini
        if self.noeud_entree == -1:
            return False

        # Liste des nœuds visités (initialement, seul le noeud d'entrée est visité)
        visited = set([self.noeud_entree])
        to_visit = [self.noeud_entree]

        # Effectue une recherche en largeur (BFS) pour vérifier la connectivité
        while to_visit:
            current = to_visit.pop(0)
            for n1, n2 in self.arcs:
                if n1 == current and n2 not in visited:
                    visited.add(n2)
                    to_visit.append(n2)
                elif n2 == current and n1 not in visited:
                    visited.add(n1)
                    to_visit.append(n1)

        # Vérifie si tous les nœuds sont visités
        return len(visited) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
        if self.noeud_entree == -1:
            return False  # Aucun nœud d'entrée défini

        # Vérifie que chaque client est relié à un nœud
        clients = set()
        for i, ligne in enumerate(t.cases):
            for j, case in enumerate(ligne):
                if case == Case.CLIENT:
                    clients.add((i, j))

        # Vérifie que chaque client est bien représenté par un nœud
        for client in clients:
            if client not in self.noeuds.values():
                return False

        # Vérifie la position du nœud d'entrée
        entree_position = self.noeuds.get(self.noeud_entree)
        if entree_position is None or entree_position not in t.cases:
            return False

        return True

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

    def afficher(self) -> None:
        print("Nœuds du réseau :")
        for noeud, coord in self.noeuds.items():
            print(f"Noeud {noeud}: {coord}")
        
        print("\nArcs du réseau :")
        for arc in self.arcs:
            print(f"Arc: {arc}")

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

