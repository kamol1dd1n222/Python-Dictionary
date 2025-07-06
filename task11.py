config = dict()
for i in range(3):
    key  = input(f"{i + 1} - key:"  )
    value  = input(f"{i + 1} - value:"  )
    config.setdefault(key,value)
print(config)    