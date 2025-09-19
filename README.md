---

# Gaussian\_log\_to\_smiles

A lightweight Python script to extract molecular structures from Gaussian log files and convert them to canonical SMILES.

## Features

* Automatically reads all `.log` files in a directory.
* Converts valid Gaussian log files to canonical SMILES using **Pybel** and **RDKit**.
* Skips files with Gaussian error terminations and prints a clear warning message (added in **v1.1.0**).
* Outputs a clean `.csv` file containing molecule names and SMILES.

## Usage

1. **Prepare your files**
   Place your Gaussian `.log` files in the same folder as `log_to_smiles.py` (or specify another directory).

2. **Run the script**

   ```bash
   python log_to_smiles.py
   ```

   or specify a folder:

   ```bash
   python log_to_smiles.py /path/to/log/files
   ```

3. **Get your results**

   * The script converts all valid log files to canonical SMILES.
   * Skipped files (with Gaussian errors) are listed with warning messages.
   * Results are saved to `result.csv`.

## Requirements

* Python 3.x
* RDKit
* OpenBabel / Pybel
* Pandas

---

要不要我在这个 README 里加一个 **Example input / output**（示例输入输出）的小节，让别人一眼看懂？
