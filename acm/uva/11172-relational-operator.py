#!/usr/bin/env python3


def main():
	for _ in range(int(input())):
		n, m = [int(n) for n in input().split()]
		ans = '<' if n < m else '>' if n > m else '='
		print(ans)


if __name__ == '__main__':
	main()
