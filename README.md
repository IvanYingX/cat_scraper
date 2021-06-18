# cat_scraper

Just a few important notes:
- Don't forget the credentials! boto3 will look at your ~/.aws/ directory to find the credentials and the configurations
- If that doesn't work, type pip install awscli. Then type aws configure and fill the asked data
- If that still doesn't work, you can go to AWS CLI webpage to download their CLI commands, and they will be installed in your path, so the aws configure command can be used from your terminal
- Try blocking public access unless you need it
- If you are working in teams, use the same account, and set up different IAM Users, each user will get a different ID and key, but all will share the same resources
- If you want a quick solution, refer to the document in the repo about making objects public
