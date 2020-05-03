import os
import ssl                                        
openssl_dir, openssl_cafile = os.path.split(      
    ssl.get_default_verify_paths().openssl_cafile)
# no content in this folder
os.listdir(openssl_dir)
# non existent file
print(os.path.exists(openssl_cafile))