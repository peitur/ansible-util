

import AnsibleUtils.admin
import AnsibleUtils.util
import AnsibleUtils.io
import AnsibleUtils.ioformat


class Creator:

	def __init__( self, options = {} ):
		
		self.debug = False
		self.data = {}

		

	



	def getCreator( type, options = {} ):

		if( type == 'playbook' ):
			return AnsibleUtils.admin.playbookcreator.PlaybookCreator( options )
		elif( type == 'role' ):
			return AnsibleUtils.admin.rolecreator.RoleCreator( options )
		else: 
			raise



if( __name__ == '__main__') :
	sys.exit()