FROM python
WORKDIR /pwdgen
COPY code.py /pwdgen/code.py
COPY passwords.txt /pwdgen/passwords.txt
CMD ["python", "/pwdgen/code.py"]