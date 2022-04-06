#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Deque:

    def __init__(self):
        self.queue = []
        self.count = 0
        
    def __repr__(self):
        return self.queue.__repr__()

    def push_front(self, key):                       # push_front adds a key to the head of the deque
        if self.count == 0:
            self.queue = [key,]
            self.count = 1
            return str("ok")
         
        self.queue.insert(0, key)
        self.count += 1
        return str("ok")

    def push_back(self, key):                         # push_back adds a key to the tail of the deque
        if self.count == 0:
            self.queue = [key,]
            self.count = 1
            return str("ok")
         
        self.queue.append(key)
        self.count += 1
        return str("ok")

    def pop_front(self):                             # pop_front extracts a key from the head of the deque and returns it
        if self.count == 0:
            return str("error")
        x = self.queue.pop(0)
        self.count -= 1
        return x

    def pop_back(self):                             # pop_back extracts a key from the tail of the deque and returns it
        if self.count == 0:
            return str("error")
        x = self.queue.pop()
        self.count -= 1
        return x

    def front(self):                               # front returns head element without removing it
        if self.count == 0:
            return str("error")
        return self.queue[0]

    def back(self):                               # back returns tail element without removing it
        if self.count == 0:
            return str("error")
        return self.queue[-1]

    def clear(self):                             # clear removes all elements from the deque
        self.queue.clear()
        self.count = 0
        return str("ok")

    def size(self):                              # size returns number of the elements in the deque
        return self.count 

def process_deque(commands):
    result = [] 
    s = Deque()
    for command in commands:
        if command.startswith('push_front'):
            command = command.split(' ')
            result.append(s.push_front(int(command[1])))
        elif command.startswith('push_back'):
            command = command.split(' ')
            result.append(s.push_back(int(command[1])))
        elif command.startswith('front'):
            result.append(s.front())
        elif command.startswith('back'):
            result.append(s.back())
        elif command.startswith('clear'):
            result.append(s.clear())
        elif command.startswith('size'):
            result.append(s.size())
        elif command == "pop_front":
            result.append(s.pop_front())
        elif command == ("pop_back"):
            result.append(s.pop_back())
        
        
    return result

if __name__ == "__main__":        

    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    
    print(process_deque(test_cmd))
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    #print(process_deque(test_cmd))

    test_cmd = ["pop_back", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    
    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))

