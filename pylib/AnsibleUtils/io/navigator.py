

import re, sys, os

from AnsibleUtils.util import util

DIRECTORIES = ['defaults','vars','files','templates','tasks','handlers','meta']
TYPES = ['playbook','role']

class Navigator:

	def __init__( self, file_or_path, options = {} ):

		self.file_or_path = file_or_path
		self.debug = False


		if 'debug' in options: self.debug = options['debug']





if( _name_ == '__main__') :
	sys.exit()