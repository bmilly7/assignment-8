class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"
class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def __init__(self,size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        current = self.data[index]
        value = Contact(key,number)

        if current is None:
            self.data[index] = Node(key,value)
            return

        while current: 
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break

            current = current.next
        current.next = Node(key,value)


    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: empty")
            else:
                print(f"Index {i}:", end=" ")
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()
    

# Test your hash table implementation here.  
table = HashTable(10)
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")
table.insert("Rebecca", "999-444-9999")  # update test

table.print_table()

print("\nSearch for John:", table.search("John"))
print("Search for Chris:", table.search("Chris"))

'''
Why is a hash table the right structure for fast lookups?
How did you handle collisions?
When might an engineer choose a hash table over a list or tree?

Hash tables are the right structure for fast lookups because their lookup time is O(1). Instead of checking every value one by one,
hash tables calculate exactly where the data should be stored, allowing to jump straight to the location instead of iterating over every
element in the data. This could take a lot of time as the size of the data grows.

I handled the collisions by using the linked list and adding a pointer if there was a collision. This way, if two keys has to the same index, the index can store 
both the keys by chaining them together. 

An engineer may choose a hash table over a list or tree when you need fast access to data using unique keys and fast lookups. They might choose a hash table when order doesnt matter as well. 





'''