import requests
import pdb
import os
from datetime import datetime

SCRIPT_PATH = os.path.dirname(
	os.path.abspath(__file__)
)


def main(query):
	engine_url = 'https://duckduckgo.com'
	params = {
		'q': query,
		'ia': 'web'
	}
	headers = {
		'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'
	}

	res = requests.get(
		engine_url, params, headers=headers)

	out_file = 'search_results_{:%Y%m%d-%H%M%S}.txt'.format(
		datetime.now()
	)

	with open(out_file, 'w') as fh:
		fh.write(res.text)




if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'query',
		help='Search term'
	)

	args = parser.parse_args()
	main(args.query)