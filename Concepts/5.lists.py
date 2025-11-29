# Lists: A list is a collection of items in a particular order.
# Lists are mutable, which means that you can change the items in a list.
# Lists are defined by square brackets [].
# Lists can contain any type of data.
# Lists can contain other lists.
# Lists can be indexed and sliced.
# List can be homogeous or hetrogeneous.
# List can be nested.
# List can be empty.

# Example
Places = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
print(Places)
print(Places[2])        # Indexing, starst from 0
print(Places[1:3])      # Slicing, start from 1 and end at 3-1(subtract 1)
print(Places[1:])        # Slicing, start from 1 and end at last
print(Places[:3])        # Slicing, start from 0 and end at 3-1
print(Places[0:4:2])      # Slicing, start from 0 and end at 4-1 with step 2
print(Places[::2])       # Slicing, start from 0 and end at last with step 2
print(Places[-1])        # Negative Indexing, start from last and end at 0
print(Places[::-1])      #Negative Slicing, start from last and end at 0 with step -1
print(Places[::-2])     #Negative Slicing, start from last and end at 0 with step -2

# OUTPUT
# ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore']
# Kolkata
# ['Mumbai', 'Kolkata']
# ['Mumbai', 'Kolkata', 'Chennai', 'Bangalore']
# ['Delhi', 'Mumbai', 'Kolkata']
# ['Delhi', 'Kolkata', 'Bangalore']
# ['Delhi', 'Kolkata']
# Bangalore
# ['Bangalore', 'Chennai', 'Kolkata', 'Mumbai', 'Delhi']
# ['Bangalore', 'Kolkata', 'Delhi']


more_places=['Prayagraj','Ayodhya']
Places.extend(more_places)  # extend is used to add more than one item to the list.
print(Places)
# OUTPUT
# ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Prayagraj', 'Ayodhya']

Places.append('Lucknow')  # append is used to add one item to the list.
print(Places)
# OUTPUT
# ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Prayagraj', 'Ayodhya', 'Lucknow']

Places.insert(2,'Jaipur')  # insert is used to add one item to the list at a specific index.
print(Places)
# OUTPUT
# ['Delhi', 'Mumbai', 'Jaipur', 'Kolkata', 'Chennai', 'Bangalore', 'Prayagraj', 'Ayodhya', 'Lucknow']

Places.remove('Jaipur')  # remove is used to remove one item from the list.
print(Places)
# OUTPUT
# ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Prayagraj', 'Ayodhya', 'Lucknow']