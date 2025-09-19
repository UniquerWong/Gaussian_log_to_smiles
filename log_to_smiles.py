"""
Uniq ugrd 20/9/2025
version 1.1.0
"""

import os
from rdkit import Chem
import pandas as pd
from openbabel import pybel

def log_to_smiles(input_dir, output_csv='result.csv'):
    data = [] 

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.log'):
            filepath = os.path.join(input_dir, filename)

            try:
                with open(filepath, 'r', errors='ignore') as f:
                    content = f.read()
                if "Error termination" in content or "Error Termination" in content:
                    print(f"{filename} 检测到Gaussian报错,未转换SMILES")
                    continue
            except Exception as e:
                print(f"{filename} 读取log文件失败: {e}")
                continue

            try:
                # 1. 用 Pybel 从 Gaussian log 读分子
                mols = list(pybel.readfile("g09", filepath))
                if len(mols) == 0:
                    print(f"无法读取分子: {filename}")
                    continue

                py_mol = mols[0]

                # 2. 转换成 RDKit 分子
                molblock = py_mol.write("mol")
                rd_mol = Chem.MolFromMolBlock(molblock, sanitize=True)

                if rd_mol is None:
                    print(f"RDKit无法解析molblock: {filename}")
                    continue

                # 3. 得到 canonical SMILES
                smiles = Chem.MolToSmiles(rd_mol, canonical=True)

                name = os.path.splitext(filename)[0]
                data.append([name, smiles])

            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")

    # 4. 输出到CSV（只保存正常转换的文件）
    df = pd.DataFrame(data, columns=['mol', 'smiles'])
    df.to_csv(output_csv, index=False)
    print(f"转换完成，结果已保存至 {output_csv}")

if __name__ == "__main__":
    log_dir = os.path.dirname(os.path.abspath(__file__))
    log_to_smiles(log_dir, output_csv='result.csv')
