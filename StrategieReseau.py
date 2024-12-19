
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []

        print("Veuillez configurer le réseau manuellement.")
        entree = t.get_entree()
        if entree == (-1, -1):
            print("Aucune entrée trouvée sur le terrain.")
            return -1, {}, []

        noeuds[0] = entree
        print(f"Nœud d'entrée défini à {entree}.")

        clients = t.get_clients()
        for i, client in enumerate(clients, start=1):
            noeuds[i] = client
            print(f"Nœud {i} défini à la position client {client}.")
        
        while True:
            arc_input = input("Entrez un arc (format : noeud1 noeud2, ou 'fin' pour terminer) : ")
            if arc_input.lower() == "fin":
                break
            try:
                n1, n2 = map(int, arc_input.split())
                if n1 in noeuds and n2 in noeuds:
                    arcs.append((n1, n2))
                    print(f"Arc ajouté entre {n1} et {n2}.")
                else:
                    print("Les nœuds spécifiés n'existent pas.")
            except ValueError:
                print("Format incorrect. Réessayez.")

        return 0, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        noeuds = {}
        arcs = []
        
        clients = t.get_clients()
        entree = t.get_entree()
        
        if entree == (-1, -1):
            return -1, {}, []

        noeuds[0] = entree
        for i, client in enumerate(clients, start=1):
            noeuds[i] = client
            arcs.append((0, i))
        
        return 0, noeuds, arcs
