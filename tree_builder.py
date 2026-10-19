class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, value): 
        self.value = value 
        self.left = None 
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        
        if self.root is None:
            print("Team is empty.")
            return
    
        if current_node is None:
            current_node = self.root 
    
        if current_node.value == manager_name: 
            if side == "left" and current_node.left is None: 
                current_node.left = EmployeeNode(employee_name) 
                print(f"{employee_name} added under {manager_name} on the left.") 
                return True 
            elif side == "right" and current_node.right is None: 
                current_node.right = EmployeeNode(employee_name) 
                print(f"{employee_name} added under {manager_name} on the right.") 
                return True 
            else: 
                print(f"{manager_name} already has a {side} subordinate.") 
            return True
    
        found_left = False
        found_right = False
    
        if current_node.left:
            found_left = self.insert(manager_name, employee_name, side, current_node.left)
    
        if current_node.right and not found_left:
            found_right = self.insert(manager_name, employee_name, side, current_node.right)
    
        if not(found_left or found_right):
            if current_node == self.root:
                print(f"Manager {manager_name} not found in the tree.")
            return False
    
        return True

    def print_tree(self, node=None, level=0):
        if node is None: 
            if level == 0:
                node = self.root
            else:
                return

        indent = "  " * level
        print(indent + f"- {node.value}")
    
        self.print_tree(node.left, level + 1) 
        self.print_tree(node.right, level + 1)


def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

company_directory()

'''
DESIGN MEMO:
How did recursive insertion work?
    The recursive insertion has a few parts. First, it checks if the tree is empty.
    If not, it sets the current node as the root if it's not a recursive call.
    Then it checks the current node to see if it is the parent. If so, check if the chosen side is available.
    If not, it throws an error message. If it is available, add it and move on.
    If the current node is not the desired parent, recursively check both sides of the tree and repeat the process.
    If the desired parent is never found, print an error message.

What challenges did you face when finding the right spot for a new employee?
    The more challenging part of this design is the recursive part. 
    Ensuring that the recursion is called with the right values took some effort.
    Most of the other cases were comparatively less complicated.

When might trees be preferable to other data structures in real-world systems?
    Trees are generally preferable when they represent some sort of hierarchy. This implementation is a good example, but a hierarchy
    of any kind works well with a tree due to its nature. Another example could be a family tree starting from a specific person.

'''