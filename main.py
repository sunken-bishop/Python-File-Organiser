import pathlib, shutil, argparse

parser = argparse.ArgumentParser(description="Process some files.")
parser.add_argument("src")
parser.add_argument("dst")

args = parser.parse_args()

shutil.move(args.src, args.dst)

