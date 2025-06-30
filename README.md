# TOTVS Include Decompress

A Python utility to decompress binary TOTVS include files (.ch and .th) into readable text format.

## Overview

This tool helps developers work with TOTVS include files by decompressing the binary format used by TOTVS Protheus into readable text files. It processes compressed .ch (C Header) files from the TOTVS framework and converts them to plain text for analysis and development purposes.

## Features

- ✅ Decompress .ch (C Header) files
- ✅ Batch processing of entire include folder
- ✅ UTF-8 encoding support
- ✅ Error handling for corrupted files
- ✅ Automatic output file naming

## Requirements

- Python 3.6 or higher
- No external dependencies (uses built-in `zlib` module)

## Getting Started

### Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/totvs-include-decompress.git
cd totvs-include-decompress
```

2. Ensure you have Python installed:
```bash
python --version
```

### Usage

#### Batch Processing (Recommended)

Process all .ch files in the `include` folder:

```bash
python decompress.py
```

This will:
- Scan the `include` folder for .ch files
- Decompress each file
- Create output files with prefix `decompressed_` and `.txt` extension

#### Single File Processing

You can also process individual files by modifying the script or using command line redirection:

```bash
python decompress.py > output.txt
```

### Project Structure

```
totvs-include-decompress/
├── decompress.py          # Main decompression script
├── README.md             # This file
└── include/              # Folder containing binary .ch files
    ├── ap5mail.ch
    ├── protheus.ch
    ├── sigawin.ch
    └── ...               # Other TOTVS include files
```

### Output

The tool generates decompressed text files with the following naming pattern:
- Input: `sigawin.ch`
- Output: `decompressed_sigawin.ch.txt`

## Example

```bash
$ python decompress.py
Processing ap5mail.ch...
File 'decompressed_ap5mail.ch.txt' created successfully.
Processing protheus.ch...
File 'decompressed_protheus.ch.txt' created successfully.
Processing sigawin.ch...
File 'decompressed_sigawin.ch.txt' created successfully.
```

## How It Works

The decompression process:

1. Reads the binary .ch file
2. Skips the first 14 bytes (header)
3. Uses zlib decompression with negative MAX_WBITS
4. Decodes the result as UTF-8
5. Saves to a text file

## Troubleshooting

### Common Issues

**"Include folder 'include' not found!"**
- Ensure you have an `include` folder in the same directory as `decompress.py`
- Place your .ch files in this folder

**Encoding errors**
- The script uses `errors='ignore'` to handle encoding issues
- Some characters might be lost in corrupted files

**File processing errors**
- Check if the .ch file is a valid TOTVS include file
- Ensure the file isn't corrupted or empty

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and development purposes. Ensure you have the proper rights to decompress and analyze TOTVS include files.
