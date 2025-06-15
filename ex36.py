#ex36
print('''
Bir gece odanda uyuyorken bir fısıltıyla uyanırsın.
Odanın köşesindeki eski ayna aniden parlamaya başlar.
Aynaya dokunduğunda, zamanın dışına çıkarsın — antik, büyülü bir kalenin içine çekilirsin.
Bu kale farklı çağların iç içe geçtiği bir yerdir.
Orta Çağ zindanları, teknolojik laboratuvarlar ve unutulmuş tapınaklar bir arada bulunur.
Amaç: Kaleden kaçmak ve kendi zamanına dönmek.

Ancak dikkatli ol!
Kimi kapıların arkasında tuzaklar, kimilerinde canavarlar, kimilerindeyse yardım edebilecek eski zaman yolcuları var.
Her kararın seni hayatta tutabilir ya da sonsuza dek bu zaman boşluğuna hapsolmana neden olabilir...
''')
def mirror_room():
    print("Now you are in Mirror Room.")
    print('''
                       [Gizli Tapınak]
                        ↑         ↑
                  [Zaman Tüneli]  |
                   ↑        ↑     |
         [Zindan] ←      [Ayna Odası]      → [Gelecek Laboratuvarı]
                             ↓
                      [Saat Kulesi]
    ''')
    print("Where do you wanna go?")
    choice=int(input("1.Zindan\n2.Gelecek Laboratuvarı\n3.Saat Kulesi\n4.Gizli Tapınak\n5.Zaman Tüneli\n> "))
    if choice==1:
        zindan()
    elif choice==2:
        gelecek_laboratuvari()
    elif choice==3:
        saat_kulesi()
    elif choice==4:
        gizli_tapinak()
    elif choice==5:
        zaman_tüneli()
    else:
        print("Write acceptable number!")
        mirror_room()
def zaman_tüneli():
    print('''There are 3 portals:
    1.Red Portal
    2.Blue Portal
    3.Green Portal
    There is a sentence down of the Green Portal:
    Only the person who can figure out time can go inside this portal.
    Be carefull about your choose if you choose wrong portal you can go time space and you never come back!
    If you wanna come back Mirror Room now, press "0".
    ''')
    choice=int(input("> "))
    if choice==1:
        zindan()
    elif choice==2:
        print("You are in Time Space now. You will be here forever!")
        exit(0)
    elif choice==3:
        print("You are back to real time. Congratulations!")
    elif choice==0:
        print("You gonna back to Mirror Room.")
        mirror_room()
    else:
        print("Write acceptable number!")
        mirror_room()
def zindan():
    print("There is a writing: 'You do not lose in darkness. Lİght comes from east. Do not forget 7...")
    print("You can press 0 if you want go back Mirror Room.")
    while True:
        choice = int(input("> "))
        if choice == 0:
            mirror_room()
            break
        else:
            print("Write acceptable number!")

def gelecek_laboratuvari():
    print("I always move in the time but never go back. I neither stop nor sleep. What is I?")
    answer=input("> ")
    if answer=='time':
        print("Code has been solved! Time code: AXR-1927")
        print("You can press 0 if you want go back Mirror Room.")
        while True:
            choice = int(input("> "))
            if choice == 0:
                mirror_room()
                break
            else:
                print("Write acceptable number!")
    else:
        print("Try again!")
        gelecek_laboratuvari()

def saat_kulesi():
    print("Tİme only start to flow again with true kod. Three letters, four numbers... Only the past and the future know this password.")
    i=0
    answer2=False
    while i<4 and answer2==False:
        answer=input("> ")
        if answer=='AXR-1927' and i<3:
            print("Real Time Portal was opened. You must find true Portal to go real time.")
            answer2=True
            print("You can press 0 if you want go back Mirror Room.")
            while True:
                choice = int(input("> "))
                if choice == 0:
                    mirror_room()
                    break
                else:
                    print("Write acceptable number!")
        elif answer!='AXR-1927' and i<3:
            print("Wrong answer! Try again!")
            i+=1
        else:
            print("You have been tried three time. ")
            print("You are in Time Space now. You will be here forever!")
            exit(0)
def gizli_tapinak():
    print("I am neither full nor empty, what is inside me is not known. Whoever goes into me are lost, whoever comes out is changed. What is me?")
    answer=input("> ")
    if answer=='mirror':
        print("There is a message for you from time traveler.")
        print("Do not forget the code AXR-1927 when you go through mirror. However first you must go to the tower where time has stoped.")
        print("You can press 0 if you want go back Mirror Room.")
        while True:
            choice = int(input("> "))
            if choice == 0:
                mirror_room()
                break
            else:
                print("Write acceptable number!")


    else:
        print("Wrong answer! Time travel lost!")
        print("You can press 0 if you want go back Mirror Room.")
        while True:
            choice = int(input("> "))
            if choice == 0:
                mirror_room()
                break
            else:
                print("Write acceptable number!")

mirror_room()