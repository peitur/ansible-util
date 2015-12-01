
import unittest
import os, sys
sys.path.append( "../pylib")


from AnsibleUtils.util import util


class TestUtils(unittest.TestCase):


	def setUp( self ):
		self.ok_yaml = "file.yml"
		self.ok_json = "file.json"
		self.nok     = "file1.txt"

	def tearDown( self ):
		pass


	def test_is_yaml( self ):
		self.assertTrue( util.is_yaml( self.ok_yaml ) )
		self.assertFalse( util.is_yaml( self.nok ) )

	def test_is_yaml( self ):
		self.assertTrue( util.is_json( self.ok_json ) )
		self.assertFalse( util.is_json( self.nok ) )

	def test_detect_type( self ):
		self.assertEqual( util.format_detect( self.ok_yaml ), "yaml" )
		self.assertEqual( util.format_detect( self.ok_json ), "json" )

		with self.assertRaises( Exception ):
			util.format_detect( self.nok )



if __name__ == "__main__":
	print( ",".join( sys.path ) )
	#unittest.main()