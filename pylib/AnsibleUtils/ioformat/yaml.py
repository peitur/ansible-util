import re, sys, os
import json, yaml

import AnsibleUtils.util
from AnsibleUtils.ioformat.ioformat import IoFormat

class Yaml( IoFormat ):
	def __init__( self, **options ):
		if 'overwrite' in options: self.complete = options['overwrite']
		super( Yaml, self ).__init__( **options )



	def write( self, data, **options ):
		"""
			
		"""

		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename


		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if 'filename' in options: filename = options['filename']

		if(debug) : print("DEBUG[WriteYaml]: F:%(filename)s" % {'filename': filename})

		if( os.path.exists( filename ) and not overwrite ): 
			raise RuntimeError( "File overwrite is refused on existsing file" )

		try:
			fd = open( filename, "w" )
			yaml.dump( data, fd , explicit_start=True, default_flow_style=False )
			fd.close()
		except Exception as error:
			print("ERROR[WriteYaml]: %(error)s" % { 'error':error} )
			raise
			
		return True


	def read( self, **options ):
		"""
		
		"""

		filename = self.filename
		if 'filename' in options: filename = options['filename']

		debug = self.debug
		if 'debug' in options: debug = options['debug']

		data = ""
		try:
			fd = open( filename, "r" )
			for line in fd:	
				data += line

			fd.close()

			return yaml.load( data )
		except:
			raise

		return None


	



if( __name__ == '__main__') :
	sys.exit()