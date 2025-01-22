#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (65.61%)
# Likes:    5205
# Dislikes: 477
# Total Accepted:    633.7K
# Total Submissions: 965.6K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If
# the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or
# -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.
#
#
#
# Example 1:
#
#
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
#
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1],
# [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the
# existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now
# [[1,1]]
#
#
#
# Constraints:
#
#
# 0 <= key, value <= 10^6
# At most 10^4 calls will be made to put, get, and remove.
#
#
#

# @lc code=start
class MyHashMap:
    def __init__(self) -> None:
        self.k = 10**4
        self.container: list[list[tuple[int, int]] | None] = [None] * self.k

    def _slot(self, key: int) -> int:
        return key % self.k

    def put(self, key: int, value: int) -> None:
        slot = self._slot(key)
        chain = self.container[slot]
        if chain is None:
            self.container[slot] = [(key, value)]
        else:
            for entry in chain:
                if entry[0] == key:
                    chain.remove(entry)
            chain.append((key, value))

    def get(self, key: int) -> int:
        slot = self._slot(key)
        chain = self.container[slot]
        if chain is None:
            return -1
        for entry in chain:
            if entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key: int) -> None:
        slot = self._slot(key)
        chain = self.container[slot]
        if chain is None:
            return
        for i, entry in enumerate(chain):
            if entry[0] == key:
                chain.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
