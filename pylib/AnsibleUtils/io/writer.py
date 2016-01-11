
import re, sys, os, getopt
import json, yaml
from pprint import pprint

from AnsibleUtils.util import util
import AnsibleUtils.ioformat.json
import AnsibleUtils.ioformat.yaml


##########################################################
## 
##########################################################
class Writer:
	"""

	"""

	def __init__( self, filename = None, **options ):
		"""
			
		"""

		self.filename = filename
		self.overwrite = True
		self.debug = False
		self.format = None

#		if not self.format and self.filename: self.format = util.format_detect( self.filename )

		if 'format' in options: self.format = options['format']
		if 'debug' in options: self.debug = options['debug']
		if 'overwrite' in options: self.complete = options['overwrite']


##########################################################
## 
##########################################################
	def __write_inventory_file__( self, data, **options ):
		"""
			
		"""

		pass

	def __write_yaml_file__( self, data, **options ):
		
		if self.filename: 
			options['filename'] = self.filename
		else :
			raise RuntimeError("[WriteYaml]ERROR: Missing Filename")

		if self.debug: options['debug'] = self.debug
		if self.format: options['format'] = self.format
		if self.overwrite: options['overwrite'] = self.overwrite
		return AnsibleUtils.ioformat.yaml.Yaml( **options ).write( data )
 

	def __write_json_file__( self, data, **options ):

		if self.filename: 
			options['filename'] = self.filename
		else :
			raise RuntimeError("[WriteYaml]ERROR: Missing Filename")

		if self.debug: options['debug'] = self.debug
		if self.format: options['format'] = self.format
		if self.overwrite: options['overwrite'] = self.overwrite
		return AnsibleUtils.ioformat.json.Json( **options ).write( data )


##########################################################
## 
##########################################################
	def write_file( self, data, **options ):
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

		if not format and filename: format = util.format_detect( filename )
		
		if(debug) : print("DEBUG[WriteFile]: File:%(filename)s D:%(debug)s O:%(overwrite)s F:%(format)s" % {'filename': filename, 'debug':debug, 'overwrite':overwrite, 'format':format})

		if not filename:
			raise RuntimeError("No write file specified")

		if( format == 'yaml') : 
			return self.__write_yaml_file__( data )
		elif( format == 'json' ):
			return self.__write_json_file__( data )
		elif( format == 'inventory' ):
			return self.__write_inventory_file__( data )
		else:
			print("ERROR: Unknown file format : %(format)s " % { 'format': format } )
			raise RuntimeError("Unknown file format")

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



##########################################################
## 
##########################################################
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
