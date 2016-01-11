

import unittest
import os, sys
sys.path.append( "../pylib")

from  AnsibleUtils.util import util
from AnsibleUtils.io.reader import Reader


class TestIoReader(unittest.TestCase):


	def setUp( self ):
		self.ok_files  = ["t_data/sample_pb_s0.json","t_data/sample_pb_s0.yml"]
		self.nok_files = ["t_data/sample_pb_s0.nok.json"]
		self.missing_files = ["t_data/sample_pb_s0.txt"]



	def tearDown( self ):
		pass


	def test_read_files( self ):
		## Ok files
		for f in self.ok_files:
			self.assertIsNotNone( Reader( f ).read_file( ) )

	def test_bad_format_file( self ):
		## Badly formated file content
		for f in self.nok_files:
			with self.assertRaises( Exception ):
				Reader( f ).read_file()

	def test_missing_file( self ):
		## Missing the file
		for f in self.missing_files:
			with self.assertRaises( Exception ):
				Reader( f ).read_file()


if __name__ == "__main__":
	unittest.main()