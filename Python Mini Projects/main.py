def truncatesentence(s,k):
        arr = s.split()
        return " ".join(arr[:k])


s = "Hello how are you"
k = 4
print(truncatesentence(s,k))