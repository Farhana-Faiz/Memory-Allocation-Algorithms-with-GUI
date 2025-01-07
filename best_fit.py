import tkinter as tk
from tkinter import messagebox

# Function to implement Best-Fit Algorithm
def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)  # Initialize allocation array with -1 (not allocated)

    # Allocate memory to each process
    for i in range(len(process_sizes)):
        best_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:  # Check if the block is large enough
                if best_index == -1 or memory_blocks[j] < memory_blocks[best_index]:
                    best_index = j  # Find the block with the least wasted space

        if best_index != -1:  # If a suitable block was found
            allocation[i] = best_index  # Assign the block to the process
            memory_blocks[best_index] -= process_sizes[i]  # Reduce available memory in the block

    return allocation

# Function to display allocation result
def display_allocation():
    try:
        # Get inputs from user
        memory_blocks = list(map(int, entry_blocks.get().split(',')))
        process_sizes = list(map(int, entry_processes.get().split(',')))

        # Call the best-fit function
        allocation = best_fit(memory_blocks, process_sizes)

        # Prepare the result message
        result = ""  # Initialize result string
        for i in range(len(process_sizes)):
            if allocation[i] != -1:
                result += f"Process {i + 1} (Size {process_sizes[i]}) allocated to Block {allocation[i] + 1}\n"
            else:
                result += f"Process {i + 1} (Size {process_sizes[i]}) not allocated\n"

        # Show the result in the GUI
        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers separated by commas.")

# Function to reset the input and output fields
def reset_fields():
    entry_blocks.delete(0, tk.END)
    entry_processes.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Best-Fit Memory Allocation")
root.geometry("500x400")

# Title label
title_label = tk.Label(root, text="Best-Fit Memory Allocation Algorithm", font=("Arial", 16, "bold"), pady=10)
title_label.pack()

# Input for memory blocks
frame_blocks = tk.Frame(root)
frame_blocks.pack(pady=10)
blocks_label = tk.Label(frame_blocks, text="Memory Blocks (comma-separated):", font=("Arial", 12))
blocks_label.pack(side=tk.LEFT)
entry_blocks = tk.Entry(frame_blocks, width=30, font=("Arial", 12))
entry_blocks.pack(side=tk.LEFT, padx=5)

# Input for process sizes
frame_processes = tk.Frame(root)
frame_processes.pack(pady=10)
processes_label = tk.Label(frame_processes, text="Process Sizes (comma-separated):", font=("Arial", 12))
processes_label.pack(side=tk.LEFT)
entry_processes = tk.Entry(frame_processes, width=30, font=("Arial", 12))
entry_processes.pack(side=tk.LEFT, padx=5)

# Button to allocate memory
allocate_button = tk.Button(root, text="Allocate Memory", font=("Arial", 12), command=display_allocation)
allocate_button.pack(pady=10)

# Button to reset fields
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset_fields)
reset_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", justify=tk.LEFT)
result_label.pack(pady=20)

# Run the main event loop
root.mainloop()
