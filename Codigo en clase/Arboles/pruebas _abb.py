from arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)

abb.transversal()
abb.transversal("preorden")
abb.transversal("posorden")

resultado = abb.search(35)
print (f"el resultado es {resultado}")
abb.remove (35)
abb.transversal()
