
import re, sys, os, getopt
import json, yaml

import AnsibleUtil.util

class Writer:

	def __initialize( self, filename, *options ):

		self.filename = filename
		self.overwrite = True
		self.debug = False
		self.format = 'yaml'

		if 'format' in options: self.format = options['format']
		if 'debug' in options: self.debug = options['debug']
		if 'overwrite' in options: self.complete = options['overwrite']



	def write_yaml_file( self, data, *options ):

		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename


		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if(debug) : print("DEBUG[WriteYaml]: F:%(filename)s" % {'filename': filename})

		if( os.path.exists( filename ) and not overwrite ): return None

		try:
			fd = open( filename, "w" )
			yaml.dump( data, fd , explicit_start=True, default_flow_style=False )
			fd.close()
		except Exception as error:
			print("ERROR[WriteYaml]: %(error)s" & {error} )
			raise
			
		return True


	def write_json_file( self, data, *options ):

		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename

		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if(debug) : print("DEBUG[WriteJson]: F:%(filename)s" % {'filename': filename})

		if( os.path.exists( filename) and not overwrite ): return None

		try:
			fd = open( filename, "w" )
			fd.write( json.dumps( data ) )
			fd.close()
		except Exception as error:
			print("ERROR[WriteJson]: %(error)s" & {error} )
			raise
			
		return True

	def write_file( self, data, *options ):

		format = self.format
		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename

		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if 'format' in options: format = options['format']

		if( is_json( filename ) ):
			format = 'json'

		if( is_yaml( filename ) ):
			format = 'yaml'

		if(debug) : print("DEBUG[WriteFile]: File:%(filename)s D:%(debug)s O:%(overwrite)s F:%(format)s" % {'filename': filename, 'debug':debug, 'overwrite':overwrite, 'format':format})



		if( format == 'yaml') : 
			return write_yaml_file( filename, data )

		elif( format == 'json' ):
			return write_json_file( filename, data )

		else:
			print("ERROR: Unknown file format : %(format)s " % { 'format': format } )

		return None





if( _name_ == '__main__'):
	sys.exit()
