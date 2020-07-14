import selenium.webdriver as drivers
import pickle
import os

from selenium.webdriver.support.ui import Select

import time,datetime


class auto_x:
    def __init__(self, user, password):
        try:
            self.driver = drivers.Chrome()
        except:
            self.driver=drivers.Edge()
        self.click_btn = "//input[id='btnOK']"


        
        # self.user=["17011010204","buwangchuxin"]
        self.user = user
        self.password = password

    
    def click_ok(self):
        btn_ok = self.driver.find_element_by_id("btnOK")
        # self.driver.switch_to_default_content()
        btn_ok.click()
        time.sleep(0.5)

    def alerts(self):
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except:
            print("点击")
        finally:
            self.driver.switch_to_default_content()

    def get_in(self):
        self.driver.get("http://202.206.48.111:8020/main.aspx")
        self.put_i()
        time.sleep(15)

        self.driver.switch_to_frame("leftFrame")
        time.sleep(1)
        aa = self.driver.find_element_by_class_name("MM")
        aa.find_element_by_link_text(u"网上评教").click()
        time.sleep(1)

        self.driver.switch_to_default_content()

        self.driver.switch_to_frame("main")
        self.driver.find_element_by_id("btnLoad").click()
        time.sleep(3)
        self.driver.switch_to_default_content()

    def enter(self):
        to_flag = True
        while True:
            f1 = self.full()
            if not f1:
                break
            else:
                flag = self.nextpage()
                time.sleep(1)
                if not flag:
                    print(
                        "============================执行完毕,已退出==============================")
                    to_flag = flag
                    break
                print("=======已翻页======")

        if to_flag:
            self.driver.switch_to_frame("main")
            self.driver.find_element_by_link_text(u"评价").click()
            self.driver.switch_to_default_content()
        return to_flag

    def option(self):
        self.driver.switch_to_frame("main")
        trs = self.driver.find_elements_by_tag_name("tr")

        for tr in trs:

            # select.click()
            try:
                select = Select(tr.find_element_by_tag_name("select"))
                n = select.select_by_index(1)
                print("选择成功")
            except:
                continue

        self.click_ok()
        self.alerts()
        time.sleep(0.5)
        self.driver.switch_to_default_content()

    def back(self):
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text(u"网上评教").click()
        time.sleep(1)
        self.driver.switch_to_default_content()

    def full(self):
        self.driver.switch_to_frame("main")
        try:
            self.driver.find_element_by_link_text(u"评价")
            return False
        except:
            return True

        finally:
            self.driver.switch_to_default_content()

    def nextpage(self):
        myflag = False
        self.driver.switch_to_frame("main")
        try:
            self.driver.find_element_by_link_text(u"下一页").click()
            print("正在翻页")
            myflag = True
        except:
            print("评价完毕，即将退出")
            myflag = False
            self.close()

        finally:
            time.sleep(1)
            if myflag:
                self.driver.switch_to_default_content()

            return myflag

    def put_i(self):
        users = self.driver.find_element_by_id("txtUserName")
        users.send_keys(self.user)
        password = self.driver.find_element_by_id("txtPwd")
        password.send_keys(self.password)

    def get_page(self):
        self.get_in()
        while True:
            flag = self.enter()
            if not flag:
                print("退出成功")
                break
            self.option()
            time.sleep(1)
            self.back()
            print("=============================此老师已经评价完毕=============================")

    def closed(self):
        self.driver.close()
        print("已完成，退出成功")


if __name__ == "__main__":

    user = input("输入教务处账号:\n")
    password = input("输入教务处密码:\n")
    t_start = datetime.datetime.now()
    test = auto_x(user, password)
    test.get_page()
    test.closed()

        
    t_end = datetime.datetime.now()


    second=(t_end-t_start).seconds
    print("一共用了：%f分钟"%(second/60))

