# TOTVS Include Decompress

A Python utility to decompress binary TOTVS include files (.ch and .th) into readable text format.

## Overview

This tool helps developers work with TOTVS include files by decompressing the binary format used by TOTVS Protheus into readable text files. It processes compressed .ch (C Header) and .th (TLPP Header) files from the TOTVS framework and converts them to plain text for analysis and development purposes.

## Features

- ✅ Decompress .ch (C Header) files
- ✅ Decompress .th (TLPP Header) files
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

Process all .ch and .th files in the `include` folder:

```bash
python decompress.py
```

This will:
- Scan the `include` folder for .ch and .th files
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
├── include/              # Folder containing binary include files
│   ├── ap5mail.ch        # C Header files
│   ├── protheus.ch
│   ├── sigawin.ch
│   ├── fw-tlpp-core.th   # TLPP Header files
│   ├── tlpp-object.th
│   └── ...               # Other TOTVS include files
└── extracted/            # Generated decompressed files
    ├── decompressed_*.txt
    └── ...
```

### Output

The tool generates decompressed text files with the following naming pattern:
- Input: `sigawin.ch` → Output: `decompressed_sigawin.ch.txt`
- Input: `tlpp-object.th` → Output: `decompressed_tlpp-object.th.txt`

## File Types Supported

### .ch Files (C Header)
Classic TOTVS Protheus include files containing:
- Macro definitions (`#define`)
- Command translations (`#xcommand`, `#xtranslate`)
- Constants and enumerations
- Legacy AdvPL syntax definitions

### .th Files (TLPP Header)  
TLPP (TOTVS Language++) include files containing:
- Object-oriented programming constructs
- Class and interface definitions
- Modern syntax translations
- Framework-specific definitions

Examples of decompressed .th files:
- `tlpp-object.th` - Core OOP syntax (CLASS, METHOD, DATA declarations)
- `fw-tlpp-core.th` - Framework core definitions
- `fw-tlpp-rest.th` - REST API related definitions
- `totvs.framework.*.th` - Framework structure and model definitions
- `framework.authentication.oidc.th` - OIDC authentication definitions

## Example

```bash
$ python decompress.py
Processing ap5mail.ch...
File 'decompressed_ap5mail.ch.txt' created successfully.
Processing fw-tlpp-core.th...
File 'decompressed_fw-tlpp-core.th.txt' created successfully.
Processing protheus.ch...
File 'decompressed_protheus.ch.txt' created successfully.
Processing tlpp-object.th...
File 'decompressed_tlpp-object.th.txt' created successfully.
Processing sigawin.ch...
File 'decompressed_sigawin.ch.txt' created successfully.
```

## Decompressed Content Examples

### From tlpp-object.th
```advpl
#xcommand CLASS <ClsNam> ;
    [ <from: INHERIT FROM, INHERIT, FROM, OF> [<NSpace>.]<SupCls> ];
    => ;
    _ObjNewClass( <ClsNam> , [<NSpace>.][<SupCls>])

#xcommand METHOD <Met> [ <scp: PUBLIC, EXPORT, LOCAL, HIDDEN> ] => ;
    _ObjClassMethod(_AsName_( <Met> ),_AsParms_([<Met>]), [<scp>])

#xcommand DATA <uVar> [AS <Typ>] ;
    [ <Scp: PUBLIC, EXPORT, READONLY, PROTECTED, LOCAL, HIDDEN> ] ;
    [ <Dft: DEFAULT, INIT> <uData> ] ;
    => _ObjClassData( <uVar>, [<Typ>], [<Scp>], [<uData>] )
```

### From fw-tlpp-core.th
Contains framework core definitions for TLPP development, including namespace declarations and core object structures.

## Use Cases

The decompressed files are valuable for:

### Development & Learning
- **Understanding TOTVS syntax**: Study how AdvPL and TLPP commands are translated
- **Code analysis**: Examine macro definitions and command structures
- **Framework exploration**: Learn about TOTVS framework internals

### Documentation & Reference
- **API reference**: Extract constants, definitions, and available commands
- **Legacy code migration**: Understand older syntax for modernization
- **Custom development**: Reference for creating custom include files

### Debugging & Troubleshooting
- **Syntax issues**: Understand how commands are preprocessed
- **Compilation errors**: Trace macro expansions and translations
- **Framework behavior**: Analyze how framework features are implemented

## How It Works

The decompression process:

1. Reads the binary include file (.ch or .th)
2. Skips the first 14 bytes (header information)
3. Uses zlib decompression with negative MAX_WBITS parameter
4. Decodes the result as UTF-8 text
5. Saves to a readable text file with `.txt` extension

Both .ch and .th files use the same compression algorithm, making them compatible with the same decompression routine.

## Troubleshooting

### Common Issues

**"Include folder 'include' not found!"**
- Ensure you have an `include` folder in the same directory as `decompress.py`
- Place your .ch and .th files in this folder

**Encoding errors**
- The script uses `errors='ignore'` to handle encoding issues
- Some characters might be lost in corrupted files

**File processing errors**
- Check if the file is a valid TOTVS include file (.ch or .th)
- Ensure the file isn't corrupted or empty
- Some older or specially formatted files may fail decompression

**"Error -3 while decompressing data" messages**
- This indicates the file may be corrupted or use a different compression format
- The tool will continue processing other files and report successful decompressions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and development purposes. The decompressed content reveals:
- TOTVS framework internal structures and syntax definitions
- Proprietary macro translations and command implementations  
- TLPP (TOTVS Language++) object-oriented programming constructs

Ensure you have the proper rights to decompress and analyze TOTVS include files. Use the extracted information responsibly and in accordance with TOTVS licensing terms.
