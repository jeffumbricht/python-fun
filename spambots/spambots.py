#!/usr/bin/env python

def main():
	
	print('\n\n  /\_/\\\n=( °w° )=\n  )   (  //\n (__ __)//\n\n')

	bots = []
	referrers = []
	botsinreferrer = []

	for line in open('bots.txt'):
		bots.append(line.rstrip('\n'))

	for line in open('referrers.txt'):
		referrers.append(line.rstrip('\n'))

	for s in referrers:
		for bot in bots:
			if bot in str(s):
				botsinreferrer.append(s)

	nobots = list(set(referrers) - set(botsinreferrer))

	with open('referrers_nobots.txt', 'w') as thefile:
		for item in nobots:
			thefile.write("%s\n" % item)

	print('removed ' + str(len(botsinreferrer)))

	
if __name__ == '__main__':
	main()