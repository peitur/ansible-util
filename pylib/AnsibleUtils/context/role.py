
import AnsibleUtils.admin
import AnsibleUtils.util
import AnsibleUtils.io
import AnsibleUtils.ioformat

from pprint import pprint

##########################################################
## 
##########################################################

DEFAULT_MAINFILE="main"
DEFAULT_FILETYPE="yml"
DEFAULT_TYPE = "yaml"

ROLEPARTS = { "vars":"dict",
			  "defaults":"dict",
			  "tasks":"list",
			  "files":None,
			  "templates":None,
			  "meta":"dict",
			  "handlers":"list"
			}

##########################################################
## 
##########################################################
class AnsibleRole:
"""

"""

	def __init__( self, rolename, options = {} ):
		"""
			
		"""

		self.name = rolename
		self.debug = False
		self.format = DEFAULT_TYPE
		self.type = "role"
		self.content = {}

		for d in ROLEPARTS:
			self.content[d] = 


		if 'debug' in options: self.debug = options['debug']
		if 'format' in options: self.content = options['format']


		pass



	def load( self, newfilename = None ):
		"""
			
		"""

		filename = self.filename
		if newfilename:
			filename = newfilename

		if not filename:
			raise RuntimeError("ERROR: No file specified for playbook parser ")

		if self.debug: print("DEBUG: Parsing file %(fname)s " % { 'fname': filename })




		return self.content

##########################################################
## 
##########################################################
if( _name_ == '__main__') :
	sys.exit()