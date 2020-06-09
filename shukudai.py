# member = ["tanaka", "tadokoro", "tajima", "tahata", "takahashi", "takeda"]


# for t, i in enumerate(member, 1):
#   print(t, i)


errmsg = "エラーです"
errnmu = 52809
print(errmsg + str(errnmu))

print(f"{errmsg:_>12}")
print(f"center:{errmsg:_^12}")
print(f"left:{errmsg:_<12}")
print(f"{errnmu:09}")

f = 0.123
print(f"percあいうえおent:{f:.2%}")
