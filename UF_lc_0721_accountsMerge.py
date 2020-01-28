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
        
        for i, p in enumerate(self._parent):
            if i != p:
                self.find(i)
        
        temp = {}
        for i, p in enumerate(self._parent):
            if p in temp:
                temp[p]+= self._mail[i]
            else:
                temp[p] = self._mail[i][:]

        new_acc = []
        for k in temp:
            new_acc.append([self._name[k]]+sorted(set(temp[k])))

        return new_acc
      
    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_y == p_x:
            return
        if self._rank[p_x] == self._rank[p_y]:
            self._rank[p_x] += 1
            self._parent[p_y] = p_x
        elif self._rank[p_x] > self._rank[p_y]:
            self._parent[p_y] = p_x
        else:
            self._parent[p_x] = p_y

            
accounts = [["Lily","Lily3@m.co","Lily4@m.co","Lily17@m.co"],
            ["Lily","Lily5@m.co","Lily3@m.co","Lily23@m.co"],
            ["Lily","Lily0@m.co","Lily1@m.co","Lily8@m.co"],
            ["Lily","Lily14@m.co","Lily23@m.co"],
            ["Lily","Lily4@m.co","Lily5@m.co","Lily20@m.co"],
            ["Lily","Lily1@m.co","Lily2@m.co","Lily11@m.co"],
            ["Lily","Lily2@m.co","Lily0@m.co","Lily14@m.co"]]

s = Solution()
r = s.accountsMerge(accounts)