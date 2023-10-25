def pyramid(h):
    for i in range(h):
        print(" "*(h-i-1)+"#"*(2*i+1))
pyramid(8)
