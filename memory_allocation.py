class MemoryBlock:
    def __init__(self, block_id, start_address, size):
        self.id = block_id
        self.start = start_address
        self.end = start_address + size - 1
        self.next = None

# Global variables for the memory allocator
pm_size = 0
memory_start = None
algorithm = 0

def enter_parameters():
    global pm_size, algorithm, memory_start
    
    pm_size = int(input("Enter size of physical memory: "))
    algorithm = int(input("Enter hole-fitting algorithm (0=first fit, 1=best fit): "))
    print()

def allocate_memory():
    global memory_start, algorithm
    
    block_id = int(input("Enter block id: "))
    block_size = int(input("Enter block size: "))
    print()

    if algorithm == 0:
        start_address = first_fit(block_id, block_size)
    elif algorithm == 1:
        start_address = best_fit(block_id, block_size)
    else:
        print("Invalid algorithm.")
        return

    if start_address is None:
        print(f"Not enough space or duplicate block found for block {block_id}")
        return

    new_block = MemoryBlock(block_id, start_address, block_size)
    current = memory_start
    prev = None

    while current and current.start < start_address:
        prev = current
        current = current.next
    
    if prev is None:
        new_block.next = memory_start
        memory_start = new_block
    else:
        prev.next = new_block
        new_block.next = current

def first_fit(size):
    # Implement first-fit memory allocation
    # Return the starting address if a block is found, or None if no suitable block is found
    pass

def best_fit(id, size):
    global memory_start

    current = memory_start

    while current:
        if current.id == id:
            return None
        current = current.next

    
    best_start = None
    best_size = None
    current = memory_start

    last_end = 0

    while current:
        gap_size = current.start - last_end
    
        if gap_size >= size and (best_size is None or gap_size < best_size):
            best_start = last_end
            best_size = gap_size

        last_end = current.end + 1
        current = current.next

    
    if pm_size - last_end >= size and (best_size is None or pm_size - last_end < best_size):
        best_start = last_end
        best_size = pm_size - last_end
        
    return best_start

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
    print("ID\tStart\tEnd")
    print("-------------------")
    current = memory_start
    while current:
        print(f"{current.id}\t{current.start}\t{current.end}")
        current = current.next
    print()

# ------------------ Print the current state of memory including ids and start-end addresses of all blocks
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
    print()
    choice = int(input("Enter selection: "))

    if choice == 1:
        enter_parameters()
    elif choice == 2:
        allocate_memory()
        print_memory()
    elif choice == 3:
        deallocate_memory()
    elif choice == 4:
        defragment_memory()
    elif choice == 5:
        print("Quitting program...")
        break
    else:
        print("Invalid selection.")