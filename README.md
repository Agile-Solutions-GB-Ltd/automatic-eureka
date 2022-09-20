# automatic-eureka

Before starting to develop CICD pipelines it is worth understanding how code and applications are Built, Configured, 
Tested, Released, Packaged and Stored (B.C.T.R.P.S). Examples of which are covered in this project with the following 
use cases in mind: 

#### Continuous Integration (CI)
We use continuous integration (CI) to fetch source code from a git repository and then execute B.C.T.R.P.S where the 
release version is normally generated.

#### Continuous Delivery (CD)
If we have released an application that runs as a services, has an endpoint on the network that we can use, then we will 
probably want to use continuous delivery (CD) to run that application in some environment.

#### Continuous Integration (CI) for Utilities
We might want to use software packages for our pipelines as utilities, why? If we can develop and release our pipeline 
code utilities it allows us to control the use of these utilities, via the version, and also simplify and make our 
pipeline code more readable, for example `agileup` might be a useful python package that we have written.

```shell
tasks:
- plugin:
    configuration:
      id: script-executor
      version: 1.0.1
    options:
      script: |-
        agileup -E DEV --list 
      shtype: bash
    run_if: passed
```    

## Build



## Configure

The [12 Factor](https://12factor.net/) approach to configuration should always be followed. 

## Test/QA

**Testing** is used to verify the correct operation of software before it is released, testing can also be applied 
to a number of different operating systems, for example using GitHub actions we can define the following CI pipeline.

![](docs/images/Screenshot-2022-09-13-14-44-38.png)

![](docs/images/Screenshot-2022-09-13-14-46-52.png)

Here the "lint" step is used for code QA and the "Matrix: ci" step performs build and test once this is successful on the
target OS images then the release step is ran and the package is published.

**For Quality Assurance (QA)** you might consider adding https://codeql.github.com/ or https://www.sonarqube.org/features/quality-gate/ 
quality gates to your pipelines.  

## Release


## Package

Some examples of the relationships between packages, repositories and application entry points:

| Language | Package Type                            | Repository Type | Entry Point                               |
|----------|-----------------------------------------|-----------------|-------------------------------------------|
| Python   | [Poetry](https://python-poetry.org/)    | PyPi            | [tool.poetry.scripts]                     |
| Java     | [Maven/Jar](https://maven.apache.org/)  | Maven           | public static void main(String args[])    |
| C#       | [NuGet](https://www.nuget.org/)         | NuGet           | static void Main(string[] args)           |
| ANY      | [OCI](https://opencontainers.org/)      | Docker          | ENTRYPOINT ["SOME_COMMAND","ARG1","ARG2"] |

Meta-data used within a package specification normally also refers to dependencies that must be included for the 
application to work. For poetry python packages this is defined in the **pyproject.toml** file for example:

```ini
[tool.poetry.dependencies]
python = "^3.9"
click = "^8.1"
PyYAML = "^5.4.1"
pytest = "^7.1.3"
prettytable = "^3.3.0"
Fabric3 = "^1.14.post1"
```

## Store

From a software package point of view, the objective of continuous integration to build, test/QA and release a software 
project with a unique version number and save that package in a repository.

**A Repository** can be public, an example of a public repository containing a released package might 
be https://pypi.org/project/agileetc/ for python and https://hub.docker.com/repository/docker/agileturret/gocd-agent-ubuntu-20.04 for docker.

**A Repository** can be private an example of a private repository containing a released package might be:
1. https://jfrog.com/artifactory/
2. https://www.sonatype.com/products/nexus-repository
3. And solutions from your cloud vendor
