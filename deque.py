class Deque:

    def __init__(self):
        pass

    def push_front(self, key):
        pass

    def push_back(self, key):
        pass

    def pop_front(self):
        pass

    def pop_back(self):
        pass

    def front(self):
        pass

    def back(self):
        pass

    def clear(self):
        pass

    def size(self):
        pass


def process_deque(commands):
    pass


if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))