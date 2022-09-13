# automatic-eureka

Before starting to develop CICD pipelines it is worth understanding how code and applications are packaged first and so 
we provide some examples in this project to help DevOps team members on getting started. Software packages can be useful 
in 2 areas, when thinking of CICD pipelines we might:

* We use software packages to fetch applications or code from a specific repositories that have a certain version that 
we want to build, test/qa and release via continuous integration (CI) and then optionally delivery to some target environment 
under continuous delivery (CD).
* We might want to use software packages for our pipelines, why? If we can develop and release our pipeline code utilities 
it allows us to both control the release of these utilities as well as providing a PLAN B in that we can always perform 
pipeline operations outside of using our favorite CICD platofrm.

To clarify the second point if we define a pipeline tasks as below using our python utility package we can execute the command
*mypythonutility -E DEV --list* making both the pipeline code more readable and also allowing us to future develop the python 
package without making significant changes the pipeline code itself.

```shell
tasks:
- plugin:
    configuration:
      id: script-executor
      version: 1.0.1
    options:
      script: |-
        mypythonutility -E DEV --list 
      shtype: bash
    run_if: passed
```    

**We can then also at anytime that is needed for development, testing our production support execute the command mypythonutility -E DEV --list !**

## What is inside a software package?

When referring to a software package that is runnable, i.e. not a library:
 
1. Any code or data that the developer of the package thought is needed to correctly use the software. The layout and 
contents of the package also depends on the package type being used which is often dependent on the programing langauge used.
2. The current version of the package.
3. Some meta-data on the source code repository, author and other useful information.
4. An entry point or points for the application or script being used.




