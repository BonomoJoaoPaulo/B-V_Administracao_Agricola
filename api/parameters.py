import os

####################
#   DB Parameters  #
####################

def get_db_host():
    return os.getenv('DB_HOST', '172.17.0.1')

def get_db_port():
    return int(os.getenv('DB_PORT', 5433))

def get_db_name():
    return os.getenv('DB_DATABASE', 'projetobd')

def get_db_user():
    return os.getenv('DB_USER', 'postgres')

def get_db_password():
    return os.getenv('DB_PASSWORD', 'password')

