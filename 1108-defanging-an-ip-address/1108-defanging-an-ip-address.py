class Solution:
    def defangIPaddr(self, address: str) -> str:
        an = address.replace(".","[.]")
        return an
       

        