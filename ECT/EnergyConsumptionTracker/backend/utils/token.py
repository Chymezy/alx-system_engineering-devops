from flask_jwt_extended import create_access_token

# Importance: Handles JWT token creation.
def generate_token(user_id):
    # Create JWT token for given user ID
    return create_access_token(identity=user_id)

