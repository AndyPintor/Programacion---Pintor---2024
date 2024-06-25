
fig = [0, 1]
while True:
    sig = fig[-1] + fig[-2]
    if sig >= 100:
        break
    fig.append(sig)
print(fig)