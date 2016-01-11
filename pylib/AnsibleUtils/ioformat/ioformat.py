import re, sys, os
import json, yaml

from AnsibleUtils.util import util

"""

"""
class IoFormat:
	def __init__( self, **options ):
		self.debug = None
		if( 'debug' in options and options['debug']  ): self.debug = True


		if( self.debug ): print("[IoFormat]DEBUG: Input options: %(options)s" % { 'options':options } )

		self.format = None
		self.filename = None
		self.overwrite = True

		if( 'format' in options ): self.format = options['format']
		if( 'filename' in options ): self.filename = options['filename']

		if( self.debug ): print("[IoFormat.1]DEBUG: Input format: %(format)s Filename: %(filename)s" % { 'format':self.format, 'filename':self.filename } )
		

		if not self.filename and not self.format:
			raise RuntimeError("Can't detect format, missing information")

		if self.filename and not self.format:
			self.format = util.format_detect( self.filename )

		if( self.debug ): print("[IoFormat.2]DEBUG: Input format: %(format)s Filename: %(filename)s" % { 'format':self.format, 'filename':self.filename } )

		if not self.format: raise RuntimeError("No format available")


	################################################################

	def get_format( self ):
		return self.format

	def read( self, **options ):
		pass

	def write( self, data, **options ):
		pass




if( __name__ == '__main__') :
	sys.exit()	