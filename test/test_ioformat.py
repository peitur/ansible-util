
import unittest
import os, sys
sys.path.append( "../pylib")

from  AnsibleUtils.util import util
from AnsibleUtils.ioformat.ioformat import IoFormat

class TestIoFormat( unittest.TestCase ):


	def setUp( self ):
#		self.ok_files  = ["t_data/sample_pb_s0.json","t_data/sample_pb_s0.yml"]
#		self.nok_files = ["t_data/sample_pb_s0.nok.json"]
#		self.missing_files = ["t_data/sample_pb_s0.txt"]
		self.debug = False
		self.supported_formats_json = ["filename1.json","filename3.test.dots.json"]
		self.supported_formats_yaml = ["filename2.yml","filename4.test.dots.yml"]
		
		self.unsupported_formats = ["filename1.txt","filename3.test.dots.txt","filename3.test.dots.abc"]
 

	def tearDown( self ):
		pass

	def test_ok_format_check( self ):
		## Badly formated file content
		for f in self.supported_formats_yaml+self.supported_formats_json:
			IoFormat( debug=self.debug, filename=f )

	def test_ok_format_json( self ):
		## Badly formated file content
		for f in self.supported_formats_json:
			self.assertEqual( IoFormat( debug=self.debug, filename=f ).get_format() , "json" )

	def test_ok_format_yaml( self ):
		## Badly formated file content
		for f in self.supported_formats_yaml:
			self.assertEqual( IoFormat( debug=self.debug, filename=f ).get_format(), "yaml" )



	def test_bad_format_file( self ):
		## Badly formated file content
		for f in self.unsupported_formats:
			with self.assertRaises( RuntimeError ):
				IoFormat( debug=self.debug, filename=f )

	def test_missing_format_file( self ):
		## Badly formated file content
		with self.assertRaises( RuntimeError ):
			IoFormat( debug=self.debug )




if __name__ == "__main__":
	unittest.main()

