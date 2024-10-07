import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_name(name):
    """Remove numeric suffixes from the model name."""
    return re.sub(r'\.\d+$', '', name)

def convert_wpl_to_ipl(input_file, output_dir):
    """Convert GTA IV WPL to GTA SA IPL format."""
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Prepare the output file path
    output_file = os.path.join(output_dir, "output.ipl")
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write("inst\n")
        
        # Read the WPL file line by line
        for line in infile:
            # Skip empty lines and comments
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            # Parse the WPL line (assuming the structure based on your example)
            parts = line.split(',')
            if len(parts) < 7:
                continue  # Skip if the line does not have enough data
            
            # Extract position, rotation, and model name from WPL
            pos_x = float(parts[0].strip())
            pos_y = float(parts[1].strip())
            pos_z = float(parts[2].strip())
            rot_x = float(parts[3].strip())
            rot_y = float(parts[4].strip())
            rot_z = float(parts[5].strip())
            rot_w = float(parts[6].strip())
            model_name = clean_name(parts[7].strip()) if len(parts) > 7 else "Unnamed"
            flags = parts[-1].strip()  # Last element could be flags

            # Write the converted data to the IPL file
            line_to_write = f"0, {model_name}, 0, {pos_x:.6f}, {pos_y:.6f}, {pos_z:.6f}, {rot_x:.6f}, {rot_y:.6f}, {rot_z:.6f}, {rot_w:.6f}, {flags}\n"
            outfile.write(line_to_write)
        
        outfile.write("end\n")

    return output_file

def select_input_file():
    """Open file dialog to select the input WPL file."""
    file_path = filedialog.askopenfilename(title="Select WPL File", filetypes=[("WPL Files", "*.wpl")])
    if file_path:
        input_entry.delete(0, tk.END)  # Clear the current entry
        input_entry.insert(0, file_path)  # Insert the selected file path

def select_output_directory():
    """Open directory dialog to select the output directory."""
    dir_path = filedialog.askdirectory(title="Select Output Directory")
    if dir_path:
        output_entry.delete(0, tk.END)  # Clear the current entry
        output_entry.insert(0, dir_path)  # Insert the selected directory path

def convert_files():
    """Handle the conversion process."""
    input_file = input_entry.get()
    output_dir = output_entry.get()
    
    if not input_file or not output_dir:
        messagebox.showwarning("Input Error", "Please select both input WPL file and output directory.")
        return
    
    try:
        output_file = convert_wpl_to_ipl(input_file, output_dir)
        messagebox.showinfo("Success", f"Conversion complete! Output saved to: {output_file}")
    except Exception as e:
        messagebox.showerror("Conversion Error", f"An error occurred during conversion:\n{str(e)}")

# Setting up the Tkinter GUI
root = tk.Tk()
root.title("WPL to IPL Converter")

# Input File Selection
tk.Label(root, text="Select WPL File:").pack(pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.pack(padx=10, pady=5)
tk.Button(root, text="Browse", command=select_input_file).pack(pady=5)

# Output Directory Selection
tk.Label(root, text="Select Output Directory:").pack(pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.pack(padx=10, pady=5)
tk.Button(root, text="Browse", command=select_output_directory).pack(pady=5)

# Convert Button
tk.Button(root, text="Convert WPL to IPL", command=convert_files).pack(pady=20)

# Run the GUI event loop
root.mainloop()