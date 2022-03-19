import hashlib

def crack_sha1_hash(hash, use_salts = False):
  # Initial values and read data
  y = []  
  with open('top-10000-passwords.txt') as f:
    pContents = f.read().splitlines() 
  with open('known-salts.txt') as f:
    sContents = f.read().splitlines()
    
  # Find the hash values and return value  
  for x in pContents:    
    if (use_salts == True):
      for k in sContents:
        if (hashlib.sha1((k+x).encode("utf-8")).hexdigest() == hash):
          return x
        if (hashlib.sha1((x+k).encode("utf-8")).hexdigest() == hash):
          return x
    else:
      if (hashlib.sha1(x.encode("utf-8")).hexdigest() == hash):
        return x

  return "PASSWORD NOT IN DATABASE"

    