class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def _getNodeHeight(root):
  if not root:
      return 0
  return root.height

def _insertRecursively(root, key):
  if not root:
      new_node = Node(key)
      return new_node
  elif key < root.key:
      root.left = _insertRecursively(root.left, key)
  else:
      root.right = _insertRecursively(root.right, key)
  root.height = 1 + max(_getNodeHeight(root.left), _getNodeHeight(root.right))

  balanceFactor = _getNodeBalance(root)
  if balanceFactor > 1:
      if key < root.left.key:
          return _rightRotate(root)
      else:
          root.left = _leftRotate(root.left)
          return _rightRotate(root)

  if balanceFactor < -1:
      if key > root.right.key:
          return _leftRotate(root)
      else:
          root.right = _rightRotate(root.right)
          return _leftRotate(root)

  return root

def _leftRotate(z):
  y = z.right
  aux = y.left
  y.left = z
  z.right = aux
  z.height = 1 + max(_getNodeHeight(z.left), _getNodeHeight(z.right))
  y.height = 1 + max(_getNodeHeight(y.left), _getNodeHeight(y.right))
  return y

def _rightRotate(z):
  y = z.left
  aux = y.right
  y.right = z
  z.left = aux
  z.height = 1 + max(_getNodeHeight(z.left), _getNodeHeight(z.right))
  y.height = 1 + max(_getNodeHeight(y.left), _getNodeHeight(y.right))
  return y

def _getNodeBalance(root):
  if not root:
      return 0
  return _getNodeHeight(root.left) - _getNodeHeight(root.right)

def encontrarMayorSubArbolCompleto(root):
  if root is None:
      return 0

  if esArbolCompleto(root):
      return _getNodeHeight(root)

  alturaIzquierda = encontrarMayorSubArbolCompleto(root.left)
  alturaDerecha = encontrarMayorSubArbolCompleto(root.right)

  return max(alturaIzquierda, alturaDerecha)

def esArbolCompleto(root):
  altura = _getNodeHeight(root)
  return contarNodos(root) == 2 ** altura - 1

def contarNodos(root):
  if root is None:
      return 0
  return contarNodos(root.left) + contarNodos(root.right) + 1
while True:
  N = int(input())
  if N == 0:
      break

  values = list(map(int, input().split()))
  root = None
  for value in values:
      root = _insertRecursively(root, value)

  print(encontrarMayorSubArbolCompleto(root))