class TrieNode(object):
    def __init__(self):
        # key=char, value=TrieNode
        self.link = {}
        # used in searching to avoid False result
        self.end = False

    def __str__(self):
        return 'link - {},  end={}'.format(self.link, self.end)

    def insert(self, s):
        node = self
        for c in s:
            if c not in node.link:
                node.link[c] = TrieNode()
            node = node.link[c]
        node.end = True

    def search(self, s):
        node = self
        for c in s:
            if c in node.link:
                node = node.link[c]
            else:
                return False
        return node.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            if c in node.link:
                node = node.link[c]
            else:
                return False
        return True
words = ['sea', 'seen', 'saw', 'scene', 'tarun']
search_words = ['see', 'sei', 'sean', 'saw', 'scene', 'scenery']
prefix = ['se', 'tar']
t = TrieNode()
for w in words:
    print('inserting {}'.format(w))
    t.insert(w)
print(t)
for w in search_words:
    print('word={}, present={}'.format(w, t.search(w)))
for w in prefix:
    print('prefix={}, present={}'.format(w, t.startsWith(w)))
