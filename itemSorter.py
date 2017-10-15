import csv
import difflib

allItems = []
transactionItems = {}
userPurchases = {}
popItem = {}
maxArr = 0
allProducts = []
allProductVals = {}

def readItems():
	csvfile = open('10000_transactions.csv', "rb")
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		global allItems
		allItems.append(row)
	global allItems
	allItems = allItems[1:]

def readProducts():
	csvfile = open('catalog.csv', "rb")
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		global allProductVals
		allProductVals[row[1]] = row[0]
		global allProducts
		allProducts.append(row[1])
	global allItems
	allItems = allItems[1:]

def popularItems():
	for i in range(0, len(allItems)):
		if allItems[i][2] not in userPurchases:
			userPurchases[allItems[i][2]] = [allItems[i][1]]
		else:
			if allItems[i][1] not in userPurchases[allItems[i][2]]:
				userPurchases[allItems[i][2]].append(allItems[i][1])
		if allItems[i][1] not in transactionItems:
			transactionItems[allItems[i][1]] = [allItems[i][2]]
		else:
			if allItems[i][2] not in transactionItems[allItems[i][1]]:
				transactionItems[allItems[i][1]].append(allItems[i][2])
	for i in userPurchases:
		count = len(userPurchases[i])
		if count > maxArr:
			global maxArr
			maxArr = count
		if count not in popItem:
			popItem[count] = [userPurchases[i]]
		else:
			popItem[count].append(userPurchases[i])


def getSimilarItem(inputList):
	similarityList = []
	for i in range(0, len(inputList)):
		simFound = difflib.get_close_matches(inputList[i], allProducts)
		if len(simFound) > 0:
			similarityList.append(allProductVals[simFound])
	return similarityList
