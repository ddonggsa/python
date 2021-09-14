

#manage_money
#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
#############################
## 공통소스 
#############################

# 공통소스내에서 주석은 각자 이름을 한줄로 표현합니다.

info = []
place_given = ["기타", "알바비", "용돈"]
place_used = ["기타", "식비", "술값", "커피", "교통비", "문화비"]
while True:
    print(""" 
***********************************
 1. 조회
 2. 추가
 3. 삭제
 4. 입금/출금 내역 수정
 5. 정렬
 6. 입금처/사용처 분류 추가
 7. 월별 통계 보기
 8. 나가기
 ***********************************
""")
    num = int(input(">"))
####2020112547 유다연 
    if num == 1:
        if len(info)>0:
            total_d = 0
            total_w = 0
            print("*********************************************************************************************************")
            print("번호\t월\t일\t시간\t입금\t\t지출\t\t분류\t\t상세정보")
            print("*********************************************************************************************************")
            for i in range(len(info)):
                print(i+1, end = ".\t")
                if info[i][0]<10:
                    print(0, end = "")
                    print(info[i][0], end = "\t")
                else:
                    print(info[i][0], end = "\t")
                if info[i][1]<10:
                    print(0, end = "")
                    print(info[i][1], end = "\t")
                else:
                    print(info[i][1], end = "\t")
                if len(info[i][2]) == 5:
                    print(info[i][2], end = "\t")
                else:
                    print(0, end = "")
                    print(info[i][2], end = "\t")
                print(info[i][5], end = "원\t\t")
                print(info[i][6], end = "원\t\t")
                if info[i][5] != 0:
                    slice_pg = place_given[info[i][7]]
                    print(slice_pg, end = "\t\t")
                else:
                    slice_pu = place_used[info[i][7]]
                    print(slice_pu, end = "\t\t")
                print(info[i][8])
                total_d += info[i][5]
                total_w += info[i][6]
            print("*********************************************************************************************************")
            print("잔액: ", end = "")
            print(total_d-total_w, end = "원\n")
            print("*********************************************************************************************************")
        else:
            print("저장되어 있는 정보가 없어 조회가 불가능합니다.")

###2020112547유다연
    elif num == 2:
        while True:
            month = input("월을 입력해주세요:(예시:05)\n>")
            if len(month) <= 2:
                if 0 < int(month) <= 12:
                    info.append([int(month)])
                    
                    break
                else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
        while True:
          
            date = input("일을 입력해 주세요:(예시:03)\n>")
            if len(date) <= 2:
                if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
                    if 0 < int(date) <= 30:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                elif int(month) == 2:
                    if 0 < int(date) <= 29:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    if 0 < int(date) <= 31:
                        info[-1].append(int(date))
                       
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
            else:
                print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
        
            time = input("시간을 입력해 주세요. (예시:10:30)\n>")
            if len(time) == 4:
                hour = int(time[0])
                minute = 10*int(time[2])+int(time[3])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                      
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            elif len(time) == 5:
                hour = 10*int(time[0])+int(time[1])
                minute = 10*int(time[3])+int(time[4])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                        
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
            choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
            if choose_dw == 1:
                info[-1].append(int(input("얼마가 입금되었습니까?\n>")))
                info[-1].append(0)
           
                #입금처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("입금처를 선택해 주세요.")
                for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
                choose_pg = int(input("\n>"))
                info[-1].append(choose_pg-1)
             
                detail = input("상세 정보를 입력해주세요.\n>")
                info[-1].append(detail)
                
                print("입금내역이 기록되었습니다.")
                enter_info = info
             
                break
            elif choose_dw == 2:
                info[-1].append(0)
                
                info[-1].append(int(input("얼마가 출금되었습니까?\n>")))
        
                #사용처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("사용처를 선택해주세요.")
                for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
                choose_pu = int(input("\n>"))
                info[-1].append(choose_pu-1)
              
                detail = input("상세 정보를 입력해주세요.\n")
                info[-1].append(detail)
             
                print("출금내역이 기록되었습니다.")
                enter_info = info
           
                break
            else:
                print("해당하는 메뉴가 존재하지 않습니다.")
                print("*************************************************")

##2020112545 배현지          
    elif num == 3:
        if len(info) > 0:
            index = int(input("몇번째 내역을 삭제하시겠습니까?"))
            del info[index-1]
           
        else:
            print("저장되어 있는 정보가 없어 삭제가 불가능합니다.")


##2020112546 김민
    elif num == 4:
        if len(info)>0:
            while True: 
                index=int(input("몇 번째 내역을 수정하시겠습니까?"))
                if index>0 and index<=len(info):
                    info[index-1][0]=int(input("월을 다시 입력해 주세요. (예시:05)\n>"))
                    info[index-1][1]=int(input("일을 다시 입력해 주세요. (예시:03)\n>"))
                    info[index-1][2]=input("시간을 다시 입력해 주세요. (예시:10:30)\n>")
                        
                    choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
                    if choose_dw==1:
                        info[index-1][5]=int(input("얼마가 입금되었습니까?\n>"))
                        info[index-1][6]=0
                        print("입금처를 선택해 주세요.")
                        for i in range(len(place_given)):
                            print(i+1, end =".")
                            print(place_given[i],end=" ")
                        choose_pg = int(input("\n>"))
                        info[index-1][7]=choose_pg-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                      
                        break

                    else:
                        info[index-1][6]=int(input("얼마가 출금되었습니까?\n>"))
                        info[index-1][5]=0
                        print("사용처를 선택해 주세요.")
                        for i in range(len(place_used)):
                            print(i+1, end =".")
                            print(place_used[i],end=" ")
                        choose_pu = int(input("\n>"))
                        info[index-1][7]=choose_pu-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                
                        break

                else:
                    print(index,"번째는 존재하지 않는 내역입니다. 다시 입력해 주세요.")

                    
        else:
            print("저장되어 있는 정보가 없어 수정이 불가능합니다.")

#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
## 2020112547 유다연 
    elif num == 5:
        if len(info)>0:
            choice = int(input("1.입력순으로 정렬하기\n2.시간순으로 정렬하기\n>"))
            if choice == 1:
                print("입력순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                info = enter_info
            elif choice == 2:
                print("시간순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                time_info = []
                for i in range(len(info)):
                    time_info.append(info[i])
                for i in range(len(info)):
                    for j in range(len(info)-1):
                        if time_info[j][0] > time_info[j+1][0]:
                            tem_time_info = time_info[j]
                            time_info[j] = time_info[j+1]
                            time_info[j+1] = tem_time_info
                        elif time_info[j][0] == time_info[j+1][0]:
                            if time_info[j][1] > time_info[j+1][1]:
                                tem_time_info = time_info[j]
                                time_info[j] = time_info[j+1]
                                time_info[j+1] = tem_time_info
                            elif time_info[j][1] == time_info[j+1][1]:
                                if time_info[j][3] > time_info[j+1][3]:
                                    tem_time_info = time_info[j]
                                    time_info[j] = time_info[j+1]
                                    time_info[j+1] = tem_time_info
                                elif time_info[j][3] == time_info[j+1][3]:
                                    if time_info[j][4] > time_info[j+1][4]:
                                        tem_time_info = time_info[j]
                                        time_info[j] = time_info[j+1]
                                        time_info[j+1] = tem_time_info
                info = time_info
        else:
            print("저장되어 있는 정보가 없어 정렬이 불가능합니다.")
        
      
            


##2020112545 배현지
    elif num == 6:

        print("입금처 분류와 사용처 분류 중에서 어떤 것을 추가하시겠습니까?")
        print("1.입금처\n2.사용처")
        choice = int(input(">"))
        if choice == 1:
            print("현재 입금처의 분류는")
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("입니다.")
            place_given_add = input("추가할 분류를 입력해 주세요.\n>")
            place_given.append(place_given_add)
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")
            

        elif choice == 2:
            print("현재 사용처의 분류는")
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("입니다")
            place_used_add = input("추가할 분류를 입력해 주세요\n>")
            place_used.append(place_used_add)
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")
   


    ## 2020112546 김민     
    elif num == 7:
        month_list=[]
        for x in range(len(info)):
            month_list.append(info[x][0])
        print("조회하고 싶으신 달을 입력하세요.(입력예시:05)")
        watch_month = int(input(">"))
        for x in range(len(info)):
            if watch_month in month_list:
                print("어떤 통계를 볼지 선택해주세요.")
                print("1.지출통계\n2.입금통계")
                watch_total = int(input(">"))
                
                if watch_total == 1:

                        pu_total_list = []
                        pu_total = 0
                        total = 0

                        print("**********************************************지출통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):                                        
                            if watch_month == info[i][0]:
                                if info[i][5]==0:
                                    for j in range(len(place_used)):
                                        if len(pu_total_list)<=len(place_used):
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total+=info[i][6]
                                                pu_total_list.append(pu_total)
                                            else:
                                                pu_total_list.append(0)
                                            
                                        else:
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total=pu_total_list[j]+info[i][6]
                                                pu_total_list[j]=pu_total
                        for i in range(len(info)):
                            if watch_month<10:
                                for j in range(len(place_used)): 
                                    print(0, end = "")
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break
                            else:
                                for j in range(len(place_used)): 
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break

                        print("*********************************************************************************************************")
                        print("지출 금액 합계:", total, "원")
                        break
        

                if watch_total == 2:

                        pg_total_list = []
                        pg_total = 0
                        total = 0
                        
                        print("**********************************************입금통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):
                            if watch_month == info[i][0]:
                                if info[i][6]==0:
                                    for j in range(len(place_given)):
                                        if len(pg_total_list)<=len(place_given):
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total+=info[i][5]
                                                pg_total_list.append(pg_total)
                                            else:
                                                pg_total_list.append(0)
                                            
                                        else:
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total=pg_total_list[j]+info[i][5]
                                                pg_total_list[j]=pg_total

                        

                        for i in range(len(info)):
                                if watch_month<10:
                                    for j in range(len(place_given)): 
                                        print(0, end = "")
                                        print(0+watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                                else:
                                    for j in range(len(place_used)): 
                                        print(watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                        
                        print("*********************************************************************************************************")
                        print("입금 금액 합계:",total,"원")
                        break
        

            else:
                print("해당하는 달이 없습니다.")
                break    
   
##2020112545 배현지 
    elif num == 8:
        out1 = 1
        out2 = 1
        while True:
            print("저희 용돈기입장을 이용해 주셔서 감사합니다. 별점을 남겨주시겠습니까?")
            print("1.Yes")
            print("2.No")
            yn = int(input(">"))
            if yn == 1:
                while True:
                    print("☆☆☆☆☆")
                    print("별점을 남겨주세요.(1점~5점 중에서 선택)")
                    star = int(input(">"))
                    if star <= 5:
                        for i in range(star):
                            print("★", end = "")
                        for i in range(5-star):
                            print("☆", end = "")
                            print()
                            print("감사합니다. 또 이용해주세요.")
                            out1 = 0
                            out2 = 0
                            break
                    else:
                        print("1점~5점 중에서 선택해주세요.")
                if out1 == 0:
                    break
            elif yn == 2:
                print("감사합니다. 또 이용해주세요.")
                out2 = 0
                break
            else:
                print("1번과 2번 중에 선택해주세요.")
        if out2 == 0:
            break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("메뉴는 1~7입니다.")





#############################
## 2020112547유다연
#############################
#manage_money
#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
info = []
place_given = ["기타", "알바비", "용돈"]
place_used = ["기타", "식비", "술값", "커피", "교통비", "문화비"]
while True:
    print(""" 
***********************************
 1. 조회
 2. 추가
 3. 삭제
 4. 입금/출금 내역 수정
 5. 정렬
 6. 입금처/사용처 분류 추가
 7. 월별 통계 보기
 8. 나가기
 ***********************************
""")
    num = int(input(">"))
##############################################################
############ 2020112547유다연
    if num == 1:
        if len(info)>0:
            total_d = 0
            total_w = 0
            print("*********************************************************************************************************")
            print("번호\t월\t일\t시간\t입금\t\t지출\t\t분류\t\t상세정보")
            print("*********************************************************************************************************")
            for i in range(len(info)):
                print(i+1, end = ".\t")
                if info[i][0]<10:
                    print(0, end = "")
                    print(info[i][0], end = "\t")
                else:
                    print(info[i][0], end = "\t")
                if info[i][1]<10:
                    print(0, end = "")
                    print(info[i][1], end = "\t")
                else:
                    print(info[i][1], end = "\t")
                if len(info[i][2]) == 5:
                    print(info[i][2], end = "\t")
                else:
                    print(0, end = "")
                    print(info[i][2], end = "\t")
                print(info[i][5], end = "원\t\t")
                print(info[i][6], end = "원\t\t")
                if info[i][5] != 0:
                    slice_pg = place_given[info[i][7]]
                    print(slice_pg, end = "\t\t")
                else:
                    slice_pu = place_used[info[i][7]]
                    print(slice_pu, end = "\t\t")
                print(info[i][8])
                total_d += info[i][5]
                total_w += info[i][6]
            print("*********************************************************************************************************")
            print("잔액: ", end = "")
            print(total_d-total_w, end = "원\n")
            print("*********************************************************************************************************")
        else:
            print("저장되어 있는 정보가 없어 조회가 불가능합니다.")
    elif num == 2:
        while True:
            month = input("월을 입력해주세요:(예시:05)\n>")
            if len(month) <= 2:
                if 0 < int(month) <= 12:
                    info.append([int(month)])
                    
                    break
                else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
        while True:
          
            date = input("일을 입력해 주세요:(예시:03)\n>")
            if len(date) <= 2:
                if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
                    if 0 < int(date) <= 30:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                elif int(month) == 2:
                    if 0 < int(date) <= 29:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    if 0 < int(date) <= 31:
                        info[-1].append(int(date))
                       
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
            else:
                print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
        
            time = input("시간을 입력해 주세요. (예시:10:30)\n>")
            if len(time) == 4:
                hour = int(time[0])
                minute = 10*int(time[2])+int(time[3])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                      
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            elif len(time) == 5:
                hour = 10*int(time[0])+int(time[1])
                minute = 10*int(time[3])+int(time[4])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                        
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
            choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
            if choose_dw == 1:
                info[-1].append(int(input("얼마가 입금되었습니까?\n>")))
                info[-1].append(0)
           
                #입금처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("입금처를 선택해 주세요.")
                for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
                choose_pg = int(input("\n>"))
                info[-1].append(choose_pg-1)
             
                detail = input("상세 정보를 입력해주세요.\n>")
                info[-1].append(detail)
                
                print("입금내역이 기록되었습니다.")
                enter_info = info
             
                break
            elif choose_dw == 2:
                info[-1].append(0)
                
                info[-1].append(int(input("얼마가 출금되었습니까?\n>")))
        
                #사용처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("사용처를 선택해주세요.")
                for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
                choose_pu = int(input("\n>"))
                info[-1].append(choose_pu-1)
              
                detail = input("상세 정보를 입력해주세요.\n")
                info[-1].append(detail)
             
                print("출금내역이 기록되었습니다.")
                enter_info = info
           
                break
            else:
                print("해당하는 메뉴가 존재하지 않습니다.")
                print("*************************************************")

###################################################################
##2020112545 배현지
 
    elif num == 3:
        if len(info) > 0:
            index = int(input("몇번째 내역을 삭제하시겠습니까?"))
            del info[index-1]
           
        else:
            print("저장되어 있는 정보가 없어 삭제가 불가능합니다.")


    elif num == 4:
        if len(info)>0:
            while True: 
                index=int(input("몇 번째 내역을 수정하시겠습니까?"))
                if index>0 and index<=len(info):
                    info[index-1][0]=int(input("월을 다시 입력해 주세요. (예시:05)\n>"))
                    info[index-1][1]=int(input("일을 다시 입력해 주세요. (예시:03)\n>"))
                    info[index-1][2]=input("시간을 다시 입력해 주세요. (예시:10:30)\n>")
                        
                    choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
                    if choose_dw==1:
                        info[index-1][5]=int(input("얼마가 입금되었습니까?\n>"))
                        info[index-1][6]=0
                        print("입금처를 선택해 주세요.")
                        for i in range(len(place_given)):
                            print(i+1, end =".")
                            print(place_given[i],end=" ")
                        choose_pg = int(input("\n>"))
                        info[index-1][7]=choose_pg-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                      
                        break

                    else:
                        info[index-1][6]=int(input("얼마가 출금되었습니까?\n>"))
                        info[index-1][5]=0
                        print("사용처를 선택해 주세요.")
                        for i in range(len(place_used)):
                            print(i+1, end =".")
                            print(place_used[i],end=" ")
                        choose_pu = int(input("\n>"))
                        info[index-1][7]=choose_pu-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                
                        break

                else:
                    print(index,"번째는 존재하지 않는 내역입니다. 다시 입력해 주세요.")

                    
        else:
            print("저장되어 있는 정보가 없어 수정이 불가능합니다.")

#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
##########################################################
## 2020112547 유다연 
    elif num == 5:
        if len(info)>0:
            choice = int(input("1.입력순으로 정렬하기\n2.시간순으로 정렬하기\n>"))
            if choice == 1:
                print("입력순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                info = enter_info
            elif choice == 2:
                print("시간순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                time_info = []
                for i in range(len(info)):
                    time_info.append(info[i])
                for i in range(len(info)):
                    for j in range(len(info)-1):
                        if time_info[j][0] > time_info[j+1][0]:
                            tem_time_info = time_info[j]
                            time_info[j] = time_info[j+1]
                            time_info[j+1] = tem_time_info
                        elif time_info[j][0] == time_info[j+1][0]:
                            if time_info[j][1] > time_info[j+1][1]:
                                tem_time_info = time_info[j]
                                time_info[j] = time_info[j+1]
                                time_info[j+1] = tem_time_info
                            elif time_info[j][1] == time_info[j+1][1]:
                                if time_info[j][3] > time_info[j+1][3]:
                                    tem_time_info = time_info[j]
                                    time_info[j] = time_info[j+1]
                                    time_info[j+1] = tem_time_info
                                elif time_info[j][3] == time_info[j+1][3]:
                                    if time_info[j][4] > time_info[j+1][4]:
                                        tem_time_info = time_info[j]
                                        time_info[j] = time_info[j+1]
                                        time_info[j+1] = tem_time_info
                info = time_info
        else:
            print("저장되어 있는 정보가 없어 정렬이 불가능합니다.")
##########################################################


##2020112545 배현지

    elif num == 6:

        print("입금처 분류와 사용처 분류 중에서 어떤 것을 추가하시겠습니까?")
        print("1.입금처\n2.사용처")
        choice = int(input(">"))
        if choice == 1:
            print("현재 입금처의 분류는")
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("입니다.")
            place_given_add = input("추가할 분류를 입력해 주세요.\n>")
            place_given.append(place_given_add)
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")
            

        elif choice == 2:
            print("현재 사용처의 분류는")
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("입니다")
            place_used_add = input("추가할 분류를 입력해 주세요\n>")
            place_used.append(place_used_add)
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")



   
  
    elif num == 7:
        month_list=[]
        for x in range(len(info)):
            month_list.append(info[x][0])
        print("조회하고 싶으신 달을 입력하세요.(입력예시:05)")
        watch_month = int(input(">"))
        for x in range(len(info)):
            if watch_month in month_list:
                print("어떤 통계를 볼지 선택해주세요.")
                print("1.지출통계\n2.입금통계")
                watch_total = int(input(">"))
                
                if watch_total == 1:

                        pu_total_list = []
                        pu_total = 0
                        total = 0

                        print("**********************************************지출통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):                                        
                            if watch_month == info[i][0]:
                                if info[i][5]==0:
                                    for j in range(len(place_used)):
                                        if len(pu_total_list)<=len(place_used):
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total+=info[i][6]
                                                pu_total_list.append(pu_total)
                                            else:
                                                pu_total_list.append(0)
                                            
                                        else:
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total=pu_total_list[j]+info[i][6]
                                                pu_total_list[j]=pu_total
                        for i in range(len(info)):
                            if watch_month<10:
                                for j in range(len(place_used)): 
                                    print(0, end = "")
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break
                            else:
                                for j in range(len(place_used)): 
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break

                        print("*********************************************************************************************************")
                        print("지출 금액 합계:", total, "원")
                        break
        

                if watch_total == 2:

                        pg_total_list = []
                        pg_total = 0
                        total = 0
                        
                        print("**********************************************입금통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):
                            if watch_month == info[i][0]:
                                if info[i][6]==0:
                                    for j in range(len(place_given)):
                                        if len(pg_total_list)<=len(place_given):
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total+=info[i][5]
                                                pg_total_list.append(pg_total)
                                            else:
                                                pg_total_list.append(0)
                                            
                                        else:
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total=pg_total_list[j]+info[i][5]
                                                pg_total_list[j]=pg_total

                        

                        for i in range(len(info)):
                                if watch_month<10:
                                    for j in range(len(place_given)): 
                                        print(0, end = "")
                                        print(0+watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                                else:
                                    for j in range(len(place_used)): 
                                        print(watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                        
                        print("*********************************************************************************************************")
                        print("입금 금액 합계:",total,"원")
                        break
        

            else:
                print("해당하는 달이 없습니다.")
                break 

##2020112545 배현지
 
    elif num == 8:
        out1 = 1
        out2 = 1
        while True:
            print("저희 용돈기입장을 이용해 주셔서 감사합니다. 별점을 남겨주시겠습니까?")
            print("1.Yes")
            print("2.No")
            yn = int(input(">"))
            if yn == 1:
                while True:
                    print("☆☆☆☆☆")
                    print("별점을 남겨주세요.(1점~5점 중에서 선택)")
                    star = int(input(">"))
                    if star <= 5:
                        for i in range(star):
                            print("★", end = "")
                        for i in range(5-star):
                            print("☆", end = "")
                            print()
                            print("감사합니다. 또 이용해주세요.")
                            out1 = 0
                            out2 = 0
                            break
                    else:
                        print("1점~5점 중에서 선택해주세요.")
                if out1 == 0:
                    break
            elif yn == 2:
                print("감사합니다. 또 이용해주세요.")
                out2 = 0
                break
            else:
                print("1번과 2번 중에 선택해주세요.")
        if out2 == 0:
            break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("메뉴는 1~7입니다.")








##########################################################
##2020112546 김민
##########################################################
#manage_money
#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
info = []
place_given = ["기타", "알바비", "용돈"]
place_used = ["기타", "식비", "술값", "커피", "교통비", "문화비"]
while True:
    print(""" 
***********************************
 1. 조회
 2. 추가
 3. 삭제
 4. 입금/출금 내역 수정
 5. 정렬
 6. 입금처/사용처 분류 추가
 7. 월별 통계 보기
 8. 나가기
 ***********************************
""")
    num = int(input(">"))

    if num == 1:
        if len(info)>0:
            total_d = 0
            total_w = 0
            print("*********************************************************************************************************")
            print("번호\t월\t일\t시간\t입금\t\t지출\t\t분류\t\t상세정보")
            print("*********************************************************************************************************")
            for i in range(len(info)):
                print(i+1, end = ".\t")
                if info[i][0]<10:
                    print(0, end = "")
                    print(info[i][0], end = "\t")
                else:
                    print(info[i][0], end = "\t")
                if info[i][1]<10:
                    print(0, end = "")
                    print(info[i][1], end = "\t")
                else:
                    print(info[i][1], end = "\t")
                if len(info[i][2]) == 5:
                    print(info[i][2], end = "\t")
                else:
                    print(0, end = "")
                    print(info[i][2], end = "\t")
                print(info[i][5], end = "원\t\t")
                print(info[i][6], end = "원\t\t")
                if info[i][5] != 0:
                    slice_pg = place_given[info[i][7]]
                    print(slice_pg, end = "\t\t")
                else:
                    slice_pu = place_used[info[i][7]]
                    print(slice_pu, end = "\t\t")
                print(info[i][8])
                total_d += info[i][5]
                total_w += info[i][6]
            print("*********************************************************************************************************")
            print("잔액: ", end = "")
            print(total_d-total_w, end = "원\n")
            print("*********************************************************************************************************")
        else:
            print("저장되어 있는 정보가 없어 조회가 불가능합니다.")
    elif num == 2:
        while True:
            month = input("월을 입력해주세요:(예시:05)\n>")
            if len(month) <= 2:
                if 0 < int(month) <= 12:
                    info.append([int(month)])
                    
                    break
                else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
        while True:
          
            date = input("일을 입력해 주세요:(예시:03)\n>")
            if len(date) <= 2:
                if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
                    if 0 < int(date) <= 30:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                elif int(month) == 2:
                    if 0 < int(date) <= 29:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    if 0 < int(date) <= 31:
                        info[-1].append(int(date))
                       
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
            else:
                print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
        
            time = input("시간을 입력해 주세요. (예시:10:30)\n>")
            if len(time) == 4:
                hour = int(time[0])
                minute = 10*int(time[2])+int(time[3])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                      
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            elif len(time) == 5:
                hour = 10*int(time[0])+int(time[1])
                minute = 10*int(time[3])+int(time[4])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                        
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
            choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
            if choose_dw == 1:
                info[-1].append(int(input("얼마가 입금되었습니까?\n>")))
                info[-1].append(0)
           
                #입금처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("입금처를 선택해 주세요.")
                for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
                choose_pg = int(input("\n>"))
                info[-1].append(choose_pg-1)
             
                detail = input("상세 정보를 입력해주세요.\n>")
                info[-1].append(detail)
                
                print("입금내역이 기록되었습니다.")
                enter_info = info
             
                break
            elif choose_dw == 2:
                info[-1].append(0)
                
                info[-1].append(int(input("얼마가 출금되었습니까?\n>")))
        
                #사용처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("사용처를 선택해주세요.")
                for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
                choose_pu = int(input("\n>"))
                info[-1].append(choose_pu-1)
              
                detail = input("상세 정보를 입력해주세요.\n")
                info[-1].append(detail)
             
                print("출금내역이 기록되었습니다.")
                enter_info = info
           
                break
            else:
                print("해당하는 메뉴가 존재하지 않습니다.")
                print("*************************************************")


         
    elif num == 3:
        if len(info) > 0:
            index = int(input("몇번째 내역을 삭제하시겠습니까?"))
            del info[index-1]
           
        else:
            print("저장되어 있는 정보가 없어 삭제가 불가능합니다.")

###################################################################
##2020112546김민
    elif num == 4:
        if len(info)>0:
            while True: 
                index=int(input("몇 번째 내역을 수정하시겠습니까?"))
                if index>0 and index<=len(info):
                    info[index-1][0]=int(input("월을 다시 입력해 주세요. (예시:05)\n>"))
                    info[index-1][1]=int(input("일을 다시 입력해 주세요. (예시:03)\n>"))
                    info[index-1][2]=input("시간을 다시 입력해 주세요. (예시:10:30)\n>")
                        
                    choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
                    if choose_dw==1:
                        info[index-1][5]=int(input("얼마가 입금되었습니까?\n>"))
                        info[index-1][6]=0
                        print("입금처를 선택해 주세요.")
                        for i in range(len(place_given)):
                            print(i+1, end =".")
                            print(place_given[i],end=" ")
                        choose_pg = int(input("\n>"))
                        info[index-1][7]=choose_pg-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                      
                        break

                    else:
                        info[index-1][6]=int(input("얼마가 출금되었습니까?\n>"))
                        info[index-1][5]=0
                        print("사용처를 선택해 주세요.")
                        for i in range(len(place_used)):
                            print(i+1, end =".")
                            print(place_used[i],end=" ")
                        choose_pu = int(input("\n>"))
                        info[index-1][7]=choose_pu-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                
                        break

                else:
                    print(index,"번째는 존재하지 않는 내역입니다. 다시 입력해 주세요.")

                    
        else:
            print("저장되어 있는 정보가 없어 수정이 불가능합니다.")

#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
##########################################################

    elif num == 5:
        if len(info)>0:
            choice = int(input("1.입력순으로 정렬하기\n2.시간순으로 정렬하기\n>"))
            if choice == 1:
                print("입력순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                info = enter_info
            elif choice == 2:
                print("시간순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                time_info = []
                for i in range(len(info)):
                    time_info.append(info[i])
                for i in range(len(info)):
                    for j in range(len(info)-1):
                        if time_info[j][0] > time_info[j+1][0]:
                            tem_time_info = time_info[j]
                            time_info[j] = time_info[j+1]
                            time_info[j+1] = tem_time_info
                        elif time_info[j][0] == time_info[j+1][0]:
                            if time_info[j][1] > time_info[j+1][1]:
                                tem_time_info = time_info[j]
                                time_info[j] = time_info[j+1]
                                time_info[j+1] = tem_time_info
                            elif time_info[j][1] == time_info[j+1][1]:
                                if time_info[j][3] > time_info[j+1][3]:
                                    tem_time_info = time_info[j]
                                    time_info[j] = time_info[j+1]
                                    time_info[j+1] = tem_time_info
                                elif time_info[j][3] == time_info[j+1][3]:
                                    if time_info[j][4] > time_info[j+1][4]:
                                        tem_time_info = time_info[j]
                                        time_info[j] = time_info[j+1]
                                        time_info[j+1] = tem_time_info
                info = time_info
        else:
            print("저장되어 있는 정보가 없어 정렬이 불가능합니다.")
     

    elif num == 6:

        print("입금처 분류와 사용처 분류 중에서 어떤 것을 추가하시겠습니까?")
        print("1.입금처\n2.사용처")
        choice = int(input(">"))
        if choice == 1:
            print("현재 입금처의 분류는")
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("입니다.")
            place_given_add = input("추가할 분류를 입력해 주세요.\n>")
            place_given.append(place_given_add)
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")
            

        elif choice == 2:
            print("현재 사용처의 분류는")
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("입니다")
            place_used_add = input("추가할 분류를 입력해 주세요\n>")
            place_used.append(place_used_add)
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")

##########################################################
##2020112546김민
  
    elif num == 7:
        month_list=[]
        for x in range(len(info)):
            month_list.append(info[x][0])
        print("조회하고 싶으신 달을 입력하세요.(입력예시:05)")
        watch_month = int(input(">"))
        for x in range(len(info)):
            if watch_month in month_list:
                print("어떤 통계를 볼지 선택해주세요.")
                print("1.지출통계\n2.입금통계")
                watch_total = int(input(">"))
                
                if watch_total == 1:

                        pu_total_list = []
                        pu_total = 0
                        total = 0

                        print("**********************************************지출통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):                                        
                            if watch_month == info[i][0]:
                                if info[i][5]==0:
                                    for j in range(len(place_used)):
                                        if len(pu_total_list)<=len(place_used):
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total+=info[i][6]
                                                pu_total_list.append(pu_total)
                                            else:
                                                pu_total_list.append(0)
                                            
                                        else:
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total=pu_total_list[j]+info[i][6]
                                                pu_total_list[j]=pu_total
                        for i in range(len(info)):
                            if watch_month<10:
                                for j in range(len(place_used)): 
                                    print(0, end = "")
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break
                            else:
                                for j in range(len(place_used)): 
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break

                        print("*********************************************************************************************************")
                        print("지출 금액 합계:", total, "원")
                        break
        

                if watch_total == 2:

                        pg_total_list = []
                        pg_total = 0
                        total = 0
                        
                        print("**********************************************입금통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):
                            if watch_month == info[i][0]:
                                if info[i][6]==0:
                                    for j in range(len(place_given)):
                                        if len(pg_total_list)<=len(place_given):
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total+=info[i][5]
                                                pg_total_list.append(pg_total)
                                            else:
                                                pg_total_list.append(0)
                                            
                                        else:
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total=pg_total_list[j]+info[i][5]
                                                pg_total_list[j]=pg_total

                        

                        for i in range(len(info)):
                                if watch_month<10:
                                    for j in range(len(place_given)): 
                                        print(0, end = "")
                                        print(0+watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                                else:
                                    for j in range(len(place_used)): 
                                        print(watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                        
                        print("*********************************************************************************************************")
                        print("입금 금액 합계:",total,"원")
                        break
        

            else:
                print("해당하는 달이 없습니다.")
                break   
#########################################################################

    elif num == 8:
        out1 = 1
        out2 = 1
        while True:
            print("저희 용돈기입장을 이용해 주셔서 감사합니다. 별점을 남겨주시겠습니까?")
            print("1.Yes")
            print("2.No")
            yn = int(input(">"))
            if yn == 1:
                while True:
                    print("☆☆☆☆☆")
                    print("별점을 남겨주세요.(1점~5점 중에서 선택)")
                    star = int(input(">"))
                    if star <= 5:
                        for i in range(star):
                            print("★", end = "")
                        for i in range(5-star):
                            print("☆", end = "")
                            print()
                            print("감사합니다. 또 이용해주세요.")
                            out1 = 0
                            out2 = 0
                            break
                    else:
                        print("1점~5점 중에서 선택해주세요.")
                if out1 == 0:
                    break
            elif yn == 2:
                print("감사합니다. 또 이용해주세요.")
                out2 = 0
                break
            else:
                print("1번과 2번 중에 선택해주세요.")
        if out2 == 0:
            break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("메뉴는 1~7입니다.")








##########################################################
##2020112545배현지
##########################################################
#manage_money
#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]
info = []
place_given = ["기타", "알바비", "용돈"]
place_used = ["기타", "식비", "술값", "커피", "교통비", "문화비"]
while True:
    print(""" 
***********************************
 1. 조회
 2. 추가
 3. 삭제
 4. 입금/출금 내역 수정
 5. 정렬
 6. 입금처/사용처 분류 추가
 7. 월별 통계 보기
 8. 나가기
 ***********************************
""")
    num = int(input(">"))

    if num == 1:
        if len(info)>0:
            total_d = 0
            total_w = 0
            print("*********************************************************************************************************")
            print("번호\t월\t일\t시간\t입금\t\t지출\t\t분류\t\t상세정보")
            print("*********************************************************************************************************")
            for i in range(len(info)):
                print(i+1, end = ".\t")
                if info[i][0]<10:
                    print(0, end = "")
                    print(info[i][0], end = "\t")
                else:
                    print(info[i][0], end = "\t")
                if info[i][1]<10:
                    print(0, end = "")
                    print(info[i][1], end = "\t")
                else:
                    print(info[i][1], end = "\t")
                if len(info[i][2]) == 5:
                    print(info[i][2], end = "\t")
                else:
                    print(0, end = "")
                    print(info[i][2], end = "\t")
                print(info[i][5], end = "원\t\t")
                print(info[i][6], end = "원\t\t")
                if info[i][5] != 0:
                    slice_pg = place_given[info[i][7]]
                    print(slice_pg, end = "\t\t")
                else:
                    slice_pu = place_used[info[i][7]]
                    print(slice_pu, end = "\t\t")
                print(info[i][8])
                total_d += info[i][5]
                total_w += info[i][6]
            print("*********************************************************************************************************")
            print("잔액: ", end = "")
            print(total_d-total_w, end = "원\n")
            print("*********************************************************************************************************")
        else:
            print("저장되어 있는 정보가 없어 조회가 불가능합니다.")
    elif num == 2:
        while True:
            month = input("월을 입력해주세요:(예시:05)\n>")
            if len(month) <= 2:
                if 0 < int(month) <= 12:
                    info.append([int(month)])
                    
                    break
                else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                    print("존재하는 달이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
        while True:
          
            date = input("일을 입력해 주세요:(예시:03)\n>")
            if len(date) <= 2:
                if int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
                    if 0 < int(date) <= 30:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                elif int(month) == 2:
                    if 0 < int(date) <= 29:
                        info[-1].append(int(date))
                        
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    if 0 < int(date) <= 31:
                        info[-1].append(int(date))
                       
                        break
                    else:
                        print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
            else:
                print("존재하는 일이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
        
            time = input("시간을 입력해 주세요. (예시:10:30)\n>")
            if len(time) == 4:
                hour = int(time[0])
                minute = 10*int(time[2])+int(time[3])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                      
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            elif len(time) == 5:
                hour = 10*int(time[0])+int(time[1])
                minute = 10*int(time[3])+int(time[4])
                if hour <= 23:
                    if minute <= 59:
                        info[-1].append(time)
                        info[-1].append(hour)
                        info[-1].append(minute)
                        
                        break
                    else:
                        print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                        print("**************************************************")
                else:
                    print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                    print("**************************************************")
            else:
                print("존재하는 시간이 아닙니다. 다시 입력해주세요.")
                print("**************************************************")
        while True:
            choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
            if choose_dw == 1:
                info[-1].append(int(input("얼마가 입금되었습니까?\n>")))
                info[-1].append(0)
           
                #입금처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("입금처를 선택해 주세요.")
                for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
                choose_pg = int(input("\n>"))
                info[-1].append(choose_pg-1)
             
                detail = input("상세 정보를 입력해주세요.\n>")
                info[-1].append(detail)
                
                print("입금내역이 기록되었습니다.")
                enter_info = info
             
                break
            elif choose_dw == 2:
                info[-1].append(0)
                
                info[-1].append(int(input("얼마가 출금되었습니까?\n>")))
        
                #사용처 예외처리하기(없는 인덱스 누르면 다시 받기)
                print("사용처를 선택해주세요.")
                for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
                choose_pu = int(input("\n>"))
                info[-1].append(choose_pu-1)
              
                detail = input("상세 정보를 입력해주세요.\n")
                info[-1].append(detail)
             
                print("출금내역이 기록되었습니다.")
                enter_info = info
           
                break
            else:
                print("해당하는 메뉴가 존재하지 않습니다.")
                print("*************************************************")


  ###########################################################
######2020112545배현지       
    elif num == 3:
        if len(info) > 0:
            index = int(input("몇번째 내역을 삭제하시겠습니까?"))
            del info[index-1]
           
        else:
            print("저장되어 있는 정보가 없어 삭제가 불가능합니다.")
#############################################################

    elif num == 4:
        if len(info)>0:
            while True: 
                index=int(input("몇 번째 내역을 수정하시겠습니까?"))
                if index>0 and index<=len(info):
                    info[index-1][0]=int(input("월을 다시 입력해 주세요. (예시:05)\n>"))
                    info[index-1][1]=int(input("일을 다시 입력해 주세요. (예시:03)\n>"))
                    info[index-1][2]=input("시간을 다시 입력해 주세요. (예시:10:30)\n>")
                        
                    choose_dw = int(input("입금, 출금 중에서 선택해주세요. 번호만 써주시면 됩니다.\n1.입금\n2.출금\n>"))
                    if choose_dw==1:
                        info[index-1][5]=int(input("얼마가 입금되었습니까?\n>"))
                        info[index-1][6]=0
                        print("입금처를 선택해 주세요.")
                        for i in range(len(place_given)):
                            print(i+1, end =".")
                            print(place_given[i],end=" ")
                        choose_pg = int(input("\n>"))
                        info[index-1][7]=choose_pg-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                      
                        break

                    else:
                        info[index-1][6]=int(input("얼마가 출금되었습니까?\n>"))
                        info[index-1][5]=0
                        print("사용처를 선택해 주세요.")
                        for i in range(len(place_used)):
                            print(i+1, end =".")
                            print(place_used[i],end=" ")
                        choose_pu = int(input("\n>"))
                        info[index-1][7]=choose_pu-1
                        detail = input("상세 정보를 입력해주세요.\n>")
                        info[index-1][8]=detail
                
                        break

                else:
                    print(index,"번째는 존재하지 않는 내역입니다. 다시 입력해 주세요.")

                    
        else:
            print("저장되어 있는 정보가 없어 수정이 불가능합니다.")

#info = [월,일,시간,시,분,입금액,지출액,분류번호,상세정보]

    elif num == 5:
        if len(info)>0:
            choice = int(input("1.입력순으로 정렬하기\n2.시간순으로 정렬하기\n>"))
            if choice == 1:
                print("입력순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                info = enter_info
            elif choice == 2:
                print("시간순으로 정렬되었습니다. 확인하시려면 조회 버튼을 눌러주세요.")
                time_info = []
                for i in range(len(info)):
                    time_info.append(info[i])
                for i in range(len(info)):
                    for j in range(len(info)-1):
                        if time_info[j][0] > time_info[j+1][0]:
                            tem_time_info = time_info[j]
                            time_info[j] = time_info[j+1]
                            time_info[j+1] = tem_time_info
                        elif time_info[j][0] == time_info[j+1][0]:
                            if time_info[j][1] > time_info[j+1][1]:
                                tem_time_info = time_info[j]
                                time_info[j] = time_info[j+1]
                                time_info[j+1] = tem_time_info
                            elif time_info[j][1] == time_info[j+1][1]:
                                if time_info[j][3] > time_info[j+1][3]:
                                    tem_time_info = time_info[j]
                                    time_info[j] = time_info[j+1]
                                    time_info[j+1] = tem_time_info
                                elif time_info[j][3] == time_info[j+1][3]:
                                    if time_info[j][4] > time_info[j+1][4]:
                                        tem_time_info = time_info[j]
                                        time_info[j] = time_info[j+1]
                                        time_info[j+1] = tem_time_info
                info = time_info
        else:
            print("저장되어 있는 정보가 없어 정렬이 불가능합니다.")

     
 ########################################################## 
#####2020112545배현지
    elif num == 6:

        print("입금처 분류와 사용처 분류 중에서 어떤 것을 추가하시겠습니까?")
        print("1.입금처\n2.사용처")
        choice = int(input(">"))
        if choice == 1:
            print("현재 입금처의 분류는")
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("입니다.")
            place_given_add = input("추가할 분류를 입력해 주세요.\n>")
            place_given.append(place_given_add)
            for i in range(len(place_given)):
                    print(i+1, end =".")
                    print(place_given[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")
            

        elif choice == 2:
            print("현재 사용처의 분류는")
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("입니다")
            place_used_add = input("추가할 분류를 입력해 주세요\n>")
            place_used.append(place_used_add)
            for i in range(len(place_used)):
                    print(i+1, end =".")
                    print(place_used[i], end = " ")
            print("으로(로) 바뀌었습니다.",sep="")
  ########################################################## 
  
    elif num == 7:
        month_list=[]
        for x in range(len(info)):
            month_list.append(info[x][0])
        print("조회하고 싶으신 달을 입력하세요.(입력예시:05)")
        watch_month = int(input(">"))
        for x in range(len(info)):
            if watch_month in month_list:
                print("어떤 통계를 볼지 선택해주세요.")
                print("1.지출통계\n2.입금통계")
                watch_total = int(input(">"))
                
                if watch_total == 1:

                        pu_total_list = []
                        pu_total = 0
                        total = 0

                        print("**********************************************지출통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):                                        
                            if watch_month == info[i][0]:
                                if info[i][5]==0:
                                    for j in range(len(place_used)):
                                        if len(pu_total_list)<=len(place_used):
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total+=info[i][6]
                                                pu_total_list.append(pu_total)
                                            else:
                                                pu_total_list.append(0)
                                            
                                        else:
                                            if place_used.index(place_used[j])==info[i][7]:
                                                total+=info[i][6]
                                                pu_total=pu_total_list[j]+info[i][6]
                                                pu_total_list[j]=pu_total
                        for i in range(len(info)):
                            if watch_month<10:
                                for j in range(len(place_used)): 
                                    print(0, end = "")
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break
                            else:
                                for j in range(len(place_used)): 
                                    print(watch_month,"월","\t",place_used[j],end="")
                                    print("\t",pu_total_list[j],"원")
                                break

                        print("*********************************************************************************************************")
                        print("지출 금액 합계:", total, "원")
                        break
        

                if watch_total == 2:

                        pg_total_list = []
                        pg_total = 0
                        total = 0
                        
                        print("**********************************************입금통계*************************************************")
                        print("*********************************************************************************************************")
                        print("월\t구분\t금액")
                        print("*********************************************************************************************************")
                        for i in range(len(info)):
                            if watch_month == info[i][0]:
                                if info[i][6]==0:
                                    for j in range(len(place_given)):
                                        if len(pg_total_list)<=len(place_given):
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total+=info[i][5]
                                                pg_total_list.append(pg_total)
                                            else:
                                                pg_total_list.append(0)
                                            
                                        else:
                                            if place_given.index(place_given[j])==info[i][7]:
                                                total+=info[i][5]
                                                pg_total=pg_total_list[j]+info[i][5]
                                                pg_total_list[j]=pg_total

                        

                        for i in range(len(info)):
                                if watch_month<10:
                                    for j in range(len(place_given)): 
                                        print(0, end = "")
                                        print(0+watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                                else:
                                    for j in range(len(place_used)): 
                                        print(watch_month,"월","\t",place_given[j],end="")
                                        print("\t",pg_total_list[j],"원")
                                    break
                        
                        print("*********************************************************************************************************")
                        print("입금 금액 합계:",total,"원")
                        break
        

            else:
                print("해당하는 달이 없습니다.")
                break   

 ########################################################## 
###2020112545배현지
    elif num == 8:
        out1 = 1
        out2 = 1
        while True:
            print("저희 용돈기입장을 이용해 주셔서 감사합니다. 별점을 남겨주시겠습니까?")
            print("1.Yes")
            print("2.No")
            yn = int(input(">"))
            if yn == 1:
                while True:
                    print("☆☆☆☆☆")
                    print("별점을 남겨주세요.(1점~5점 중에서 선택)")
                    star = int(input(">"))
                    if star <= 5:
                        for i in range(star):
                            print("★", end = "")
                        for i in range(5-star):
                            print("☆", end = "")
                            print()
                            print("감사합니다. 또 이용해주세요.")
                            out1 = 0
                            out2 = 0
                            break
                    else:
                        print("1점~5점 중에서 선택해주세요.")
                if out1 == 0:
                    break
            elif yn == 2:
                print("감사합니다. 또 이용해주세요.")
                out2 = 0
                break
            else:
                print("1번과 2번 중에 선택해주세요.")
        if out2 == 0:
            break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("메뉴는 1~7입니다.")
 ########################################################## 
