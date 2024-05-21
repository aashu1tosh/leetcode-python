s ="the sky is blue"
c = s.split()
c.reverse()
a = " ".join(c)
print(a)

# this works even better
# " ".join(s.split())