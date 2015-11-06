
import AnsibleUtil.admin
import AnsibleUtil.util
import AnsibleUtil.io
import AnsibleUtil.ioformat


PLAYPARTS = ['vars','tasks','handlers','main','']

class AnsiblePlaybook:

	def __init__( self, filenmae, options = {} ):

		self.auto_read = False
		self.filename = None
		self.content = None
		self.debug = False
		self.format = "playbook"

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
				print("ERROR: Could not read  file %(fname)s : %(error)s" % { 'fname': self.filename ,'error': error } )






		



if( _name_ == '__main__') :
	sys.exit()