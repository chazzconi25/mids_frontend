import requests

# URL to which the POST request will be sent
url = 'https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery'

s = requests.Session()

alpha = input("What is your alpha?")

# Data to be sent in the POST request
payload = {
    'P_ALPHA': alpha,
    'P_LAST_NAME': '',
    'P_MICO_CO_NBR': '',
    'P_SECOF_COOF_SEBLDA_AC_YR': '2025',
    'P_SECOF_COOF_SEBLDA_SEM': 'FALL',
    'P_SECOF_COOF_SEBLDA_BLK_NBR': '1',
    'P_MAJOR_CODE': '',
    'P_NOMI_FORMATTED_NAME': '',
    'Z_ACTION': 'QUERY',
    'Z_CHK': '0'
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "content-length": "192",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "memory_sched_state=Initial; f5_cspm=1234; WSG$DRUWQ000$URL0=/ITSD/mids/druwq000$.startup; WSG$DRUWQ000$CAP0=Midshipmen_-_Query_Photos; WSG$DGDWQ000$URL0=/ITSD/mids/dgdwq000$.startup; WSG$DGDWQ000$CAP0=Academic_Information_-_Query; WSG$DGDWQ000$URL1=/ITSD/mids/dgdwq000$mids.startup?Z_CHK=0; WSG$DGDWQ000$CAP1=MIDS; WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; nmstat=c25f152e-3864-65e2-c27f-535c6d94e217; AMP_MKTG_075dfa7287=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRm5pbWl0endlYnByaW50LnVzbmEuZWR1JTNBOTE5MiUyRmFwcCUzRnNlcnZpY2UlM0RwYWdlJTJGVXNlcldlYlByaW50JTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMm5pbWl0endlYnByaW50LnVzbmEuZWR1JTNBOTE5MiUyMiU3RA==; AMP_075dfa7287=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1Y2JmNjljOC0wM2NkLTRkNTItOTdhNC1jZWE5NzE5NDJlNzIlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzI1Mzc1MTMzMjg2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyNTM3NTMyNDkzMSU3RA==; _gid=GA1.2.961660700.1727021097; BIGipServermids_prod=!t1FwLo3ihJ/1jEVHrP/1DhKiDM7x/s6C+w6n2Jlvfn+vPU/oeZBQGOCCc8FsAVac0tzD2MmMoIqkqvw=; _ga=GA1.2.543747182.1724942883; _ga_LY79N0FLBS=GS1.1.1727105632.36.1.1727105638.0.0.0; f5avraaaaaaaaaaaaaaaa_session_=IAGFLJLOFKDJLIBAEDGFPOJGGFHNABOIBKMNLNBGKDFGJOHBNEGDEDLEJBEDOPFOIEBDPLFFKHMGBGDHFBIANEAEMAONNPMAJNOEKAKEDAKMOBGNEJJJNFNHGCKEBANC; OAMAuthnCookie_mids.usna.edu:443=%2FpDhK%2Fssw0nKfVbGI8spg0yhPLLa%2Fa6CZ4lkkDIgIY%2FrCevKYwi%2FhGZ9zrHiafuooiYFncfwOCE%2FdAdtiqAYFYeL%2FfU6UM7rgyBy9J%2BMLWfNnNq2uY%2F8ouJnTUX8KwV1PuzPN7gxYd27TJCYgkvD6uEk51OdG1bYUGVKGym97%2FTdf%2FfKodwLFiGAO4Hyk1pA5w2RJ%2FvzKkITQVX5D%2F%2FvrC6otuNlgJ5FLrZJW7kdUaoWlDE%2BRCRj42PquKA3vnA6Ov%2BzdJPyrYaMRFGZO2l1IUydr1a8Rrg3bpUDyRQRsSbUB7Wvk60t%2BCiN5HVq%2BsLGNyqaQbQmIuPx%2BRXqQJKUH%2F4tvvA2JGnZ2sem7znu6%2F%2B6rWzNXAo9mch%2Fpyy85PX6VKyTDC8h2SWum%2FfGrc6QFozqegb9%2FpvFl2pkyDbP1bpxwE9VBJH2v0zM%2FNUTKB7YpNSzmmpCrbtigs9PMseOeyjpctYI%2FlqiMOL01MM8%2FvwVOQBQ9hPdyB3vL8jgGCyx7fi88YhGos2jiS9xWIoFpNyzPmnAEgSAiLUQCQyy0aS86HRUImpDaNDnAAqML2vkbhe65%2FYFILRMjMYjvnrDoA%3D%3D",
    "host": "mids.usna.edu",
    "origin": "https://mids.usna.edu",
    "referer": "https://mids.usna.edu/ITSD/mids/drgwq010$.startup",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}


response = s.post(url, headers=headers, data=payload, verify=False)
print(f'Status Code: {response.status_code}')
print(response.text)

