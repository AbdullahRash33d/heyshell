patcher_src = "/usr/local/lib/python3.7/dist-packages/undetected_chromedriver/patcher.py"
with open(patcher_src, "r") as f:
    contents = f.read()
    contents = contents.replace("return urlretrieve(u)[0]",\
                     "return urlretrieve('file:///content/chromedriver_linux64.zip',"\
                     "filename='/tmp/chromedriver_linux64.zip')[0]")
with open(patcher_src, "w") as f:
    f.write(contents)
