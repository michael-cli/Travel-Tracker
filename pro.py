import time
import firebase_admin
import mysql.connector
from firebase_admin import credentials
from firebase_admin import db
from selenium import webdriver
from mysql.connector import errorcode
from mysql.connector import Error

# webdriver path set 
browser = webdriver.Chrome("F:/Michael/chromedriver.exe") 
  
# To maximize the browser window 
browser.maximize_window() 

#Firebase Config
cred = credentials.Certificate('jfile.json')
    # Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bdata-60608.firebaseio.com/'
     })           
 

global i
i=0

def Estimate():
    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
    ref = db.reference('210/source')
    src = ref.get()
    print("Source: ",src)

    try:
        ref1 = db.reference('stops_210')
        bstop = ref1.order_by_key().get()
        for key,value in bstop.items():
            print('{0}'.format(value))
            des = value
            if (des=="kandivali telephone exchange"):
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/kte')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/kte')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/kte')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("Finally 1")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    

            if (des=="ambedkar hospital"):
                #//*[@id='sb_ifc50']/input
                #//*[@id="sb_ifc50"]/input
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/ambed hosp')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/ambed hosp')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/ambed hosp')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("finally 2")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="kandivali railway station"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/krs')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/krs')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/krs')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("Finally 3")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")



            if (des=="balbharti college"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/balbharti')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/balbharti')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/balbharti')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("finally 4")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")


            if (des=="jain mandir kandivali"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/jain mandir')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/jain mandir')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/jain mandir')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                    print("Estimated Time: ",tme.text,'\n')   
                    ref1 = db.reference('210/jain mandir')
                    ref1.set(tme.text)
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("finally 5")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="milap talkies"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/milap talkies')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/milap talkies')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/milap talkies')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("finally 6")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="nl vidyalaya"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/nl vidyalaya')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/nl vidyalaya')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/nl vidyalaya')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("finally 7")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="choksi hospital"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/choksi hosp')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/choksi hosp')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/choksi hosp')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    print("finally 8")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="orlem church malad"):
                time.sleep(3)
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd and Marve Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/orlem church')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/orlem church')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/orlem church')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                    print("Estimated Time: ",tme.text,'\n')   
                    ref1 = db.reference('210/jain mandir')
                    ref1.set(tme.text)
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    
                    print("finally 9")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            '''if (des=="evershine nagar"):
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/evershine ngr')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/evershine ngr')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/evershine ngr')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="kachpada"):
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/kachpada')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/kachpada')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/kachpada')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="dmart shopping malad"):
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/dmart shopping')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/dmart shopping')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/dmart shopping')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")

            if (des=="malad depot"):
                a = browser.find_element_by_xpath("//*[@id='sb_ifc50']/input")
                a.send_keys(src)
                b = browser.find_element_by_xpath("//*[@id='sb_ifc51']/input")
                b.send_keys(des)
                time.sleep(3)
                #//*[@id="directions-searchbox-0"]/button[1]
                browser.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()
                time.sleep(3)
                try:
                    try:
                        route1 = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route1: ",route1.text)
                        if(route1.text=="SV Rd"):
                            print("Route 1 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/Malad depot')
                            ref1.set(tme.text)
                            time.sleep(4)
                    except:
                        print("Route 1 Not Found")

                    try:
                        route2 = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route2: ",route2.text)
                        if(route2.text=="SV Rd"):
                            print("Route 2 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-1']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text)   
                            ref1 = db.reference('210/Malad depot')
                            ref1.set(tme.text)
                    except:
                        print("Route 2 Not Found")

                    try:
                        route3 = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[2]/h1[1]/span")
                        print("Route3: ",route3.text)
                        if(route3.text=="SV Rd"):
                            print("Route 3 Selected")
                            tme = browser.find_element_by_xpath("//*[@id='section-directions-trip-2']/div[2]/div[1]/div[1]/div[1]/span[1]")
                            print("Estimated Time: ",tme.text,'\n')   
                            ref1 = db.reference('210/Malad depot')
                            ref1.set(tme.text)
                    except:
                        print("Route 3 Not Found")

                except:
                    print("Exception")
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")
                    time.sleep(2)

                finally:
                    browser.get("https://www.google.com/maps/dir///@19.2052673,72.8410227,15z/data=!4m2!4m1!3e0")'''

    except Exception as e:
        print("Error reading data from Firebase", e)
    finally:
            print("Completed") 

while True:
    try:
        Estimate()
        i+=1
        print("Count: ",i)
        print("Close\n\n")
    except:
        print("Exception")
