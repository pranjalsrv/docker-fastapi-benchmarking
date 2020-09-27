FROM ubuntu:20.10
COPY ab.exe /bin/
RUN echo "hello"
#ENTRYPOINT ["/bin/ab.exe", "-n", "100", "-c", "10", "http://127.0.0.1:80/"]
CMD /bin/ab.exe -n 100 -c 10 http://127.0.0.1:80/