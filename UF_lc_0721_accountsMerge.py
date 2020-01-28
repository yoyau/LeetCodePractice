# -*- coding: utf-8 -*-
"""
721. Accounts Merge
"""

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
            ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
            ["Mary", "mary@mail.com"]]

r = Solution().accountsMerge(accounts)