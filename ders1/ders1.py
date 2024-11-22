my_list = ["Python" , "Golang","Php","Java"]
user = input("1basanda sil,2 basanda saxla")
if user == "1":
    user = input("silmek istediyiniz adi qeyd edin")
    my_list.remove(user)
    print(my_list)