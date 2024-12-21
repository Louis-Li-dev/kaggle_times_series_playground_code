import argparse
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--train_csv', type=str, default='../data/train.csv', help='Path to the training CSV file')
parser.add_argument('--test_csv', type=str, default='../data/test.csv', help='Path to the test CSV file')
parser.add_argument('--output', type=str, default='../output/', help='Path to the output directory')
# Check if the script is running in a Jupyter notebook
if 'ipykernel' in sys.modules:
    args = parser.parse_args([])
else:
    args = parser.parse_args()
