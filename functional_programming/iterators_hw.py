class CharIterator:

    def __iter__(self):
        return self

    def __init__(self, first_char, last_char):
        self.first_char = ord(first_char)
        self.last_char = ord(last_char)
        self.counter = ord(first_char) - 1

    def __next__(self):
        if self.counter < self.last_char:
            self.counter += 1
            return chr(self.counter)
        else:
            raise StopIteration


char_iterator = CharIterator('a', 'z')

for i in char_iterator:
    print(i)
