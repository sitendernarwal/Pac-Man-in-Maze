# I have changed something in forked repo.
# main branch me change kiya 
class Stack:
    def __init__(self) -> None:
        self._array = []

    def push(self, x) -> None:
        self._array.append(x)

    def is_Empty(self) -> bool:
        return len(self._array) == 0

    def __len__(self) -> int:
        return len(self._array)

    def pop(self):
        if self.is_Empty():
            return None
        else:
            return self._array.pop()

    def top(self):
        if self.is_Empty():
            return None
        else:
            return self._array[-1]


