import re

def is_yaml( filename ):
	if( re.match( r".+\.yml$", filename ) ):
		return True
	return False

def is_json( filename ):
	if( re.match( r".+\.json$", filename ) ):
		return True
	return False

def is_template( filename ):
	if( re.match( r".+\.j2$", filename ) ):
		return True
	return False


def format_detect( filename ):
	if( is_json( filename ) ): return 'json'
	elif( is_yaml( filename ) ): return 'yaml'
	else :
		raise RuntimeError("Unknown file format sent to reader: "+filename.__str__() )



if( __name__ == '__main__') :
	sys.exit()