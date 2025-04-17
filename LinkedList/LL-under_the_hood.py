# Example of how a Linked List works under the hood using a dictionary
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# Accessing the value of the third node by traversing the dictionary
# Start at the head, go to the next node, then the next, and finally get the value
print(head['next']['next']['value'])  # Output: 23