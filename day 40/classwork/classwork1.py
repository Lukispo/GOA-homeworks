def reverse(st):
    ls = []
    ls = st.split()
    ls = ls[::-1]
    return " ".join(ls)
print(reverse("hallo niga"))