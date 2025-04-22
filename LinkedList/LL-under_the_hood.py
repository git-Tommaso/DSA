# Example of how a Linked List works under the hood using a dictionary
# This demonstrates the basic structure of a linked list where each node
# contains a value and a reference to the next node

# Create a linked list structure using nested dictionaries
# Each dictionary represents a node with 'value' and 'next' keys
head = {
    "value": 11,  # First node's value
    "next": {     # Reference to the second node
        "value": 3,  # Second node's value
        "next": {    # Reference to the third node
            "value": 23,  # Third node's value
            "next": {     # Reference to the fourth node
                "value": 7,  # Fourth node's value
                "next": None  # End of the list
            }
        }
    }
}

# Accessing the value of the third node by traversing the dictionary
# This demonstrates how linked list traversal works:
# 1. Start at the head
# 2. Follow the 'next' references
# 3. Access the 'value' at the desired position
print(head['next']['next']['value'])  # Output: 23

"""
This example illustrates the fundamental concept of linked lists:
- Each node contains data (value) and a reference to the next node
- Nodes are connected through these references
- The last node points to None, indicating the end of the list
- To access a specific node, we must traverse from the head
- This structure allows for dynamic memory allocation and efficient
  insertions/deletions at any position
"""