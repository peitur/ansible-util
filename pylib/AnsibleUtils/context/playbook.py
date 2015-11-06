
import AnsibleUtil.admin
import AnsibleUtil.util
import AnsibleUtil.io
import AnsibleUtil.ioformat


PLAYPARTS = ['vars','tasks','handlers','main','']

class AnsiblePlaybook:

	def __init__( self, filenmae, options = {} ):

		self.filename = filename
		self.debug = False
		self.format = "inventory"

		if 'debug' in options: self.debug = options['debug']


		
		pass





if( _name_ == '__main__') :
	sys.exit()