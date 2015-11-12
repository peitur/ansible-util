
import re, sys, os, getopt
import json, yaml
from pprint import pprint

from AnsibleUtils.util import util

class Writer:

	def __init__( self, filename = None, options = {} ):
		"""
			
		"""

		self.filename = filename
		self.overwrite = True
		self.debug = False
		self.format = None

		if 'format' in options: self.format = options['format']
		if 'debug' in options: self.debug = options['debug']
		if 'overwrite' in options: self.complete = options['overwrite']


	def __write_inventory_file__( self, data, options = {} ):
		"""
			
		"""

		pass

	def __write_yaml_file__( self, data, options = {} ):
		"""
			
		"""

		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename


		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if 'filename' in options: filename = options['filename']

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


	def __write_json_file__( self, data, options = {} ):
		"""
			
		"""

		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename

		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if 'filename' in options: filename = options['filename']

		if(debug) : print("DEBUG[WriteJson]: F:%(filename)s" % {'filename': filename})

		if( os.path.exists( filename ) and not overwrite ): return None

		try:
			fd = open( filename, "w" )
			fd.write( json.dumps( data ) )
			fd.close()
		except Exception as error:
			print("ERROR[WriteJson]: %(error)s" & {error} )
			raise
			
		return True

	def write_file( self, data, options = {} ):
		"""
			
		"""

		format = self.format
		debug = self.debug
		overwrite = self.overwrite
		filename = self.filename

		if 'debug' in options: debug = options['debug']
		if 'overwrite' in options: complete = options['overwrite']
		if 'format' in options: format = options['format']
		if 'filename' in options: filename = options['filename']

		if not self.format: self.format = util.format_detect( filename )



		if(debug) : print("DEBUG[WriteFile]: File:%(filename)s D:%(debug)s O:%(overwrite)s F:%(format)s" % {'filename': filename, 'debug':debug, 'overwrite':overwrite, 'format':format})

		if( format == 'yaml') : 
			return self.__write_yaml_file__( data )
		elif( format == 'json' ):
			return self.__write_json_file__( data )
		elif( format == 'inventory' ):
			return self.__write_inventory_file__( data )
		else:
			print("ERROR: Unknown file format : %(format)s " % { 'format': format } )

		return None


	def format( self, f = None ):
		if f:
			self.format = f
		return self.format


	def filename( self, f = None ):
		if f:
			self.filename = f
		return self.filename


	def print_info( self ):
		print("INFO: %(class)s N:%(fname)s D:%(debug)s F:%(format)s" % {'class': __class__ ,'fname': self.filename,'debug': self.debug,'format': self.format} )



#################################################################
if( __name__ == '__main__'):
	import builtins
	import AnsibleUtils.io.writer

	sys.path.append( "../../" )
	print( sys.path.__str__() )

	print("###################################################")
	try:

		r = AnsibleUtils.io.writer.Writer( "../../../test.json", { 'debug': True } )
	#	r = Reader( "../../playbooks/erlang.json" )

		print("Writer : %(r)s" % { 'r' : r.write_file( {"test":True, "good":[1,2,3]} ) } )
		if( r ): r.print_info()

	except Exception as error:
		print("ERROR: %(error)s" % {'error': error })

	print("###################################################")

	print("###################################################")
	try:

		r = AnsibleUtils.io.writer.Writer( "../../../test.yml", { 'debug': True } )
	#	r = Reader( "../../playbooks/erlang.json" )

		print("Writer : %(r)s" % { 'r' : r.write_file( {"test":True, "good":[1,2,3]} ) } )
		if( r ): r.print_info()

	except Exception as error:
		print("ERROR: %(error)s" % {'error': error })

	print("###################################################")


	sys.exit()
