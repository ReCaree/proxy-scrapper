import hashlib

#
# https://www.codevscolor.com/python-remove-duplicate-lines-text-file
#

def http_remove_duplicates():
  completed_lines_hash = set()

  out = open("proxy/http-removed.txt", "w")

  for line in open("proxy/http.txt", "r"):
    hash = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()

    if hash not in completed_lines_hash:
      out.write(line)
      completed_lines_hash.add(hash)

  out.close()

def socks4_remove_duplicates():
  completed_lines_hash = set()

  out = open("proxy/socks4-removed.txt", "w")

  for line in open("proxy/socks4.txt", "r"):
    hash = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()

    if hash not in completed_lines_hash:
      out.write(line)
      completed_lines_hash.add(hash)

  out.close()

def socks5_remove_duplicates():
  completed_lines_hash = set()

  out = open("proxy/socks5-removed.txt", "w")

  for line in open("proxy/socks5.txt", "r"):
    hash = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()

    if hash not in completed_lines_hash:
      out.write(line)
      completed_lines_hash.add(hash)

  out.close()