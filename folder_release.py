import os
import argparse
import shutil

parser = argparse.ArgumentParser(description='释放文件夹')
parser.add_argument('-p', '--path', required=True, type=str, help='要释放的文件夹路径')
args = parser.parse_args()


folder_path = os.path.abspath(args.path)
for file in os.listdir(folder_path):
    shutil.move(os.path.join(folder_path, file), os.path.join(os.path.dirname(folder_path), file))
