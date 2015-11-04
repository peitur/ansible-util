
import re, sys, os
import json, yaml

from AnsibleUtils.util import util


class Reader:
	
	def __init__( self, filename, *options ):

		self.filename = filename
		self.debug = False
		self.format = None


		if 'format' in options: self.format = options['format']
		if 'debug' in options: self.debug = options['debug']

		if( not format ): format_detect( filename )

	def format_detect( filename ):
		if( is_json( filename) ): self.format = 'json'
		elif( is_yaml( filename ) ): self.format = 'yaml'
		else :
			raise RuntimeError("Unknown file format sent to reader: "+filename.__str__() )


	def load_yaml( self, *options ):

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


	def load_json( self, *options ):
		filename = self.filename

		debug = self.debug
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
		debug = self.debug
		if 'debug' in options: debug = options['debug']
		
		filename = self.filename
		try:
			if( self.format == 'json' ): return load_json( )
			elif( self.format == 'yaml' ): return load_yaml( )
		except: 
			raise


	def print_info( self ):
		print("INFO: %(class)s N:%(fname)s D:%(debug)s F:%(format)s" % {'class': __class__ ,'fname': self.filename,'debug': self.debug,'format': self.format} )
		

#################################################################
if( __name__ == '__main__') :
	import builtins
	import AnsibleUtils.io.reader

	sys.path.append( "../../" )
	print( sys.path.__str__() )
	print( dir( Reader ) )

	r = AnsibleUtils.io.reader.Reader( "../../playbooks/erlang.json" )
#	r = Reader( "../../playbooks/erlang.json" )

	print("Reader : %(r)s" % { 'r' : r })
	if( r ): r.print_info()

	sys.exit()