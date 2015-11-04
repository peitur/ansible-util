

def Util:
	
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

