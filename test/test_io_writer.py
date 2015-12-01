

import unittest
import os, sys, shutil
sys.path.append( "../pylib")

from  AnsibleUtils.util import util
from AnsibleUtils.io.reader import Reader
from AnsibleUtils.io.writer import Writer


class TestIoReader(unittest.TestCase):


	def setUp( self ):
		self.cleanup_test = True
		self.debug = False
		self.read_files  = ["t_data/sample_pb_s2.json","t_data/sample_pb_s2.yml"]
		self.read_missing_files = ["t_data/bad.txt"]
		self.read_nok_files = []

		self.target_dir = "t_result"
		self.target_files = [self.target_dir+"/wtest.json",self.target_dir+"/wtest.yml"]
		if not os.path.exists( self.target_dir ):
			os.mkdir( self.target_dir )

	def tearDown( self ):
		if not self.cleanup_test: pass

		shutil.rmtree( self.target_dir )

	def test_write_files( self ):
		## Ok files
		for f in self.read_files:
			r = Reader( f, { 'debug':self.debug } ).read_file()

			for x in self.target_files:
				self.assertIsNotNone( Writer( x, { 'debug':self.debug } ).write_file( r ) )
				self.assertIsNotNone( Reader( x, { 'debug':self.debug } ).read_file() )



if __name__ == "__main__":
	unittest.main()