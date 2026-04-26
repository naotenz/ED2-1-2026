# tree.py - Árbol de Decisión para el comportamiento del PNJ

class TreeNode:
    """Nodo del árbol de decisión."""
    def __init__(self, condition, true_branch=None, false_branch=None, action=None):
        self.condition = condition  # Condición a evaluar
        self.true_branch = true_branch  # Rama si la condición es verdadera
        self.false_branch = false_branch  # Rama si la condición es falsa
        self.action = action  # Acción a realizar si llegamos a este nodo (hoja)

class DecisionTree:
    """Árbol de decisión que controla el comportamiento de un PNJ."""
    def __init__(self):
        self.root = None

    def build_tree(self):
        """Construcción del árbol de decisión."""
        # Definimos el árbol de decisiones
        # Rama de ataque o huida
        attack_condition = lambda pnj, enemy: pnj['health'] > 50 and enemy['distance'] < 10
        flee_condition = lambda pnj, enemy: pnj['health'] <= 50 or enemy['strength'] > 50
        patrol_condition = lambda pnj, enemy: enemy['distance'] > 10
        
        attack_node = TreeNode(attack_condition, action="Atacar")
        flee_node = TreeNode(flee_condition, action="Huir")
        patrol_node = TreeNode(patrol_condition, action="Patrullar")
        
        # Nodo raíz: Si hay un enemigo cerca o no
        root_condition = lambda pnj, enemy: enemy['distance'] < 10
        self.root = TreeNode(root_condition, true_branch=attack_node, false_branch=patrol_node)

        # Si huir es necesario, conectamos el nodo de huir
        attack_node.false_branch = flee_node

    def evaluate(self, pnj, enemy):
        """Evaluamos el árbol de decisión para determinar qué acción tomar."""
        current_node = self.root
        while current_node:
            if current_node.condition(pnj, enemy):
                if current_node.true_branch is None:  # Si es una hoja, retornamos la acción
                    return current_node.action
                current_node = current_node.true_branch  # Seguir por la rama verdadera
            else:
                if current_node.false_branch is None:  # Si es una hoja, retornamos la acción
                    return current_node.action
                current_node = current_node.false_branch  # Seguir por la rama falsa