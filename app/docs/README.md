# Singularity Registry Documentation

Hello there! It's so great that you want to use Singularity Registry. Let's get started. 

## Introduction
This section covers rationale, background, and frequently asked questions.

 - [Introduction](introduction.md): Covers some background and basic information.
 - [Use Cases](use-cases.md): a few examples of when Singularity Registry is useful
 - [Frequenty Asked Questions](faq.md): Quick answers to some questions you might have on your mind.


## Deploy a Registry
This section is going to cover installation, which means configuration of a Docker image, building of the image, and then starting your image with other services (docker-compose) to run your registry.

 - [install](install.md): configure, build, and deploy your registry.
 - [setup](setup.md): setting up and registering the running application.
 - [credentials](credentials.md): User accounts and credentials for using the client.
 - [plugins](plugins/README.md): Details about available plugins, and how to configure them.

## Use a Registry

 - [sregistry Client](client.md): A client provided by Singularity Python to push, pull, list, and delete.
 - [Singularity usage](singularity-client.md): The Singularity development branch has functionality to use your registry too.


@vsoch wants [your input!](https://www.github.com/singularityhub/sregistry/issues) This registry is driven by desire and need for clusters small and large, so if you don't tell me what you want, how will I know that you want it?

