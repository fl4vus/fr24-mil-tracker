import main as main

print("WHEN PROMTED, TYPE 'y' FOR YES, ALL OTHER INPUTS ARE NO")

recurring = str(input("Do you want program to run in a periodic loop? "))

match recurring:
    case 'y':
        total_time = int(input("Total time to run? (in seconds) "))
        sleep_timer = int(input("Time b/w each iteration: "))
        
        import time
        start_time=time.time()
        end_time=time.time()-start_time

        while  end_time < total_time:
            #print(time.time())
            main.main()
            end_time=time.time()-start_time
            time.sleep(sleep_timer)
    
    case 'Y':
        total_time = int(input("Total time to run? (in seconds) "))
        sleep_timer = int(input("time b/w each iteration: "))
        
        import time
        start_time=time.time()

        end_time=time.time()-start_time

        while  end_time < total_time:
            #print(time.time())
            main.main()
            end_time=time.time()-start_time
            time.sleep(sleep_timer)
    case _:
        #print(time.time())
        main.main()       

    

    



