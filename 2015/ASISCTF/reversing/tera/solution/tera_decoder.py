#!/usr/bin/python
#
# ASIS CTF Quals 2015
# tera (REVERSING/100)
#
# @a: Smoke Leet Everyday
# @u: https://github.com/smokeleeteveryday
#

from struct import unpack
import urllib2

# Fetch single byte from URL using content range
def get_buffer_byte(url, offset):
  req = urllib2.Request(url)
  req.headers['Range'] = 'bytes=%s-%s' % (offset, offset)
  f = urllib2.urlopen(req)
  return f.read()

# Decryption functionality
def decrypt(url, index_table, key_table):
	plaintext = ""
	for m in xrange(0, 38):
		i = unpack('<Q', index_table[m*8: (m+1)*8])[0]
		b = get_buffer_byte(url, i)
		k = unpack('<I', key_table[m*4: (m+1)*4])[0]
		plaintext += chr(ord(b) ^ k)
	return plaintext

# Target URL
url = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000"

# Key and indexing tables
key_table = "\xF2\x00\x00\x00\x9A\x00\x00\x00\x83\x00\x00\x00\x12\x00\x00\x00\x39\x00\x00\x00\x45\x00\x00\x00\xE7\x00\x00\x00\xF4\x00\x00\x00\x6F\x00\x00\x00\xA1\x00\x00\x00\x06\x00\x00\x00\xE7\x00\x00\x00\x95\x00\x00\x00\xF3\x00\x00\x00\x90\x00\x00\x00\xF2\x00\x00\x00\xF0\x00\x00\x00\x6B\x00\x00\x00\x33\x00\x00\x00\xE3\x00\x00\x00\xA8\x00\x00\x00\x78\x00\x00\x00\x37\x00\x00\x00\xD5\x00\x00\x00\x44\x00\x00\x00\x39\x00\x00\x00\x61\x00\x00\x00\x8A\x00\x00\x00\xFB\x00\x00\x00\x22\x00\x00\x00\xFA\x00\x00\x00\x9E\x00\x00\x00\xE7\x00\x00\x00\x11\x00\x00\x00\x39\x00\x00\x00\xA6\x00\x00\x00\xF3\x00\x00\x00\x33\x00\x00\x00\x00\x00\x00\x00\x00\x00\x59\x40"
index_table = "\xF4\x7C\x61\x89\x4C\x00\x00\x00\x83\x5F\xE9\xB5\xB4\x00\x00\x00\x6B\x68\x8D\x59\xE4\x00\x00\x00\xEF\x74\x26\xA6\x36\x01\x00\x00\xB7\xBE\x65\x7A\x83\x01\x00\x00\x7C\x46\x31\xA8\x9F\x01\x00\x00\x01\xCD\x2A\x20\xA6\x02\x00\x00\x5E\x64\x10\x3F\x49\x04\x00\x00\xE4\x65\x6D\xCE\xCD\x04\x00\x00\x7E\xDE\xC8\x8E\x02\x05\x00\x00\x56\x4A\x50\x19\x62\x05\x00\x00\xB8\x1D\x19\x2D\xBD\x05\x00\x00\x92\x25\xD0\xD5\x2B\x07\x00\x00\xFE\x04\x6D\xEE\x3D\x07\x00\x00\x20\xE3\xAF\xE5\x25\x0A\x00\x00\x9E\xFB\x64\xB4\x73\x0A\x00\x00\x4B\xE3\xF6\x59\x62\x0B\x00\x00\xDC\x94\x50\xA4\x9A\x0B\x00\x00\x39\xEA\xE0\x48\xC5\x0B\x00\x00\x56\xCC\x1E\xC4\x7A\x0C\x00\x00\x8B\xFB\x73\xF0\x85\x0C\x00\x00\x16\x91\x6A\x53\x92\x0C\x00\x00\xBF\xDA\xE6\x0B\x93\x0D\x00\x00\x40\xDA\x89\xB9\x61\x0E\x00\x00\x68\xA2\x9C\x99\x37\x0F\x00\x00\x1F\x9D\x9B\xC5\xB7\x0F\x00\x00\x9D\x93\xA3\xD3\x18\x10\x00\x00\x69\x03\xED\x2A\x20\x10\x00\x00\xF3\x6C\x92\xFB\xE8\x10\x00\x00\x65\xA0\x8E\xC3\x3B\x11\x00\x00\x4F\x04\x04\x75\x25\x13\x00\x00\x3C\xDC\x12\x06\xFB\x14\x00\x00\x92\xDA\x70\x23\x57\x16\x00\x00\x41\x44\x63\x75\x3D\x17\x00\x00\x74\x93\x2D\x0F\x9D\x1B\x00\x00\x8E\x2D\xE4\x0D\xA9\x1B\x00\x00\x3E\x8F\x4C\xEF\xE9\x1B\x00\x00\x00\x4E\xB8\xA4\xFD\x1B\x00\x00"

print "[+]Got flag: [%s]" % decrypt(url, index_table, key_table)