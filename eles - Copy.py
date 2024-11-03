from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

driver = webdriver.Chrome()
driver.get("https://www.eles.si/prevzem-in-proizvodnja")

datelist = pd.date_range(start = datetime(2022, 1, 1), end = datetime(2024, 11, 3)).tolist()

for date in datelist:
    date_input = date.strftime("%d.%m.%Y")
    date_input_box = driver.find_element(By.CLASS_NAME, "datepicker")
    date_input_box.clear()
    date_input_box.send_keys(date_input)
    date_input_box.send_keys(Keys.TAB)
    pokazi_tabelo = driver.find_element(By.ID, "dnn_ctr1215_View_ctl00_btn_ShowTimedDataTabela")
    pokazi_tabelo.click()
    time.sleep(1)
    table = driver.find_element(By.ID, "dnn_ctr1215_View_ctl00_RadTabbedDataL_ctl00")
    df_table = pd.read_html(table.get_attribute('outerHTML'))
    df_table[0].index = pd.date_range(start=date, periods=24, freq='h')
    df_merge = pd.concat([df_merge, df_table[0]])

df_merge.to_csv("D:/Downloads/merge.csv")