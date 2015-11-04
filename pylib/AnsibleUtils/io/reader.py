
import re, sys, os
import json, yaml

import AnsibleUtil.util


class Reader:
	
	def __initialize__( self, *options ):

		self.filename = filename
		self.debug = False

		if 'format' in options: self.format = options['format']
		if 'debug' in options: self.debug = options['debug']



	def load_yaml( self, options ):
		debug = self.debug
		if 'debug' in options: debug = options['debug']


		filename = self.filename

		data = ""
		try:
			fd = open( filename, "r" )
			for line in fd:	
				data += line

			return yaml.load( data )
		except:
			raise
		finally:
			if( fd ): fd.close()

		return None


	def load_json( self, options ):
		debug = self.debug

		filename = self.filename

		if 'debug' in options: debug = options['debug']

		data = ""
		try:
			fd = open( filename, "r" )
			for line in fd:	
				data += line
			return json.loads( data )
		except:
			raise
		finally:
			if( fd ): fd.close()

		return None



	def read_file( self, *options ):

		filename = self.filename

		pass