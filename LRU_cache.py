class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.oldest=Node(0,0)
        self.latest=Node(0,0)
        self.latest.prev=self.oldest
        self.oldest.next=self.latest
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def remove(self,node):
        prev,next=node.prev,node.next
        prev.next=next
        next.prev=prev
    def insert(self,node):
        prev,next=self.latest.prev,self.latest
        prev.next=next.prev=node
        node.prev=prev
        node.next=next

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.oldest.next
            self.remove(lru)
            del self.cache[lru.key] 