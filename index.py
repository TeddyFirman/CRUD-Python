import mysql.connector
 
 
koneksi = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="crudPython"
)
 
 
mycursor = koneksi.cursor()
 
lanjut = True
while lanjut:
    print("CRUD")
    print("1.Read Data")
    print("2.Create Data")
    print("3.Update Data")
    print("4.Delete Data")
    print("5.Exit")
    print("")
     
 
    p = int(input("PILIH MENU :"))
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        print("======================")
        print("(id,nama,kelas,alamat)")
        for x in myresult:
            print(x)
    elif(p == 2):
        nama = input("Nama :")
        kelas = input("Kelas :")
        alamat = input("Alamat :")
        sql = "INSERT INTO user (nama, kelas,alamat) VALUES (%s, %s,%s)"
        val = (nama, kelas,alamat)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "data user berhasil di tambah")
    elif(p == 3):
        id = input("ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            nama = input("Nama ("+user[1]+") :") or user[1]
            kelas = input("Kelas ("+user[2]+") :") or user[2]
            alamat = input("Alamat ("+user[3]+") :") or user[3]
            sql = "UPDATE user SET nama=%s,kelas=%s,alamat=%s WHERE id=%s"
            val = (nama, kelas,alamat,id)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di simpan")
        else:
            print("data tidak ditemukan")
    elif(p == 4):
        id = input("ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            print("MENGHAPUS DATA :",user)
            sql = "DELETE FROM user WHERE id="+id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di hapus")
        else:
            print("data tidak ditemukan")
    elif(p == 5):
        lanjut = False