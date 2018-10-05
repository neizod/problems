#!/usr/bin/env python3


def main():
	for i in range(int(input())):
		ls = sorted(int(n) for n in input().split())
		print(f'Case {i+1}: {ls[1]}')


if __name__ == '__main__':
	main()
