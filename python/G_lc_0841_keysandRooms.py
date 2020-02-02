# -*- coding: utf-8 -*-
"""
841. Keys and Rooms
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # rooms -> outList
        roomNum = len(rooms)
        self._reachableRoom = []
        self._reached = [False for i in range(roomNum)]
        self._rooms = rooms
        self.bfs(0)
        if len(self._reachableRoom) == roomNum:
            return True
        else:
            return False
    def bfs(self, roomInd):
        self._reached[roomInd] = True
        self._reachableRoom.append(roomInd)
        for next_room in self._rooms[roomInd]:
            if not self._reached[next_room]:
                self.bfs(next_room)

rooms = [[1],[2],[3],[]]
#rooms = [[1,3],[3,0,1],[2],[0]]
output = Solution().canVisitAllRooms(rooms)