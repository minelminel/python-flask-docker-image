### Build

For the purpose of this outline, the following items are assumed:
  'flaskapp' is the IMAGE
  'latest' is the version

```bash
# 'tags' are employed for revision specification and can be defaulted to 'latest'
# build image (with tag) 'image':'tag' , in current dir

docker build -t webinar-flask:v1 .
```

```bash
# -d is 'daemon', -p is 'port' <arbitrary>:<script specified>, 'image':'tag'
# 'it' flag not present in some configs (?)
# outputs hash

  docker run -it -d -p 5000:5000 webinar-flask:v1
```
#### at this point, http://localhost:5000 should be live, running locally

```bash
# view images
docker images

# processes
docker ps
```

```bash

```

```bash

```
