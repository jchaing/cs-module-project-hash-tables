class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# LinkedList only used as reference
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Print entire LL"""

        if self.head is None:
            return "[Empty List]"

        cur = self.head
        s = ""

        while cur is not None:
            s += f"({cur.value})"

            if cur.next is not None:
                s += "-->"

            cur = cur.next

        return s

    def find(self, value):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur

            cur = cur.next

        return None

    def delete(self, value):
        cur = self.head

        # Special case of deleting head
        if cur.value == value:
            self.head = cur.next
            return cur

        # General case of deleting internal Node

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:  # Found it!
                prev.next = cur.next  # Cut it out
                return cur  # Return deleted node
            else:
                prev = cur
                cur = cur.next

        return None  # If we got here, nothing found

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_or_overwrite_value(self, value):
        node = self.find(value)

        if node is None:
            # Make a new node
            self.insert_at_head(HashTableEntry(value))

        else:
            # Overwrite old value
            node.value = value


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        self.buckets = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)

        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.buckets)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # 1. Hash the key
        # 2. Take the hash and mod it with len of array
        idx = self.hash_index(key)

        # 3. Check if there's a value at that index
        if self.buckets[idx] is not None:
            # Check if the key is already in our LL
            node = self.buckets[idx]  # this is the head

            while node is not None:
                if node.key == key:
                    # If so, overwrite that value
                    node.value = value
                    return

                node = node.next

            # Add a node to the head of the linked list
            old_head = self.buckets[idx]
            new_head = HashTableEntry(key, value)
            new_head.next = old_head
            self.buckets[idx] = new_head

        # 3a. Go to index and put in value
        else:
            # Add the first node
            self.buckets[idx] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)

        node = self.buckets[idx]

        # Special case of deleting head; see if head matches
        if node.key == key:
            self.buckets[idx] = node.next
            return node

        # General cse of deleting internal node
        prev_node = node
        node = node.next

        while node is not None:
            if node.key == key:  # Found it!
                prev_node.next = node.next  # Cut it out!
                return node  # Return deleted node
            else:
                prev_node = node
                node = node.next

        return None  # If we got here, nothing found

        # self.buckets[idx] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # 1. Hash the key
        # 2. Take the hash and mod it with the len of array
        idx = self.hash_index(key)
        # 3. Go to index and traverse our LL
        node = self.buckets[idx]

        while node is not None:
            if node.key == key:  # key was found
                return node.value  # return its value

            # cycle to next node
            node = node.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # Store old list
        old_buckets = self.buckets

        # Update capacity
        self.capacity = new_capacity

        # Create new list with new capacity
        self.buckets = [None] * new_capacity

        # loop through old list
        for node in old_buckets:
            while node is not None:
                # insert node into new list
                self.put(node.key, node.value)
                # cycle to next node
                node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


ht2 = HashTable(8)
print(ht2.djb2("car"))
print(ht2.djb2("rae"))
print(ht2.hash_index("car"))
ht2.put("Toyota", "Tacoma")
ht2.put("Honda", "Accord")
ht2.put("Porsche", "911")
print(ht2.capacity)
print(ht2.get("Honda"))
print(ht2.get("Toyota"))
print(ht2.get("Porsche"))
ht2.delete("Porsche")
ht2.delete("Honda")
print(ht2.get("Toyota"))
print(ht2.buckets)
