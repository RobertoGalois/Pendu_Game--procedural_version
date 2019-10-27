#!/usr/bin/python3.7
# -*-coding:utf-8 -*

import pickle
import random

def saveScore(pScore):
	with open('./saves.s', 'wb') as wFile:
		pick = pickle.Pickler(wFile)
		pick.dump(pScore)

def loadScores():
	with open('./saves.s', 'rb') as rFile:
		unPick = pickle.Unpickler(rFile)
		return unPick.load()

def	checkSavedScores():
	retScores = {}

	try:
			retScores = loadScores()
	except FileNotFoundError:
			saveScore(retScores)

	return retScores

def pickRandomWord():
	try:
		with open('words.txt', 'r') as rFile:
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


def inputLetter(triedLetters):
	retLetter = ''
	while (len(retLetter) != 1 or retLetter.isalpha() == False or retLetter in triedLetters):
		retLetter = input('--> Essayez une lettre (a->z): ')
		if (retLetter in triedLetters):
			print("    |--> Vous avez déjà tenté la lettre [", retLetter , "] auparavant !")

	return (retLetter.lower())

def game(pChosenWord):
	shownWord = ['*' for letter in pChosenWord]
	remainedFails = 8
	testLetter = ''
	triedLetters = []

	while ('*' in shownWord and remainedFails > 0):
		print('---------------------')
		print('Mot mystère: [ ', "".join(shownWord), ' ] - (', remainedFails ,' échecs restants)\n', sep='')
		testLetter = inputLetter(triedLetters)
		triedLetters.append(testLetter)

		if (testLetter in pChosenWord):
			print('    --> BRAVO ! Vous avez trouvé la lettre [', testLetter, '] !\n')
			for indx, letter in enumerate(pChosenWord):
				if (letter == testLetter):
					shownWord[indx] = testLetter

		else:
			remainedFails -= 1
			print('    --> Pas de [', testLetter , '] dans le mot mystère. Vous perdez 1 essai.')

	#if it is a victory
	if (remainedFails > 0):
		print('    ---------------------------------------------------')
		print('    |FELICITATIONS VOUS AVEZ TROUVÉ LE MOT MYSTÈRE !!!|')
		print('    ---------------------------------------------------')
		print('    --> Il s\'agissait du mot [', pChosenWord ,']')
		print('    --> Vous gagnez', remainedFails , ' points !')

	else:
		print('    --------------------')
		print('    |VOUS AVEZ PERDU ! |')
		print('    --------------------')
		print('    --> Il s\'agissait du mot [', pChosenWord ,']')

	return (remainedFails)


# MAIN
try:
	print('-========================================-')
	print('| BIENVENUE DANS LE SUPER JEU DU PENDU ! |')
	print('-=======================================-')
	userName = input('--> Comment vous appellez-vous ? ')
	userScore = 0
	allScores = checkSavedScores()
	keepOnPlaying = True

	if (userName in allScores.keys()):
		print("\nBonjour {0} !\n--> Votre capital est de [{1} points].".format(userName, allScores[userName]))
	else:
		print("\nBonjour {0} ! Vous êtes nouveau.elle par ici visiblement :). Bienvenue !".format(userName))
		print("--> Vous démarrez avec un capital de [0 points].")
		allScores[userName] = 0
		saveScore(allScores)

	while (keepOnPlaying):
		print('\n\n\n---------------------')
		print('| NOUVELLE PARTIE ! |')
		print('---------------------')

		chosenWord = pickRandomWord()
		print(chosenWord)
		allScores[userName] += game(chosenWord)
		saveScore(allScores)
		print('    --> Votre score total est de {0} points.'.format(allScores[userName]))
		if (input('\n\nVoulez-vous faire une nouvelle partie {0} ? (O pour OUI, N pour NON) ==> '.format(userName)).lower() != 'o'):
			keepOnPlaying = False

	print('\n\n-===============================-')
	print('| AU REVOIR ! A LA PROCHAINE ! |')
	print('-===================================-')

except KeyboardInterrupt:
	print('\n\nOh quoi vous vous arrêtez comme ca d\'un coup d\'un seul ? Bien...')

	try:
		print('Vous partez avec', allScores[userName], 'points.')
		saveScore(allScores)
	except NameError:
		print('Nous ne saurons même pas qui vous êtes... Dommage :(')

	print('\n\n-===============================-')
	print('| AU REVOIR ! A LA PROCHAINE ! |')
	print('-===================================-')
