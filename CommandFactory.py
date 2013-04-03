# -*- coding: utf8 -*-

import Command
from CommandTalk import CommandTalk
from CommandHelp import CommandHelp
from CommandMove import CommandMove
from CommandLook import CommandLook
from CommandException import CommandException
from PlayerException import PlayerException


class CommandFactory:

	@staticmethod
	def create(player, commandFull):
		cmd = commandFull[0]
		del commandFull[0]

		if cmd in ("talk", "move")\
			and (not player.isConnected() or not player.connect()):
			raise PlayerException(
				"A player must be connected to launch the command %s" % cmd
			)

		if cmd == "look":
			command = CommandLook()
		elif cmd == "talk":
			command = CommandTalk()
		elif cmd == "move":
			command = CommandMove()
		elif cmd == "createPlayer":
			if player.isConnected():
				raise PlayerException(
					"You cannot create a new player when you're connected"
				)
		elif cmd in ('quit', 'exit', 'q'):
			return Command.quit
		elif cmd == 'help':
			command = CommandHelp()
		else:
			raise CommandException('Unknown command')

		command.setArgs(commandFull)
		command.setPlayer(player)
		return command
