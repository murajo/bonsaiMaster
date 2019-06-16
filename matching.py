# 使い方はDB仕様書
def matchingRoot(rootLog=""):
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
def resultGet(rootLog=""):
	if rootLog == '':
		return 0
	elif rootLog == "111":
		return {'id':3,'name':'黒松'}
	elif rootLog == "112":
		return {'id':13,'name':'真柏'}
	elif rootLog == "121":
		return {'id':10,'name':'五葉松'}
	elif rootLog == "122":
		return {'id':14,'name':'赤松'}
	elif rootLog == "21":
		return {'id':5,'name':'皐月'}
	elif rootLog == "22":
		return {'id':18,'name':'百日紅'}
	elif rootLog == "23":
		return {'id':9,'name':'銀杏'}
	elif rootLog == "24":
		return {'id':15,'name':'椿'}
	elif rootLog == "311":
		return {'id':2,'name':'キンズ'}
	elif rootLog == "312":
		return {'id':12,'name':'紫式部'}
	elif rootLog == "321":
		return {'id':4,'name':'さくらんぼ'}
	elif rootLog == "322":
		return {'id':17,'name':'白あけび'}
	elif rootLog == "411":
		return {'id':7,'name':'もみじ'}
	elif rootLog == "412":
		return {'id':1,'name':'オリーブ'}
	elif rootLog == "421":
		return {'id':5,'name':'サツキ'}
	elif rootLog == "422":
		return {'id':6,'name':'チリメンカズラ'}
	elif rootLog == "51":
		return {'id':10,'name':'五葉松'}
	elif rootLog == "52":
		return {'id':11,'name':'桜'}
	elif rootLog == "53":
		return {'id':0,'name':'りんごの木'}