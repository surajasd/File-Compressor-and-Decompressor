import zlib, base64

def compress(inputfile,outputfile):
    
    data = open(inputfile ,'r').read()
    
    bytesdata = bytes(data,'utf-8')
    
    compressdata = base64.b64encode(zlib.compress(bytesdata,9))
    decodedata = compressdata.decode('utf-8')
    
    comf = open(outputfile,'w')
    comf.write(decodedata)

def decompress(inputfile,outputfile):
    filecontent = open(inputfile,'r').read()
    
    encodedata = filecontent.encode('utf-8')
    
    decompressdata = zlib.decompress(base64.b64decode(encodedata))
    decodeddata = decompressdata.decode('utf-8')
    
    file = open(outputfile,'w')
    file.write(decodeddata)
    file.close()


    
    
