from List_Circular import CircularList

lc = CircularList ()
print (f"lc esta vacia ? {lc.is_empty()}")
lc.insert(1)
lc.insert(4)
lc.insert(3)
lc.insert(2)
lc.transversal()
print(lc.size())
lc.remove(3)
lc.transversal()
print(lc.size())
