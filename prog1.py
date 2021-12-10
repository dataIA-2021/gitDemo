import myClass as mc

i=10

url_fichier = "data.csv"

x = mc.myObject(url_fichier)

print('x={}, i={}, url={}'.format(x, i, x.url))

print('ok')

x.test()
x.stat()

