from selenium import webdriver

web = webdriver.Chrome()
web.get('https://www.cwb.gov.tw/V7/observe/real/NewObs.htm#self')

web.find_element_by_link_text('基隆市').click()
print(web.find_element_by_xpath('//div[@style=""]//tbody').text)

web.find_element_by_link_text('臺北市').click()
print(web.find_element_by_xpath('//div[@style="display: block;"]//tbody').text)

web.close()
