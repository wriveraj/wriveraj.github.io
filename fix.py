import re
with open(r"C:\Users\River\wriveraj.github.io\index.html","r",encoding="utf-8") as f:
    h=f.read()
old="I spent <strong>15 years running operations</strong>"
idx=h.find(old)
print("Found at:",idx)
if idx>=0:
    end=h.find("</p>",idx)
    h=h[:idx]+"In my current role and the last 8 years, I\u2019ve been managing field inventory for a medical device division in high-volume distribution. For me, numbers weren\u2019t abstract \u2014 a wrong move or allocation is high risk when it involves a surgical procedure."+h[end:]
    with open(r"C:\Users\River\wriveraj.github.io\index.html","w",encoding="utf-8") as f:
        f.write(h)
    print("Done")
else:
    print("Not found")

