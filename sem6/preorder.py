"""Como estamos comenzando con los árboles binarios de búsqueda arranquemos con algo fácil: 
si se inserta, uno a uno, una serie de elementos, ¿cómo sería el recorrido en pre-orden correspondiente?
Input
La entrada comienza con una línea que contiene un número entero positivo C 
que corresponde a la cantidad de casos (1 ≤ C ≤ 10). Luego siguen C líneas, cada una con no menos de 1 y no más de 256 valores enteros no negativos,
 menores a 1000, sin repetidos, y separados entre sí por un espacio en blanco. Al final de cada línea hay un valor -1 que no hace parte de la serie
   correspondiente.
Output
La salida debe contener C líneas. Cada una con el correspondiente recorrido en pre-orden del árbol binario de búsqueda resultante. 
Los elementos de ese recorrido deben aparecer concatenados (unidos entre sí)."""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursively(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursively(root.right, key)
        return root

    def search(self, key):
        if self._search_recursively(self.root, key) != None:
            return True
        else:
            return False

    def _search_recursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursively(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._min_value_node(root.right).key
            root.right = self._delete_recursively(root.right, root.key)

        return root

    def inorder(self):
        elements = []
        self._inorder_recursively(self.root, elements)
        return elements

    def _inorder_recursively(self, root, elements):
        if root:
            self._inorder_recursively(root.left, elements)
            elements.append(root.key)
            self._inorder_recursively(root.right, elements)

for i in range(int(input())):
    arbol=input().split()
    prueba=BinarySearchTree()
    for i in arbol:
      prueba.insert(i)
    print(prueba)
    


