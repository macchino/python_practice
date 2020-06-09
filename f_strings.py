# f文字列の使い方
# 基本
a = 123
b = "abc"

print("{}and{}".format(a, b))
print("{}and{}".format(b, a))

print("{first}   and{second}".format(first=a, second=b))
print("{second}and{first}".format(second=b, first=a))

# f文字列（f-strings）は文字列リテラルの前にfまたはFを置く（f'xxx', F'xxx'）。
# 文字列中の置換フィールドに変数をそのまま指定できる。

print(f"{a}dna{b}")
print(f"{a}anda{b}")

# 標準の文字列リテラルと同様、シングルクォート'だけでなく
# ダブルクォート"でもトリプルダブルクォート''', """でもOK。
print(f"{a}and{b}")
print(f"""{a} and{b}""")

# 右寄せ、中央寄せ、左寄せ
s = "abc"

print(f"right :{s:_>8}")
print(f"center:{s:^8}")
print(f"left:  {s:_<8}")

# ゼロ埋め
i = 1234

print(f"zero padding:{i:08}")
# 桁区切り
print(f"comma:{i:,}")

# 2進数、8進数、16進数
print(f"bin:{i:b}")
print(f"oct:{i:o}")
print(f"hex:{i:x}")

# 小数点以下の桁数、有効桁（有効数字)
f = 12.3456
print(f"digit(decimal):{f:.3f}")
print(f"digit(all)    :{f:.3g}")

# パーセント表記
print(f"percent:{f:.2%}")

# 波括弧{}の扱い
print(f"{{}}-{f}-{{{f}}}")

# ネストした置換フィールド
n = 123
p = 8

print("{n:0{p}}".format(n=n, p=p))

print(f"{n:0{p}}")

n_1 = 1.23456

for i in range(5):
    print(f"{f:.{i}f}")

# raw文字との組み合わせ
print("x\ty")
print(r"x\ty")

# 文字列リテラルの先頭にrとfを両方つけることで
# raw文字列かつf文字列として処理される。
# rとfの順番はどちらでもよい。大文字でもOK。
x = "xxxx"
y = "yyyy"

print(f"{x}\t{y}")

print(rf"{x}\t{y}")

print(fr"{x}\t{y}")

# f文字列では式を使用可能
# 文字列メソッドformat()では置換フィールド内に式を記述することはできず 、
# エラーKeyErrorになる。
a = 3
b = 4

print(f"{a}+{b}={a+b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b:.2e}")
"""
辞書のキー指定方法
辞書（dict型オブジェクト）を置換フィールドに指定する場合、
文字列メソッドformat()ではキーの指定に引用符', "は不要。
引用符をつけるとエラーになる。
"""
d = {"key_1": 3, "key_2": 4}
print("{0[key_1]},{0[key_2]}".format(d))

"""
f文字列では置換フィールドがそのまま式として評価されるので引用符が必要。
引用符が無いとエラーになる。
"""
print(f'{d["key_1"]},{d["key_2"]}')
