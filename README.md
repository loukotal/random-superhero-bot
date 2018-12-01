# Random  superhero Mastodon bot

## Installation
I've had some trouble using the AWS Lambda environment - especially running the handler function. 
I found this article [link](https://medium.com/i-like-big-data-and-i-cannot-lie/how-to-create-an-aws-lambda-python-3-6-deployment-package-using-docker-d0e847207dd6) on how 
to deploy it using Docker.

I had trouble with running library `libffi-d7...` from `cffi` package that the Mastodon.py wrapper uses. What (I think) helped was putting the precompiled library to the root folder of the .zip file.

Another useful links for AWS Lambda and Python
- [AWS Lambda Deployment Package - official docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
- [Hassle-Free Python Lambda Deployment](https://joarleymoraes.com/hassle-free-python-lambda-deployment/)
- [Precompiled lambda packages](https://github.com/Miserlou/lambda-packages)
- [Zappa serverless python](https://github.com/Miserlou/Zappa)
- [Hosting platforms for bots](https://botwiki.org/resources/hosting-platforms/)
