# 使い方はDB仕様書
def matchingRoot(rootLog):
	if rootLog == '':
		return 1
	elif len(rootLog) == 1:
		if rootLog == '1' or rootLog == '4':
			return 2
		elif rootLog == '2':
			return 4
		elif rootLog == '3':
			return 5
		else:
			return 8
	elif len(rootLog) == 2:
		if rootLog[0] == '1':
			return 3
		elif rootLog[0] == '2' or rootLog[0] == '5':
			return 0
		elif rootLog[0] == '3':
			return 6
		elif rootLog[0] == '4':
			return 7
	elif len(rootLog) == 3:
		return 0