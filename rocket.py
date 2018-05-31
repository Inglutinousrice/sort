# 로케트 발사
import os
import time

height = float( input("얼마나 올라갈까요???! (0 : 종료)") )

if height == int(height) and height != 0:

    height = int(height)
    rocket_len = 3
    num = height - rocket_len
    cnt = 2

    #올라간당
    for i in range(0,height - rocket_len  + 1) :
        print(" 1.하아아아아아아아ㅏㅏ늘 !!앗!!",end = "")
        print("")
        for j in range(0, num) :
            if cnt < 10 :
                print(" ",cnt,sep = "")
            else :
                print(cnt)
            cnt += 1

        if cnt < 10 :
            print(" ",cnt,"         로",sep = "")
        else :
            print(cnt,"        로")
        if cnt + 1 < 10 :
            print(" ", cnt + 1, "         케",sep = "")
        else :
            print(cnt + 1, "        케")
        if cnt + 2 < 10 :
            print(" ",cnt + 2, "         또",sep = "")
        else :
            print(cnt + 2, "        또")

        cnt += 3
        for k in range(num, height - rocket_len) :
            if cnt < 10 :
                print(" ",cnt,sep = "")
            else :
                print(cnt)
            cnt += 1

        if height + 2 < 10 :
            print(" ",height + 2," 따아아아아아아아아아앙 !!앗!!",sep = "")
        else :
            print(height + 2, "따아아아아아아아아아앙 !!앗!!")
        num -= 1
        time.sleep(0.5)
        cnt = 2
        os.system("cls")



    #한칸 더 올라간당
    cnt = 2
    print(" 1.하아아아아아아아ㅏㅏ늘 !!앗!!",end = "")
    print("")
    print(" ", cnt, "         케", sep="")
    print(" ", cnt + 1, "         또", sep="")
    cnt += 2
    for j in range(0, height - 2) :
        if cnt < 10 :
            print(" ",cnt,sep = "")
        else :
            print(cnt)
        cnt += 1
    if height + 2 < 10 :
        print(" ",height + 2," 따아아아아아아아아아앙 !!앗!!",sep = "")
    else :
        print(height + 2, "따아아아아아아아아아앙 !!앗!!")
    time.sleep(0.5)
    os.system("cls")


    #또한칸 더 올라간당
    cnt = 2
    print(" 1.하아아아아아아아ㅏㅏ늘 !!앗!!",end = "")
    print("")
    print(" ", cnt, "         또", sep="")
    cnt += 1
    for j in range(0, height - 1) :
        if cnt < 10 :
            print(" ",cnt,sep = "")
        else :
            print(cnt)
        cnt += 1
    if height + 2 < 10:
        print(" ", height + 2, " 따아아아아아아아아아앙 !!앗!!", sep="")
    else:
        print(height + 2, "따아아아아아아아아아앙 !!앗!!")
    time.sleep(0.5)
    os.system("cls")



    #떨어진당
    cnt = 2
    up_height = 1
    for i in range(0,height - rocket_len  + 2) :
        print(" 1.하아아아아아아아ㅏㅏ늘 !!앗!!",end = "")
        print("")
        for j in range(0, up_height) :
            if cnt < 10 :
                print(" ",cnt,sep = "")
            else :
                print(cnt)
            cnt += 1

        if cnt < 10 :
            print(" ",cnt, "         또",sep = "")
        else :
            print(cnt, "        또")

        cnt += 1
        for k in range(up_height, height - rocket_len + 2) :
            if cnt < 10 :
                print(" ",cnt,sep = "")
            else :
                print(cnt)
            cnt += 1
        if height + 2 < 10:
            print(" ", height + 2, " 따아아아아아아아아아앙 !!앗!!", sep="")
        else:
            print(height + 2, "따아아아아아아아아아앙 !!앗!!")
        up_height += 1
        time.sleep(0.5)
        cnt = 2
        os.system("cls")

    #폭발!
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")
    print("퍼버버버ㅓ버어퍼어버어ㅓㅇ퍼ㅓ엎어퍼엉퍼ㅓㅍ어퍼엎버ㅓㅇ벙ㅍ버ㅓ어퍼버ㅓㅂㅇ펑벞펑버ㅓ")


elif height == 0:
    print("",end = "")
else :
    print("잘못 입력하셨습니다")
