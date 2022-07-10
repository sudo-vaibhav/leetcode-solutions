class Solution:
    def validIPAddress(self, ip: str) -> str:
        
#         ipv4 check
        
        if ip.count(".")==3:
            chunks = ip.split(".")
            if len(chunks)==4: 
                for chunk in chunks:
                    try:
                        if (len(chunk)>1 and chunk[0]=="0") or int(chunk)>255:
                            break
                    except:
                        break
                else:
                    return "IPv4"
        
#        ipv6 check
        if ip.count(":")==7:
            chunks = ip.split(":")
            if len(chunks)==8:
                for chunk in chunks:
                    if 1<=len(chunk)<=4:
                        invalid = False
                        for c in chunk:
                            if not (c.isdigit() or ord("a")<=ord(c.lower())<=ord("f")):
                                invalid = True
                                break
                        if invalid:
                            break
                    else:
                        break
                else:
                    return "IPv6"
    


        return "Neither"
            