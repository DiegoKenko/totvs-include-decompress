#sample: ./decompress.py .\includes\sigawin.ch > sigawin.ch

import zlib
import sys
import os

def create_txt_file(content, filename):
    """Create a txt file with the given content"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"File '{filename}' created successfully.")

def decompress_file(input_file, output_file):
    """Decompress a single file"""
    try:
        with open(input_file, 'rb') as f:
            content = f.read()
        
        decompress = zlib.decompressobj(-zlib.MAX_WBITS)
        inflated = decompress.decompress(content[14:])
        inflated += decompress.flush()
        
        decoded_content = inflated[:-1].decode('utf-8', errors='ignore')
        create_txt_file(decoded_content, output_file)
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Process all files in the include folder
include_folder = "include"
if os.path.exists(include_folder):
    for filename in os.listdir(include_folder):
        if filename.endswith('.ch'):  # Only process .ch files
            input_path = os.path.join(include_folder, filename)
            output_path = f"decompressed_{filename}.txt"
            print(f"Processing {filename}...")
            decompress_file(input_path, output_path)
else:
    print(f"Include folder '{include_folder}' not found!")
