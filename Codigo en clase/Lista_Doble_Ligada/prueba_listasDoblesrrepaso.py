from DobleLinkedListRepaso import DoubleLinkedList

ld = DoubleLinkedList()
print ("Esta vacia :" , ld.is_empty())
ld.append(10)
ld.append(20)
ld.append(30)
print (f"La lista tiene {ld.get_size()} elementos")
ld.transversal()
ld.reversetransversal()
