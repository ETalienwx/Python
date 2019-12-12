__author__ = 'asus'
a={}
a=dict()

a={10:20,"aa":"bb"}
print(a)

#0(1)
a={
    "ip":"127.0.0.1",
    "port":80
}
a["proto"]="tcp"
print(a)
a["port"]=100
print(a)

for key in a:
    print(key,a[key])

a={
    "ip":"127.0.0.1",
    "port":80
}
del(a["ip"])
print(a)
a.clear()
print(a)

a={
    "ip":"127.0.0.1",
    "port":80
}
print("ip" in a)

a={
    "ip":"127.0.0.1",
    "port":80
}
b={
    "port":80,
    "ip":"127.0.0.1"
}
print(a==b)#true
print(len(a))

#hash
print(hash(100))
print(hash("aaa"))
print(hash(()))
#print(hash([]))#cannot hash

a={
    "ip":"127.0.0.1",
    "port":80
}
print(a.keys())#return dict_keys(['ip','port'])
print(a.values())#return dict_values
print(a.items())#return dict_items


