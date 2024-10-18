#inisiasi matriks
a = [[6,2,7],[9,5,6],[7,9,9]]
b = [[5,6,7],[7,3,9],[4,1,7]]
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
#menentukan ukuran matriks
baris_a = len(a)
kolom_a = len(a[0])

baris_b = len(b)
kolom_b = len(b[0])
#menampilkan matriks 
print (a)
print ("baris matriks a adalah ", baris_a)
print ("kolom matriks a adalah ", kolom_a)

print (b)
print ("baris matriks b adalah ", baris_b)
print ("kolom metriks b adalah ", kolom_b)
#memeriksa kelayakan perkalian matriks
if (kolom_a !=baris_b):
    print ("martriks a dan b tidak dapat dikalikan")
else:
    print("martiks a dan b dapat dikalikan")
#perkalian matriks
    c = (a[0][0]*b[0][0])+(a[0][1]*b[1][0])+(a[0][2]*b[2][0])
    d = (a[0][0]*b[0][1])+(a[0][1]*b[1][1])+(a[0][2]*b[2][1])
    e = (a[0][0]*b[0][2])+(a[0][1]*b[1][2])+(a[0][2]*b[2][2])
    print (f"[{c} {d} {e}]")
    f = (a[1][0]*b[0][0])+(a[1][1]*b[1][0])+(a[1][2]*b[2][0])
    g = (a[1][0]*b[0][1])+(a[1][1]*b[1][1])+(a[1][2]*b[2][1])
    h = (a[1][0]*b[0][2])+(a[1][1]*b[1][2])+(a[1][2]*b[2][2])
    print (f"[{f} {g} {h}]")
    i = (a[2][0]*b[0][0])+(a[2][1]*b[1][0])+(a[2][2]*b[2][0])
    j = (a[2][0]*b[0][1])+(a[2][1]*b[1][1])+(a[2][2]*b[2][1])
    k = (a[2][0]*b[0][2])+(a[2][1]*b[1][2])+(a[2][2]*b[2][2])
    print (f"[{i} {j} {k}]")
