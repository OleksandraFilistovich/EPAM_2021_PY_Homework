"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""

import argparse
# empty, <=0, float, w_n != n


def bounded_knapsack(W, weights, n):
    """
    Counts 'max' weight of bag with given bars. GREEDY
    * with many checks

    :param W: capacity of a bag
    :param weights: weights of all bars
    :param n: number of bars
    :return: max weight counted with greedy method
    """

    value_error = False

    if not W or W <= 0:
        value_error = True

    elif not n or n <= 0:
        value_error = True
    elif int(n) != len(weights):
        value_error = True
    else:
        for weight in weights:
            if weight <= 0:
                value_error = True

    if value_error:
        raise ValueError
    else:
        weights = [int(w) for w in weights]
        weights.sort(reverse=True)
        current = 0

        for weight in weights:
            if (current + weight) <= W:
                current += weight

        return current

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', type=int,
                        help='Capacity of a bag.')
    parser.add_argument('-w', nargs='*', type=int,
                        help='Weights of all bars.')
    parser.add_argument('-n', type=int,
                        help='Number of bars.')

    args = parser.parse_args()

    print(bounded_knapsack(args.W,args.w,args.n))


if __name__ == '__main__':
    main()
