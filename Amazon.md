# Download files from an S3 Bucket using *requests*

This small step by step tutorial will guide you to:

- Create an Amazon S3 bucket
- Make public the files in the bucket
- Upload your files
- Download the files from the bucket

## Create an Amazon S3 bucket

The first thing you have to do is creating an Amazon Web Service, so go to the [AWS webpage](https://aws.amazon.com/).Click on the 'Sign In to the Console' button on the top right corner, and, in the next window, click on the 'Create a new AWS account'. <br>
Follow the steps and in the search bar, type 'S3', and click on the first option:

![XOR gate](images/amazon_search.PNG)

In the next window, click on 'Create bucket':

![XOR gate](images/Create_bucket.PNG)

Set a name for your bucket, and choose a region (any from US usually works fine). Disable the 'Block all public access' option:

![XOR gate](images/disable.PNG)

Once you created it, you can access to it in the bucket list, now you just need to make it public.

## Make public the files in the bucket

To make the objects public, go to http://awspolicygen.s3.amazonaws.com/policygen.html, which will help you create the necessary policy.<br>
- In 'Select Type of Policy' select S3 Bucket Policy. 
- In 'Principal' type ' * '
- In 'Actions' select 'Get Object'
- In 'Amazon Resource Name (ARN)' type arn:aws:s3:::{your_bucket_name}/*
- Press Statement
- Press Generate Policy and copy the text
  
![XOR gate](images/Policy.PNG)

Go back to your bucket and go to the Permissions tab. In 'Bucket Policy' click Edit. Paste the text you copied and save changes.<br> 
Now your bucket is publicly accesible, and anyone can download your files. 

## Upload your files

Uploading files to a bucket is quite straightforward. Just go to the bucket and click Upload:

![XOR gate](images/Upload.PNG)

Select the files in 'Add files' or 'Add folder' and then click Upload

## Download the files from the bucket

In your bucket, select the file you want to download, and copy the Object URL.

![XOR gate](images/URL.PNG)

Open a python editor or notebook and use the requests library to download the image from the URL you just copied. Something like this:
```
import requests
# Change this with your URL
url = f'https://testbucket1905.s3.amazonaws.com/AICore.png'
response = requests.get(url)
with open('image.png', 'wb') as f:
    f.write(response.content)
```

And that's it, you should be able to see the file in the same working directory.

You might need to download several files, but taking the URL for all files will defeat the purpose of creating a pipeline. To solve that, you can use the library boto3 and get a list with the contents of your bucket. 

But before that, you have to configure your authentication credentials. Download the AWS CLI here: https://aws.amazon.com/cli/. You also need an access key ID and secret access key. To obtain them, follow these steps:
- Open the IAM console at https://console.aws.amazon.com/iam/

- On the navigation menu, choose Users.

- Choose your IAM user name (not the check box)

- Open the Security credentials tab, and then choose Create access key.

- To see the new access key, choose Show. Your credentials resemble the following:
```
    Access key ID: AKIAIOSFODNN7EXAMPLE

    Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

- To download the key pair, choose Download .csv file. Store the .csv file with keys in a secure location.

Now, go to the terminal and type
```
aws configure
```
Fill the fields with your data, and you are ready to use boto3

```
import boto3
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('Bucket_name')
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object)
```
This will print all the objects in your bucket. Now you can play around, and get a list of all URLs, so anyone can download your images.