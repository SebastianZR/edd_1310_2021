

algo = Array (10)
print (algo.get_item(6363))
algo.set_item (533,3)
print (algo.get_item(3))
print (f"El arreglo tiene {algo.get_lenght()} elementos")
algo.clear(777)
print (algo.get_item(3))
print ("--------------------------")
for x in algo :
    print (x)
print ("----Prueba Iterador ----")
for x in range (algo.get_lenght()):
    print (f"{x} --->{algo.get_item(x)}")
