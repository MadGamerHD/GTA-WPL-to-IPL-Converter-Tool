# WPL to IPL Converter Tool

## Overview

The **WPL to IPL Converter** is a Python-based tool designed for converting GTA IV WPL files into the IPL format used by GTA: San Andreas. This tool provides a straightforward interface, enabling users to convert WPL files seamlessly into the compatible IPL format necessary for modding and game development.

## Features

- **User-Friendly Interface**: Built using Tkinter, the application offers an intuitive graphical user interface (GUI) for ease of use.
- **Input File Selection**: Users can easily select a WPL file for conversion.
- **Output Directory Selection**: The tool allows users to specify the output directory where the converted IPL files will be saved.
- **Conversion Logic**: The script reads the contents of the selected WPL file, processes the relevant data, and generates an IPL file formatted according to the specifications of GTA: San Andreas.
- **Data Mapping**: The conversion handles necessary adjustments to model names and positional data to ensure compatibility with the IPL format.
- **Error Handling**: Basic error handling is included to alert users of any issues during the conversion process.

## Requirements

To run the **WPL to IPL Converter Tool**, you need Python installed on your machine. This tool requires the following Python packages:

- **Tkinter**: This library is typically included with standard Python installations, providing the GUI framework for the application.

### Install Required Packages

To ensure you have the necessary packages, you may use pip for any additional dependencies. Run the following command in your terminal or command prompt:

```bash
pip install tkinter
```

## Code Structure

- **Function Definitions**:
  - **`clean_name(name)`**: Cleans up model names by removing numeric suffixes, ensuring that names are formatted correctly for the IPL file.
  - **`convert_wpl_to_ipl(input_file, output_dir)`**: Handles the core conversion process, reading the WPL file and writing the corresponding IPL data to the specified output directory.

- **Tkinter GUI Components**:
  - The GUI includes buttons for selecting input files and output directories, along with a button to initiate the conversion.
  - Message boxes provide feedback to the user regarding the success or failure of the conversion process.

## Usage

The WPL to IPL Converter Tool simplifies the process of converting WPL files for modding enthusiasts and game developers, making it easier to prepare assets for use in GTA: San Andreas.
