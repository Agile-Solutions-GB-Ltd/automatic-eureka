# SpringBoot Source to Image API Example

## Credentials
```properties
spring.security.user.name=admin
spring.security.user.password=admin123
```

## Pack
```shell
pack build agileturret/sample-application-1 --builder paketobuildpacks/builder:base --env "BP_JVM_VERSION=17" --publish
```

## Fly
```shell
export FLYCTL_INSTALL="/home/devops/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"
flyctl auth login
flyctl launch --image agileturret/sample-application-1:latest
fly scale memory 1024
flyctl deploy
```


