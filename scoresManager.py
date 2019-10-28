#!/usr/bin/python3.7
# -*-coding:utf-8 -*

import pickle
import constants

def saveScores(pScore):
	with open(constants.SAVE_FILE, 'wb') as wFile:
		pick = pickle.Pickler(wFile)
		pick.dump(pScore)

def loadScores():
	with open(constants.SAVE_FILE, 'rb') as rFile:
		unPick = pickle.Unpickler(rFile)
		return unPick.load()

def	checkSavedScores():
	retScores = {}

	try:
			retScores = loadScores()
	except FileNotFoundError:
			saveScore(retScores)

	return retScores
