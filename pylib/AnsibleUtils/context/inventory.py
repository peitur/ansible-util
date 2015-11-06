
import AnsibleUtils.admin
import AnsibleUtils.util
import AnsibleUtils.io
import AnsibleUtils.ioformat




INVOPTIONS= { 	"ansible_ssh_host": None,
				"ansible_ssh_port": None, 
				"ansible_ssh_user": None,
				"ansible_ssh_pass": None,
				"ansible_connection": None,
				"ansible_ssh_private_key_file": None,
				"ansible_shell_type": None,
				"ansible_python_interpreter" : None
			}

INVINTERPRET = r"ansible_.+_interpreter"
INTERPRETERS = []



class AnsibleInventory:

	## options:
	##  - debug: 		Enable debugging, including all subclasses
	##  - filename:		Operate on filename, read
	##  - content:		Data content
	##  - auto_read:  	Auto read the filename
	def __init__( self, options = {} ):

		self.auto_read = False
		self.filename = None
		self.content = None
		self.debug = False
		self.format = "inventory"

		if 'debug' in options: self.debug = options['debug']
		if 'filename' in options: self.filename = options['filename']
		if 'content' in options: self.content = options['content']
		if 'auto_read' in options: self.auto_read = True


		## Filename selected and not data has been sent to contructor, assuming that the filename will be used for write later
		if self.auto_read and self.filename:
			try:

				robj = AnsibleUtils.io.reader.Reader( self.filename, { 'debug': self.debug, 'format': self.format } )
				self.content = robj.read_file( )

			except RuntimeError as error:
				print("ERROR: Could not read nventory file %(fname)s : %(error)s" % { 'fname': self.filename ,'error': error } )




if( __name__ = '__main__' ):
	sys.exit()