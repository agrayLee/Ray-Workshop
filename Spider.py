import requests
from datetime import date, timedelta
from bs4 import BeautifulSoup

# 设置Cookie
cookies = {
    "sidebarStatus": "1",
    "dtCookie": "v_4_srv_1_sn_179EAFBE2531D535AC7123975B2F3B95_perc_100000_ol_0_mul_1_app-3Ab18e72331efb9884_1",
    "rxVisitor": "1679302713921J76I97OK85I39RHG1V4QF2MO22PK7P7G", " "
    "vuex": "{%22configuration%22:{%22configurationBuildingIdList%22:[]%2C%22configurationProjectIdList%22:[]}}",
    "dtSa": "-",
    "dtLatC": "2",
    "rxvt": "1688953043632|1688950602813",
    "dtPC": "1$551242710_129h-vWNWHFMLBFKMKKHMSMTUKRCHHMABKHKHO-0e0",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2218a0643534dbb4-01d1a5663075fde-7c54647d-2073600-18a0643534e10cd%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhMDY0MzUzNGRiYjQtMDFkMWE1NjYzMDc1ZmRlLTdjNTQ2NDdkLTIwNzM2MDAtMThhMDY0MzUzNGUxMGNkIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218a0643534dbb4-01d1a5663075fde-7c54647d-2073600-18a0643534e10cd%22%7D",
    "_bl_uid": "I1lzmm6e44hm7CipphR3znnepywd",
    "azure_ad_token": "eyJ0eXAiOiJKV1QiLCJub25jZSI6InYzTHZneU1uTHZOSzdDUnVQYmVlM3RGX0Vka1BCaXdYZm5MQUFjdmh6QlUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8wN2M5MWI3ZC05ODAyLTRiNTAtYmE2MC03YmVjNTg2ODFmZGEvIiwiaWF0IjoxNjk1NzIyNDQ1LCJuYmYiOjE2OTU3MjI0NDUsImV4cCI6MTY5NTcyNzE2MCwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsidXJuOnVzZXI6cmVnaXN0ZXJzZWN1cml0eWluZm8iXSwiYWlvIjoiQVRRQXkvOFVBQUFBclpFR3YzSHhLeW9DbnBubHNReTExTUlqNGR4R3hkQnFyd0JQa3FySDE3Nk42YnpOTEVpVmVuNURjVTdHYngwRSIsImFtciI6WyJwd2QiLCJyc2EiXSwiYXBwX2Rpc3BsYXluYW1lIjoiS1BMIEtlcnJ5UGx1cyBBZG1pbiBQb3J0YWwiLCJhcHBpZCI6IjQxOTYwNzdhLTk2ODMtNDMxNi04ODg4LWM0ZmFjMzVhZTJhNCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiYzU5MzUwM2ItODgwNy00ZDU3LWIwZGQtZGRlMmUyMGVjNDRlIiwiZmFtaWx5X25hbWUiOiJMaSIsImdpdmVuX25hbWUiOiJSYXkiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxNzUuNDIuMjIuMjE3IiwibmFtZSI6IlJheSBMaSIsIm9pZCI6Ijg2MTkyNjdjLWMxMjktNDcyOS05NWFjLWZhOTk0ZjY2NGQ5ZSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0yODIyNjkwMjIyLTM2NjEzMDI2MjQtMTA0MzA1NDcxNC0xNDUxNCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMjcxRUIyRjE0IiwicmgiOiIwLkFYSUFmUnZKQndLWVVFdTZZSHZzV0dnZjJnTUFBQUFBQUFBQXdBQUFBQUFBQUFCeUFHYy4iLCJzY3AiOiJVc2VyLlJlYWQgcHJvZmlsZSBvcGVuaWQgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsiZHZjX21uZ2QiLCJkdmNfY21wIiwiZHZjX2RtamQiLCJrbXNpIl0sInN1YiI6IkIzcC03cWkxWlJNcWZDY3JxNlRlMWNQQTFQVmJ5bjViQTIySGhPZWpIM1UiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiIwN2M5MWI3ZC05ODAyLTRiNTAtYmE2MC03YmVjNTg2ODFmZGEiLCJ1bmlxdWVfbmFtZSI6IlJheS5MaUBrZXJyeXByb3BzLmNvbSIsInVwbiI6IlJheS5MaUBrZXJyeXByb3BzLmNvbSIsInV0aSI6IjJpSV9ObVNIVlVLS2VjeDZtRGtPQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiUExfQzJhN0FLVTZ4UlJsTDRqeGFSMkFubnJVTEo0dElWQkkxcEVwakdIZyJ9LCJ4bXNfdGNkdCI6MTU0MTY2NTAyN30.k9VdiiIBRKPLw1BK6KS0p06s59GsT3fN9uiN50YOnVe_f0V8SdoxOsyZDuQSeO3FV27DOd6eHWCztTiM7My6i6yXuj5NC-SCtV2_2JN6-8lutUt7vE703PjNfpbzpt9l_FnX-rJKZ6qcQbg2gjVeFO5BWoNcMcJhY5usc7PD815DdLUQO4bbXRq-6AR0IC23Kn8Jb6WvSNzPmHnvTS8ST7VT2uktmaP9qQxGpdaXlhZIEK1reEVSd8nzG_3EaVP-BWIDtPPgwK_PiR91Cny6rjVQNQNsDRZbWmqfCsqjcKg9ytym8ej1qBfzV2V9wYscj868EJIluaSGr_2H4CywNQ",
    "Admin-Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTYzMjc1NDYsInVzZXIiOnsidXNlcklkIjo1MjcsImZyb21UeXBlIjoiUyIsImxvZ2luQWNjb3VudCI6InJheS5saUBrZXJyeXByb3BzLmNvbSIsIm5pY2tOYW1lIjoi5p2O5Lic5aiBIiwicm9sZXMiOiItIiwibW9kdWxlcyI6IlBST1BNQU5fQVBQLEZJTkFOQ0VfQURNSU4sQ0lQX0FQUCxLRVlTVE9ORV9BUFAiLCJzdXBlckFkbWluIjpmYWxzZX0sInVzZXJfbmFtZSI6IkxvZ2luVXNlcih1c2VySWQ9NTI3LCBmcm9tVHlwZT1TLCBjSWQ9bnVsbCwgbG9naW5BY2NvdW50PXJheS5saUBrZXJyeXByb3BzLmNvbSwgbmlja05hbWU95p2O5Lic5aiBLCBwaG9uZU51bWJlcj1udWxsLCByb2xlcz0tLCBzY29wZXM9bnVsbCwgY29tcGFueUlkcz1udWxsLCBwcm9qZWN0SWRzPW51bGwsIGJ1aWxkaW5nSWRzPW51bGwsIG1vZHVsZXM9UFJPUE1BTl9BUFAsRklOQU5DRV9BRE1JTixDSVBfQVBQLEtFWVNUT05FX0FQUCkiLCJqdGkiOiIxZjMwYzA2YS1lMDBiLTQyNWItYmYyNC0wZDdjNzU4MjFiNzIiLCJjbGllbnRfaWQiOiJTLXdlYkFwcCIsInNjb3BlIjpbImFwcCJdfQ.iFi37-k4TtXjmtC_EVGcVALdOJRiMHuo_pGiDJfK8jhB4gwRPfjOv1jMliT87Up44KKQI3BMVaLkmjZNG4OQuNF8_YUhJDCZoBZgXPCAuUQOo9Y_GtWq5ZZSM3H3uCOZIIUhL29it6IzKptK3vx5uguEKabb3cqVfhQl-DYZfBva3bIxrpX2ptrFiYiESW3KSxQXZ9tr4BExflUMpnGpGIJdwNBexR-rr3xjaKfoCT5kmXys3CdP75o1MD89lZqyOcw2b7A92BfUBYowX13_mxyZ5aRq1-HTM6XKw9LmDAcULF_LumytoeoquH3q0q2AmM8GK2tGWoa8an0WZCVYIQ",

    # 添加其他Cookie
}

# 获取当前日期的前一天
today = date.today()
yesterday = today - timedelta(days=1)
start_date = yesterday.strftime("%Y-%m-%d")
end_date = yesterday.strftime("%Y-%m-%d")

# 构造请求参数
params = {
    "startDate": start_date,
    "endDate": end_date,
}

# 发送请求
url = "https://admin.kerryplus.com/sales/sale"
response = requests.get(url, params=params, cookies=cookies)
if response.status_code == 200:
    html = response.text
    # 解析HTML
    soup = BeautifulSoup(html, "html.parser")
    # 判断日期输入框是否存在
    date_inputs = soup.find_all("input", class_="nt-calendar-range-picker-input")
    if len(date_inputs) >= 2:
        # 输入开始日期和结束日期
        start_date_input = date_inputs[0]
        end_date_input = date_inputs[1]
        start_date_input["value"] = start_date
        end_date_input["value"] = end_date

        # 点击搜索按钮
        search_button = soup.find("button", class_="ant-btn ant-btn-primary")
        if search_button:
            search_button.click()

            # 提取数据
            tenant_name = soup.find("td", attrs={"key": "tenantName"})
            entry_time = soup.find("td", attrs={"key": "entryTime"})
            total_amount = soup.find("td", attrs={"key": "totalAmount"})

            # 打印爬取的数据
            if tenant_name and entry_time and total_amount:
                print("租户名称:", tenant_name.text)
                print("日期:", entry_time.text)
                print("营业额:", total_amount.text)
            else:
                print("未找到数据")
        else:
            print("搜索按钮未找到")
    else:
        print("日期输入框未找到")
else:
    print("请求失败，状态码:", response.status_code)