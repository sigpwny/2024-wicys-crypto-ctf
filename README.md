# Fall CTF 2023 Challenge Repo

Put your challenge in chals/[category]/chalname

Flag format is sigpwny{}

Each challenge should have a challenge.yml so we can put on CTFd. Use [chals/crypto/add_one/challenge.yml](chals/crypto/add_one/challenge.yml) as a template.

If your chal needs to be deployed, create your Dockerfile (look to pwn chals for reference, or look to internal CTF repo for reference for your chal type) and add an entry to the [docker-compose.yml](docker-compose.yml) file.

## CI

As soon as you push to main, your challenge will be automatically added to ctfd according to your challenge.yml, and your chal will be auto deployed if it is writtein in docker-compose.yml.


## Lazy Development

Make sure your `Dockerfile` builds.

```bash
docker build .
```

Then make sure your challenge works.

```bash
docker run -p 0.0.0.0:1337:1337/tcp --rm -it $(docker build -q .)
```

You can read more notes [here](https://github.com/sigpwny/sigpwny-challenge-store#making-a-challenge-guide) - specifically step 4, "Deploying a challenge". 