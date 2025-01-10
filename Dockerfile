FROM python
WORKDIR /pwdgen
COPY code.py /pwdgen/code.py
COPY passwords.txt /pwdgen/passwords.txt
RUN pip install --no-cache-dir random
