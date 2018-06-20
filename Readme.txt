Language used: Python
OS used: Kali Linux

File descriptions:

pow.py - Implements POW
pow_performance.py - Takes difficulty, d, message file, input.txt and computes execution time while displaying solution

How to use:

1. Target
python pow.py -t d /path/to/input.txt
2. Solution
python pow.py -s /path/to/input.txt /path/to/target.txt /path/to/solution.txt
3. Verify
python pow.py -v /path/to/input.txt /path/to/target.txt /path/to/solution.txt

Example commands:

Target:
python pow.py -t 10 ../data/input.txt


Solution:
python pow.py -s ../data/input.txt ../data/target.txt ../data/solution.txt

Verify:
python pow.py -v ../data/input.txt ../data/target.txt ../data/solution.txt

Performance evaluation exercise:

To compute execution time for a difficulty d, run
python pow_performance.py d ../data/input.txt

Example commands:
python pow_performance.py 21 ../data/input.txt
python pow_performance.py 22 ../data/input.txt
python pow_performance.py 23 ../data/input.txt
python pow_performance.py 24 ../data/input.txt
python pow_performance.py 25 ../data/input.txt
python pow_performance.py 26 ../data/input.txt
