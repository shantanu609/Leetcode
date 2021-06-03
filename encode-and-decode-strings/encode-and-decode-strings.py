class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(self.len_to_String(string) + string.encode('utf-8') for string in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0 
        output = [] 
        while i < len(s):
            length = self.string_to_Int(s[i: i+4])
            i += 4  # actual string 
            output.append(s[i: i + length])
            i += length 
        
        return output
    
    def len_to_String(self, string):
        bytes_ = [chr(len(string) >> (i * 8) & 0xff) for i in range(4)]
        bytes_.reverse()
        bytes_str = ''.join(bytes_)
        return bytes_str
    
    def string_to_Int(self, bytes_str):
        result = 0 
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
