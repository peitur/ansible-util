import re, sys, os
import json, yaml

import AnsibleUtils.util
from AnsibleUtils.ioformat.ioformat import IoFormat


class Json( IoFormat ):
	def __init__( self, **options ):
		if 'overwrite' in options: self.complete = options['overwrite']
		super( Json, self ).__init__( **options )



	def write( self, data, **options ):
		"""
			
		"""

		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename

		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if 'filename' in options: filename = options['filename']

		if(debug) : print("DEBUG[WriteJson]: F:%(filename)s" % {'filename': filename})

		if not filename:
			raise RuntimeError("No write file specified")
			

		if( os.path.exists( filename ) and not overwrite ): 
			raise RuntimeError( "File overwrite is refused on existsing file" )

		try:
			fd = open( filename, "w" )
			fd.write( json.dumps( data ) )
			fd.close()
		except Exception as error:
			print("ERROR[WriteJson]: %(error)s" % { 'error': error} )
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

			return json.loads( data )
		except:
			raise

		return None




if( __name__ == '__main__') :
	sys.exit()