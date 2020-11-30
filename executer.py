from mcrcon import MCRcon
from sys import argv
from model import models
import json
import config

if len(argv) != 2:
	print('Enter object file')
	exit(1)
	
NO_AI = 1

data = None
try:
	with open(argv[1], 'r') as fd:
		data = json.load(fd)
except FileNotFoundError:
	print('No such file')
	exit(0)
except json.decoder.JSONDecodeError:
	print('JSON corrupted')
	exit(0)
	
with MCRcon(*config.server_data) as mcr:
	for el in data:
		print(mcr.command(models[el[0]].format(*el[1:4], NO_AI, *el[-2:])))
