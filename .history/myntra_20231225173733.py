import requests
import json

url = "https://www.myntra.com/gateway/v2/search/dresses?f=Gender%3Amen%20women%2Cwomen&p=1&rows=100&o=49"

products = []

payload = {}
headers = {
  'authority': 'www.myntra.com',
  'accept': 'application/json',
  'accept-language': 'en-GB,en;q=0.7',
  'app': 'web',
  'content-type': 'application/json',
  'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pTXpnNU5qaGpZemt0TnpoaU15MHhNV1ZsTFdJMll6VXRNalpoT1dVNE9UQmtZVGd4SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzTVRRek9UUXhOak1zSW1semN5STZJa2xFUlVFaWZRLkE2X3hzZWRZS3A5OEJ2ZWU3aGUzQ1V2ci1NN0M1SjVVRGdUdlVVc3U1X3M=; _d_id=59d4cbc5-f5ec-4d4f-a49d-9b5b9ba59cfb; AKA_A2=A; _abck=CCC72BFE638D6B5FED92F762303E9FEC~0~YAAQhDkgF7FxoViMAQAAK3K0oAsgMCzj+oduJIQoymiQJtvDy7pPD2proQ1JMTxdHou7cHkCwQh+SgXIoY8ppvFv6GEW/4tqBeCyTEz0WkVOr5yIP7sf1J+nI6RJdcPe6w6pfhNJohTDZvxnUf7qJx/9SB9QWgqElwfpJf8ZfYf87+khSOjqhE4td0mAPg2Yo3bVw4vEHCs6hdcpHLj8hqVeHumYnocBdTNYcueNedpIfR9MzrWhBvpoYVQL65ct9+XCU8TVxuQAqeZ0QGc6tmG4ciRt5/mxtDJbx4FDbmdjnEjnMqWAL5gO1y5OESx8JntD6I6Ut50D+eSJ6fwnBdKPlk5wLu5mjKkhy3tn5YCDDHHzRRK18W1gD4MLXuohLtPPIPGJ8A8K5ejMqn3Gp3DzLoTYGlMJ~-1~-1~-1; ak_bmsc=285A13C853A120BCD8115FCCAE885143~000000000000000000000000000000~YAAQhDkgF7JxoViMAQAAK3K0oBZ7za76VV3z1eOcFezCGOaayz0OGHYdCLEaJSJSgqX7nQGVE7bc43OCifLrGUoG1sc7Q9nZGOMAVeDamZsKnrcQF1tV80u5GdrJLeU6f9o4jVMhk1CUTYwmlS2BrfsxX6qwqa1lEj/PhwSLqyCDFAzswb0rExcXXSKfd6zjr2GAu3XGzUdrzlyZ080j02ZPQe8r7vV14EFncKHAAnnhLrDV+eBGtwDmUSJIyax76jWTsKb2TPMc+yMZ4DpNFOQNygmy9yjEErkwbrspE+pHt7l273V73bew+t8eSB5a7fieYaAcYfIWxpaAkkBk5/Q1/cYcUSS48oaqUxt4UaCpLrdCfJbU7fvghssl1U8x/GYkGaJcWZCGKiiULMrmZyWAFobnc4HyYFyVioBig24jPQ==; bm_sz=46DC1255EA09707EC7527310B99AE33D~YAAQhDkgF7RxoViMAQAAK3K0oBYFfnh8yNG1yYPteP+LpQRC0p/HcX74m5Nif6CN/yEDPiBy5myCM2iUXKz1fHzm36saZkAQ9/324BlrYffaBklnUgUT3aR/OFVY2DT4cPHBEj3Sb2CFODeBQTOwT/1nynlrHMY0wk5N/ScSTVbTSfb1TRNwkoupegam2MhtbsXOH2gTk6E/Kk4EzFhrrDSxlaUs8o2KZmFrkw8zrG4iujAoKkb6ZM4hZjiFrBnYrtaMn3LNo3dp2+cLrU19qpfnl/wCtmbopC2eS+wbmdYd0d8=~3487795~3159353; mynt-eupv=1; _ma_session=%7B%22id%22%3A%22dcdc8d3f-1ecb-407b-8169-940ec11b35d7-59d4cbc5-f5ec-4d4f-a49d-9b5b9ba59cfb%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22%22%7D; mynt-ulc-api=pincode%3A752115; mynt-loc-src=expiry%3A1703504670070%7Csource%3AIP; _mxab_=config.bucket%3Dregular%3Bcheckout.donation%3Denabled%3BConvenience_fee_logged_out_user%3Denabled%3Bshl.desktop%3Denabled-3%3Bcoupon.cart.channelAware%3DchannelAware_Enabled; _pv=default; dp=d; microsessid=526; lt_timeout=1; lt_session=1; _xsrf=Wr2o6qwaM1Y41txd88NILIeOAUkj1rpM; x-mynt-pca=YDGwa9_xYX4UbeqGnE4v38KehVyB9wqqDBfilpUVPVAf7XJA1kWHOBNHzw8PEmnImVhvhrE8f2zI39WKg4YBrcBqIRgzxQxDatEWAF0j6i29iENZ2cLgMrCpud-0Eu_vspUKII4j0ocNUDXVf6CL24eHpF-kZ0caLkQAPjtsFiPiL_k_; user_session=Qy4xTki-1SOwqi-wq8xj9w.WyWxQa-3ILYDqLoVTgi13_uxnI2L-0RN216Sp2B7HhDyubdH2g0tPZMiUQXIuGukdYkfFV1tHuLwUyP-CbWmwvY-XIf93aBcq4Q9cfK6sHkjdlGQ2EQ-HpYg992l0VG2s0VyKcPC8pGsWo-rRp1SBQ.1703503230130.86400000.qv95Bk6EHWlJLKA8KZQ88Q9GDOJ9J7i3uXq6ETQDbns; bm_mi=18B132AB147C893D2F685134DD74DE8C~YAAQhDkgFwd2oViMAQAAp7u0oBar5ZeLOY1MSOpILTbebIUzYQoFMBDAF5GTORRWRoEYJncy7TBhKoLhufOXhnqWcpX0ARj+GO5oraTZRGFOS34OUvW3iMF3+CkoXY/P0L18OuKZaUX84DzoesUip4Z1dearuonmEudkw4ZahsewmtvgrKuEj902vX8mpf9hzAsiFiOeJshwx9O+C9FSLoMAbOho90Dz4B/zVXz2X9Eac85m7JpK05adF7R/ZgOzcimj0fBM2CfJan6kBUPuMDv4dhuzqbBCRNvIc6iL0DrU5ylQ84f6tW0FU5USGmsPx45uFkA=~1; utrid=fXF2XXYKcWMbXAQMS19AMCMyMDc1OTUwNTY3JDI%3D.f25f94e4babb23bc65b581ddf0ed83b2; bm_sv=E9A232C8963816823767BCCF28326398~YAAQhDkgFzZ2oViMAQAA2r20oBYgq9okM8m/X6+kPj7jvItima7raQ6lVCZ1T4rnKkWt0MgxFp7bdq0uB9BnHoeEmbm1xh/v2YPkdFwRz0vTIFxA01Qc3pcv+InV/5HsflSYrX9/Tbt6THkThRNLcSPqOoTB2StlS2ez3nvOU0zFnge8s3JY9lOFopR+ti9S733mwiAqSfOLmTXEK3bo20bvgbG8z1IuglNSWoIrUo1JcKg5ANgR2OGm/zJNsWAL~1; _abck=CCC72BFE638D6B5FED92F762303E9FEC~-1~YAAQ1/3UF3j9c1yMAQAAzBfMoAufmF3RbeRNXkBg4ujQvkmMAQKO63z2klrKN5gi9HKkfwBcH9rKZ4oWFdk1zQZi3+ZwphuC658pAEJnRPiSXI5KzEjNItBzAwwMEqW2KQIOXYG3PmqMdIdKHldxbdkd4U0+eKcGQs2WwVWEljsaiEgRI24uz2/Z4i75/8ccwniReTmWRt0uYpdx1FyVQgZPl79FcM+k3+hKZpsMUSpTikWwIATMvXF0Eos3p/B67cD/2Aqkour+/RRJHxoIL7QBbCV1Em5amkIIz/PIb6mSgoT1gWkC6lTVWNCfsuXg5/Gs+QFjR7MZYq1GTQXyRje6VQp0f8EUYONqCKT5IMhFKg3YZpKZrfEunJouTpZY0hvxtfTZiZxoxxOPrPlIuouPrk2G09Ko~0~-1~-1; bm_sv=E9A232C8963816823767BCCF28326398~YAAQ1/3UF3n9c1yMAQAAzBfMoBZwzlEF4dONe8HHWpeDiYNcEIqv9K+4topNrry/bCJT/RuWSi25xTKHzej6LE/rD9xJAj+Khd4vizA0LE4Hho5r/PZQpCs2vrfeecZdTovNDP2BTwCnz76HLfB6tUnvKkizObAjcHl5czuijJRvY/AHzgnWZ2VDd77UGzQ0KlIM6qnIIqsRFffQLhGtupXNnSAN/HsyvKo/TAH6xYhbciuDZCLInjHWim0x9UE/~1',
  'referer': 'https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen&p=2&rf=Discount%20Range%3A10.0_100.0_10.0%20TO%20100.0',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-location-context': 'pincode=752115;source=IP',
  'x-meta-app': 'channel=web',
  'x-myntra-app': 'deviceID=59d4cbc5-f5ec-4d4f-a49d-9b5b9ba59cfb;customerID=;reqChannel=web;appFamily=MyntraRetailWeb;',
  'x-myntraweb': 'Yes',
  'x-requested-with': 'browser'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
# data = []

for product in data['products'][0].:
    print(product)

print(products)
