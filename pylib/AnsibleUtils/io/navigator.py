

import re, sys, os
import json, yaml

import AnsibleUtil.util

DIRECTORIES = ['defaults','vars','files','templates','tasks','handlers','meta']


class Navigator:

	def __initialize__( self, file_or_path, *options ):

		self.file_or_path = file_or_path
		self.debug = False

		if 'debug' in options: self.debug = options['debug']





if( _name_ == '__main__') :
	sys.exit()