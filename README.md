# Random  superhero Mastodon bot
The bot: https://botsin.space/web/accounts/89547
## Overview
This is a fun project created to get my hands on and try out AWS - namely Lambda function. It uses `textgenrnn` library to generate new superhero names and dataset of superheroes [link](https://www.kaggle.com/claudiodavi/superhero-set#heroes_information.csv). It was trained on google colab with 10 epochs (just arbitraty number I chose, honestly).

## Installation
I've had some trouble using the AWS Lambda environment - especially running the handler function. 
I found this article [link](https://medium.com/i-like-big-data-and-i-cannot-lie/how-to-create-an-aws-lambda-python-3-6-deployment-package-using-docker-d0e847207dd6) on how 
to deploy it using Docker.

I had trouble with running library `libffi-d7...` from `cffi` package that the Mastodon.py wrapper uses. What (I think) helped was putting the precompiled library to the root folder of the .zip file.

Another problem I encountered was putting the model in the Lambda function. Since textgenrnn uses keras and tensorflow. TF package is very large and Lambda restriction for the function code is 250 mb unzipped when uploaded through s3. So the first workaround was to generate n (in our case 10k) examples and just randomly choose 5 of them, instead of generating them everytime the Lambda function is run. 

Another useful links for AWS Lambda and Python
- [AWS Lambda Deployment Package - official docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
- [Hassle-Free Python Lambda Deployment](https://joarleymoraes.com/hassle-free-python-lambda-deployment/)
- [Precompiled lambda packages](https://github.com/Miserlou/lambda-packages)
- [Zappa serverless python](https://github.com/Miserlou/Zappa)
- [Hosting platforms for bots](https://botwiki.org/resources/hosting-platforms/)
- [Serverless dl/ml in production](https://blog.waya.ai/deploy-deep-machine-learning-in-production-the-pythonic-way-a17105f1540e)
- [Serving TF predictions with Lambda and Python](https://medium.com/tooso/serving-tensorflow-predictions-with-python-and-aws-lambda-facb4ab87ddd)

## Possible improvements
I can an improvement in actually generating the output when the function is run - that would mean, I think, to build tensorflow and other big libraries that are being used from source. Or maybe developing simple REST api (maybe using Flask?) on EC2 and calling it from the Lambda function.