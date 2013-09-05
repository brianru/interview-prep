def swap (x, y, s):
    return ''.join([y if c == x else c for c in s.strip()])

print swap(' ', '%20', "hi brian")
