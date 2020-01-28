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
        acc_num = len(accounts)
        self._parent = list(range(acc_num))
        self._rank = [0]*acc_num
        
        self._name = []
        self._mail = []
        
        for acc in accounts:
            self._name.append(acc[0])
            self._mail.append(acc[1:])
        
        for i in range(len(self._name)):
            for j in range(i):
                for mail in self._mail[j]:
                    if mail in self._mail[i]: 
                        self.merge(i, j)
                        break
        new_acc = []
        for i, v in enumerate(self._parent):
            if i == v:
                mail = list(set(self._mail[i]))
                mail.sort()
                new_acc.append([self._name[i]]+mail)
        print(self._parent)
        print(self._mail)
        return new_acc
      
    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        print(p_x, p_y)
        if p_y == p_x:
            return
        if self._rank[p_x] == self._rank[p_y]:
            self._rank[p_x] += 1
            self._parent[p_y] = p_x
            self._mail[p_x]+=self._mail[p_y]
        elif self._rank[p_x] > self._rank[p_y]:
            self._parent[p_y] = p_x
            self._mail[p_x]+=self._mail[p_y]
        else:
            self._parent[p_x] = p_y
            self._mail[p_y]+=self._mail[p_x]
accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],
            ["David","David0@m.co"],
            ["David","David1@m.co","David4@m.co","David0@m.co"],
            ["David","David0@m.co","David1@m.co","David3@m.co"],
            ["David","David4@m.co","David1@m.co","David3@m.co"]]

s = Solution()
r = s.accountsMerge(accounts)