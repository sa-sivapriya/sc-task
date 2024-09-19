import jwt

def decode_auth_token(auth_token,key):

    try:
        payload = jwt.decode(auth_token,algorithm="HS256", key=key,options={"verify_signature" : False})
        if not payload['admin']:
            raise jwt.InvalidTokenError
        return "success"
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
