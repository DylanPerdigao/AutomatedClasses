from msedge.selenium_tools import Edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import EdgeOptions


URL= 'https://ucstudent.uc.pt/login'
LOGIN_EMAIL= 'uc...@student.uc.pt'
LOGIN_PASSWORD= 'yourpassword'

def main():
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('headless')
    edge_options.add_argument('disable-gpu')
    driver = Edge(executable_path='msedgedriver.exe', options=edge_options)
    driver.get(URL)
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/form/div[1]/div/input')))

    email_input= driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[1]/div/input')    
    pass_input= driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[2]/div/input')    
    email_input.send_keys(LOGIN_EMAIL)
    pass_input.send_keys(LOGIN_PASSWORD)
    
    login_button= driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div/form/div[3]/button')    
    login_button.click()

    try: wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div/div[7]/div')))
    except:
        driver.quit()
        return '\nbro, you dont even are having a class, get a life nerd!'
    
    try:
        try: enter_class_button= driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div[6]/div/div[8]/button[1]')
        except: enter_class_button= driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div[7]/div/div[8]/button[1]')
        enter_class_button.click()
    
        while True:
            try: 
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/div/div[3]/div/button[2]')))
                break
            except: continue

        online_presence= driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/div/div[3]/div/button[2]')    
        online_presence.click()

        while True:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/footer/button[2]')))
                break
            except: continue

        presence_check= driver.find_element_by_xpath('/html/body/div[2]/div[2]/footer/button[2]')    
        presence_check.click()
        
        online_presence= driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/div/div[4]/div/div[3]/div/button[2]')    
        
        while str(online_presence.value_of_css_property('background-color'))!='rgba(3, 164, 121, 1)': continue
        driver.quit()
        return '\ndone bro, you checked your presence, you can go back to sleep now'
    except: 
        driver.quit()
        return '\ndoesn\'t exist a class running right now bro'

if __name__=='__main__':
    print(main())
