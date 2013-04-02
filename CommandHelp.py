# -*- coding: utf8 -*-

from CommandAbstract import CommandAbstract
from CommandException import CommandException


class CommandHelp(CommandAbstract):
	def run(self):
		print('Available commands:')
		print('talk <Character name> "<Sentence>": Talk to a character')
		print('move <south|east|west|north>: Go to the indicated direction')
		print('look: See what is in the current area' +
			' (characters, items, neighbour areas...)')
		print('createPlayer: Not Yet Implemented')
		print('help: Display this help')
		print('quit|exit|q: Quit the game')
