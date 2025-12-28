FROM alpine:latest
RUN apk add --update python3 


WORKDIR /app 
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "notebook.py" ] 
