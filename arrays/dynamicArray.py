import ctypes

class DynamicArray(object):

    #? Python Constructor
    def __init__(self):
        self.size = 0
        self.capacity = 16
        self.A = self.make_array(self.capacity) #Allocate memory to make this array eqaul to the capacity 

    def __size__ (self):
        #Return number of current elements in array
        return self.size
    
    def __capacity__(self):
        return self.capacity

    def __getItem__(self, k):
        #return element at k index
        if k >= self.size and k >=0:
            return IndexError("K is out of bounds")
        return self.A[k]
    
    def append(self, element):
        if self.size == self.capacity:
            #make a copy of array and make twice the current capacity
            self.resize(2*self.capacity) #resize method is define below
        #set the last element of A equal to the element
        self.A[self.size] = element
        self.size +=1

    def resize(self, new_capacity):
        #new capacity of A
        copy_A = self.make_array(new_capacity)
        for i in range(self.size):
            copy_A[i] = self.A[i] #put elements of A in new array
        self.A = copy_A #change current array
        self.capacity = new_capacity #assign new capacity
    
    def make_array(self, new_capacity):
        #using ctype library
        return (new_capacity * ctypes.py_object)()
    
    def is_empty(self):
        #return if there's no elements
        return self.size == 0
    
    def find(self, k):
        #return index of given k element and -1 if not found
        for index in self.size:
            if(self.A[index] == k):
                return index
            return -1
    

        

dynamic_array = DynamicArray();

print("Capacity:", dynamic_array.__capacity__())
print("Size: " ,dynamic_array.__size__())

for i in range(16):
    dynamic_array.append(i)

print("Capacity:", dynamic_array.__capacity__())
print("Size: " ,dynamic_array.__size__())    

dynamic_array.append(16)

print("Capacity:", dynamic_array.__capacity__())
print("Size: " ,dynamic_array.__size__())  

print("Element at " , 12, ": " ,dynamic_array.__getItem__(12))
    
    
        



