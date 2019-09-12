# Automated-WhatsApp-Messaging
AWS Lambda deployed python tool that allows you to send automated WhatsApp messages to users, repeated at a specified time interval, using the TWILIO API and AWS Lambda.

*INSTRUCTIONS*

1) Navigate to app.__init__.py
  - Enter Twilio API credentials (TWL_SID and AUTH_TKN) after registering with www.twilio.com
  - Enter 'FROM' phone number (Note: if using sandbox environment, this will be provided by the twilio whatsapp messaging service)
2) Navigate to main.py
  - Add desired contacts (names and phone numbers--in any format since we use an API to validate--and reformat if necessary--the number)
  - Create the desired message bodies
3) After changing contents of above, replace main.py and __init__.py in "main_lamba_deployer.zip" with the modified files
4) Go to AWS and create a AWS Lambda instance; upload the .zip file with the handler set to main.main
5) To automatically send messages at a particular time of the day, create a CloudWatch event in your Lambda function (e.g. schedule expression: cron(30 1 * * ? *))
