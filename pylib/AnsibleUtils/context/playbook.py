
import sys, os, re

sys.path.append( "/Users/peter/Vagrant/ansible-util/pylib" )

from pprint import pprint
import AnsibleUtils.admin
import AnsibleUtils.util
import AnsibleUtils.io.reader
import AnsibleUtils.io.writer
import AnsibleUtils.ioformat

##########################################################
## 
##########################################################

PLAYPARTS = ['vars','tasks','handlers']

class AnsiblePlaybook:
"""

"""


##########################################################
## 
##########################################################

	def __init__( self, playname, options = {} ):
		"""
			
		"""

		self.name = playname
		self.auto_read = False
		self.filename = None
		self.content = []
		self.main = []
		self.debug = False
		self.format = None
		self.type = "playbook"

		if 'debug' in options: self.debug = options['debug']
		if 'filename' in options: self.filename = options['filename']
		if 'content' in options: self.content = options['content']
		if 'auto_read' in options: self.auto_read = True
		if 'format' in options: self.content = options['format']


		## Filename selected and not data has been sent to contructor, assuming that the filename will be used for write later
		if self.auto_read and self.filename:
			try:

				if self.filename: 
					self.load( self.filename )
				else:
					print("[AnsiblePlaybook]ERROR: Filename has not been set in Playbook Context" )				

			except RuntimeError as error:
				pprint("[AnsiblePlaybook]ERROR: Could not read  file %(fname)s : %(error)s" % { 'fname': self.filename ,'error': error } )
				raise


##########################################################
## 
##########################################################


	def content( self, newcontent = None ):
		if newcontent : self.content = newcontent
		return self.content

	def main( self, newcontent = None ):
		if newcontent : self.main = newcontent
		return self.main



	def load( self, newfilename = None ):
		"""

		"""

		filename = self.filename
		if newfilename:
			filename = newfilename

		if not filename:
			raise RuntimeError("[AnsiblePlaybook.load]ERROR: No file specified for playbook parser ")

		if self.debug: print("[AnsiblePlaybook.load]DEBUG: Parsing file %(fname)s " % { 'fname': filename })

		try:

			robj = AnsibleUtils.io.reader.Reader( filename, { 'debug': self.debug, 'type': self.type } )
			data = content = robj.read_file( )

			content = []
			main = []
			for x in data:		
				for y in x:
#					if self.debug: print("[AnsiblePlaybook.load]DEBUG: Read : %(data)s" % { 'data': y } )
					if y in PLAYPARTS: 
						self.content.append( { y : x[y] } )
					else:
						self.main.append( { y : x[y] } )

		except:
			raise

		return { 'main': self.main, 'content': self.content }


##########################################################
## 
##########################################################
	def __str__(self):
		return ""+"debug:"+self.debug.__str__()+" filename:"+self.filename.__str__()+" auto_read:"+self.auto_read.__str__()+" content: "+self.content.__str__()




##########################################################
if( __name__ == '__main__' ):

	import AnsibleUtils.context.playbook

	print("###################################################")
	try:

		r = AnsibleUtils.context.playbook.AnsiblePlaybook( "erlang", {'filename':"../../../playbooks/erlang.json", 'debug' : True, 'auto_read':True} )
		pprint("INFO: %(info)s" % {'info': r} )

	except Exception as error:
		print("ERROR: %(error)s" % { 'error': error })
		raise

	print("###################################################")




	sys.exit()