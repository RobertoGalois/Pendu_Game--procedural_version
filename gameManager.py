#!/usr/bin/python3.7
# -*-coding:utf-8 -*

import random
import gameMsgs
import constants
import time

def pickRandomWord():
	try:
		with open(constants.DICT_FILE, 'r') as rFile:
			line = next(rFile)
			for num, aline in enumerate(rFile, 2):
				if random.randrange(num):
					continue

				line = aline
			return line[:len(line) - 1]
	except FileNotFoundError:
		print('ERROR: pas de fichier dictionnaire "words.txt" dans le repertoire.')
		print('Le programme a besoin dans son répertoire d\'un fichier texte "words.txt" avec la liste des mots que le programme pourra tirer pour jouer.')
		exit(1)

def inputUserName():
	retUserName = ''

	while (retUserName.strip() == ''):
		retUserName = input('--> Comment vous appellez-vous ? ')

	return retUserName

def inputLetter(alreadyTriedLetters):
	retLetter = ''

	while (len(retLetter) != 1 or retLetter.isalpha() == False or retLetter in alreadyTriedLetters):
		retLetter = input('--> Essayez une lettre (a->z): ')
		if (retLetter in alreadyTriedLetters):
			print("    |--> Vous avez déjà tenté la lettre [", retLetter , "] auparavant !")

	return (retLetter.lower())

def game():
	chosenWord = pickRandomWord()
#	print(chosenWord)
	shownWord = ['*' for letter in chosenWord]
	remainedFails = 8
	testLetter = ''
	alreadyTriedLetters = []

	while ('*' in shownWord and remainedFails > 0):
		print('---------------------')
		print('Mot mystère: [ ', "".join(shownWord), ' ] - (', remainedFails ,' échecs restants)\n', sep='')
		testLetter = inputLetter(alreadyTriedLetters)
		alreadyTriedLetters.append(testLetter)

		if (testLetter in chosenWord):
			print('    --> OUI ! Vous avez trouvé la lettre [', testLetter, '] !\n')
			for indx, letter in enumerate(chosenWord):
				if (letter == testLetter):
					shownWord[indx] = testLetter

		else:
			remainedFails -= 1
			print('    --> NOPE. Pas de [', testLetter , '] dans le mot mystère. Vous perdez 1 essai.\n')

		time.sleep(2)

	#if it is a victory
	if (remainedFails > 0):
		gameMsgs.showVictoryMsg()
		print('    --> Il s\'agissait du mot [', chosenWord ,']')
		print('    --> Vous gagnez', remainedFails , ' points !')

	else:
		gameMsgs.showFailMsg()
		print('    --> Il s\'agissait du mot [', chosenWord ,']')

	return (remainedFails)
