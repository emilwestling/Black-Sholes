import argparse
import numpy as np
from Blacksholes import heatmap_gen


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description='Generate Black-Scholes heatmap.')
    parser.add_argument('--K', type=float, default=100, help='Strike price')
    parser.add_argument('--r', type=float, default=0.05,
                        help='Risk-free interest rate')
    parser.add_argument('--sigma', type=float, default=0.2, help='Volatility')

    args = parser.parse_args()

    heatmap_gen(args.K, args.r, args.sigma)


if __name__ == "__main__":
    main()
