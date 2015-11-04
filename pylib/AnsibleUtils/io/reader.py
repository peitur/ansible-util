
import re, sys, os
import json, yaml

from AnsibleUtils.util import util


class Reader:
	
	def __init__( self, filename, options = {} ):

		self.filename = filename
		self.debug = False
		self.format = None

		print("Reader, options : %(opt)s" % { 'opt': options })


		if 'format' in options: self.format = options['format']
		if 'debug' in options: self.debug = options['debug']

		if not self.format: self.format = util.format_detect( filename )


	def load_yaml( self, options = {} ):
		filename = self.filename		
		if 'filename' in options: filename = options['filename']

		debug = self.debug
		if 'debug' in options: debug = options['debug']

		data = ""
		try:
			fd = open( filename, "r" )
			for line in fd:	
				data += line

			return yaml.load( data )
		except:
			raise

		return None


	def load_json( self, options = {}):
		filename = self.filename
		if 'filename' in options: filename = options['filename']

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

		return None



	def read_file( self, options = {}):
		debug = self.debug
		if 'debug' in options: debug = options['debug']

		filename = self.filename		
		if 'filename' in options: filename = options['filename']


		if( debug ): print("DEBUG: Reader, reading %(format)s file : %(fname)s " % { 'format': self.format, 'fname': filename })

		try:
			
			if( self.format == 'json' ): return self.load_json( )
			elif( self.format == 'yaml' ): return self.load_yaml( )
			else: raise RuntimeError("No format detected")

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

	print("###################################################")
	try:

		r = AnsibleUtils.io.reader.Reader( "../../../playbooks/erlang.json", { 'debug': True } )
	#	r = Reader( "../../playbooks/erlang.json" )

		print("Reader : %(r)s" % { 'r' : r.read_file() })
		if( r ): r.print_info()

	except Exception as error:
		print("ERROR: %(error)s" % {'error': error })

	print("###################################################")

	print("###################################################")
	try:

		r = AnsibleUtils.io.reader.Reader( "../../../playbooks/erlang.yml", { 'debug': True } )
	#	r = Reader( "../../playbooks/erlang.json" )

		print("Reader : %(r)s" % { 'r' : r.read_file() })
		if( r ): r.print_info()

	except Exception as error:
		print("ERROR: %(error)s" % {'error': error })

	print("###################################################")





	sys.exit()