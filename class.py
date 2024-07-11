#list
list=[1,2,3,4]
print("list:",list)
list.insert(1,9)
print("list after inserting: ",list)
list[1]=5
print("list after modifying: ",list)
list.remove(4)
print("list after deleting: ",list)
#Dictionary
dict={"model":"samsung","price":"20000"}
print("Dictionary: ",dict)
dict["price"]="50000"
print("Dictionary after updating: ",dict)
dict["color"]="blue"
print("Dictionary after adding a new key and value: ",dict)
dict.pop("model")
print("Dictionary after removing model key: ",dict)
#set
set={"apple","banana","lichi"}
print("Set: ",set) 
set.add("orange")
print("Set after adding: ",set)
set.remove("banana")
print("Set after removing: ",set)