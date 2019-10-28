#!/usr/bin/python3.7
# -*-coding:utf-8 -*

import gameMsgs
import scoresManager
import gameManager
import time

try:
	gameMsgs.showWelcomeMsg()
	userName = gameManager.inputUserName()
	allScores = scoresManager.checkSavedScores()
	keepOnPlaying = True

	if (userName in allScores.keys()):
		print("\nBonjour {0} !\n--> Votre capital est de [{1} points].".format(userName, allScores[userName]))
	else:
		print("\nBonjour {0} ! Vous êtes nouveau.elle par ici visiblement :). Bienvenue !".format(userName))
		print("--> Vous démarrez avec un capital de [0 points].")
		allScores[userName] = 0
		scoresManager.saveScores(allScores)

	time.sleep(2)
	while (keepOnPlaying):
		gameMsgs.showNewGameMsg()
		allScores[userName] += gameManager.game()
		scoresManager.saveScores(allScores)

		print('    --> Votre score total est de {0} points.'.format(allScores[userName]))
		if (input('\n\nVoulez-vous faire une nouvelle partie {0} ? (O pour OUI, N pour NON) ==> '.format(userName)).lower() != 'o'):
			keepOnPlaying = False

	gameMsgs.showGoodByeMsg()

except KeyboardInterrupt:
	print('\n\n\n\n/----------------------------------------------------------------\\')
	print('|Oh quoi vous vous arrêtez comme ca d\'un coup d\'un seul ? Bien...|')
	print('\----------------------------------------------------------------/')

	try:
		print('Vous partez avec', allScores[userName], 'points.')
		scoresManager.saveScores(allScores)
	except NameError:
		print('Nous ne saurons même pas qui vous êtes... Dommage :(')

	gameMsgs.showGoodByeMsg()
