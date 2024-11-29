class MemoryBlock:
    def __init__(self, block_id, start_address, size):
        self.id = block_id
        self.start = start_address
        self.end = start_address + size - 1
        self.next = None

# Global variables for the memory allocator
pm_size = 0
memory_start = None
algorithm = 0  # 0=First Fit, 1=Best Fit

def enter_parameters():
    global pm_size, algorithm
    # Ask user for the size of physical memory
    # Ask user for the hole-fitting algorithm to use
    # Initialize memory_start with the full size of the physical memory as an empty block

def allocate_memory():
    global memory_start, algorithm
    # Ask for block id and size
    # Check for duplicate id and if enough memory exists using the chosen strategy
    # Depending on the algorithm, call first_fit or best_fit to find suitable position
    # Insert the block into the linked list if space is found, or print error if not

def first_fit(size):
    # Implement first-fit memory allocation
    # Return the starting address if a block is found, or None if no suitable block is found
    pass

def best_fit(size):
    # Implement best-fit memory allocation
    # Return the starting address if a block is found, or None if no suitable block is found
    pass

def deallocate_memory():
    global memory_start
    # Ask for the block id to deallocate
    # Remove the block from the linked list if found
    # Combine adjacent free spaces (if any) to form a single larger hole

def defragment_memory():
    global memory_start
    # Compacts the blocks to be contiguous
    # Coalesces the holes into one large hole at the far-right end
    # Updates the addresses of the blocks and the free space accordingly

def print_memory():
    global memory_start
    # Print the current state of memory including ids and start-end addresses of all blocks

# ------------------
# Main Program Logic
# ------------------

while True:
    print("Memory allocation")
    print("-----------------")
    print("1) Enter parameters")
    print("2) Allocate memory for block")
    print("3) Deallocate memory for block")
    print("4) Defragment memory")
    print("5) Quit program")
    choice = int(input("Enter selection: "))

    if choice == 1:
        enter_parameters()
    elif choice == 2:
        allocate_memory()
    elif choice == 3:
        deallocate_memory()
    elif choice == 4:
        defragment_memory()
    elif choice == 5:
        print("Quitting program...")
        break
    else:
        print("Invalid selection.")