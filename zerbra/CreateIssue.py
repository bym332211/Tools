#coding=utf8
import http.client

conn = http.client.HTTPConnection("10.200.4.144")


product = "4"
module="0"
project=""
businessproj="线路".encode('utf-8')
bu="2"
type="codeerror"
severity="3"
channel="fenixao"
openedBuild="trunk"
assignedTo="baoyiming@lvmama.com"
title="python"
steps="aa"
story=""
task="0"
os=""
browser=""
mailto=""
keywords=""
files1=""
labels1=""
files2=""
labels2=""
case="0"
caseVersion="0"
result="0"
testtask="0"
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"product\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"module\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"project\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"businessproj\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"bu\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"type\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"severity\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"channel\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"openedBuild[]\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"assignedTo\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"title\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"steps\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"story\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"task\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"os\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"browser\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"mailto[]\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"keywords\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"files[]\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"labels[]\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"files[]\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"labels[]\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"case\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"caseVersion\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"result\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
          "Content-Disposition: form-data; name=\"testtask\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" \
          % (product, module, project, businessproj, bu, type, severity, channel, openedBuild, assignedTo, title, steps, story, task, os, browser, mailto, keywords, files1, labels1, files2, labels2, case, caseVersion, result, testtask )


headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "6f1e34b7-ea17-43c6-7e41-21f119171bdf"
    }

conn.request("POST", "/zentaopms/www/index.php?m=bug&f=create&productID=4&extra=moduleID%3D0", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))