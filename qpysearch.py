import threading
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.by import By

subject_name = ""
driver = None

root = tk.Tk()
root.geometry("850x400")
root.title("QPSearch")


def on_submit():
    global subject_name, driver
    subject_name = subject_entry.get()
    driver = webdriver.Chrome()
    driver.get("https://libportal.manipal.edu/MIT/Question%20Paper.aspx")
    thread = threading.Thread(target=traverse)
    thread.start()
    print(subject_name)


def traverse():
    web_table = {}
    tbody = driver.find_element(By.ID, 'ctl00_ctl00_chmain_MITContent_FileGridCS_gvFiles').find_element(By.TAG_NAME,
                                                                                                        'tbody')
    for ele in tbody.find_elements(By.TAG_NAME, 'tr'):
        try:
            link = ele.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a')
            web_table[link.get_attribute('id')] = link.text
        except Exception:
            pass

    for ele_id in web_table:
        if '..' in web_table[ele_id]:
            pass
        elif len(web_table[ele_id]) == 0:
            dummyElement = driver.find_element(By.ID, ele_id)
            trueElement = dummyElement.find_element(By.XPATH, '..').find_element(By.CSS_SELECTOR, "a[target='_blank']")
            if subject_name.lower() in trueElement.text.lower():  # and any(year in trueElement.text.lower() for year in ['2006', '2019']):
                print("Found file:", trueElement.get_attribute('href'))
                text_widget.insert(tk.END, trueElement.get_attribute('href') + "\n\n")

            else:
                continue
        else:

            if any(year in web_table[ele_id] for year in ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']):
                continue
            else:
                driver.find_element(By.ID, ele_id).click()
                traverse()
                driver.back()




time.sleep(1)

label = tk.Label(root, text="Enter Subject Name/Subject Code:")
label.place(relx=0.5, rely=0.1, anchor='center')

label = tk.Label(root, text="Copy/Paste the links below to view the PDFs:")
label.place(relx=0.5, rely=0.5, anchor='center')

text_widget = tk.Text(root, width=100, height=10)
text_widget.place(relx=0.5, rely=0.8, anchor='center')

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

subject_entry = tk.Entry(root)
subject_entry.place(relx=0.5, rely=0.2, anchor='center')

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.place(relx=0.5, rely=0.3, anchor='center')


root.mainloop()
