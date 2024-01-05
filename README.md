# selenium-web_scraping-live
scraping top 10 trending videos on Youtube using selenium and AWS Lamda

Step 1 - Launch the repository on Replit
* Attempt to scrape the page using requests & Beautiful Soup
* References:
    * YouTube trending feed: [https://www.youtube.com/feed/trending](https://www.youtube.com/feed/trending) 
    * Beautiful soup tutorial: [https://blog.jovian.ai/web-scraping-u...](https://ankit-pratap-singh.medium.com/web-scraping-using-python-and-beautifulsoup-adf43cbdb816) 


Step 2 - Extract information using Selenium
* Install selenium and create a browser driver
* Load the page and extract information
* Create a CSV of results using Pandas
* References:
    * Selenium tutorial: [https://www.browserstack.com/guide/py...](https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test)
    * Pandas tutorial: [https://jovian.ai/learn/data-analysis...](https://jovian.com/learn/data-analysis-with-python-zero-to-pandas/lesson/lesson-4-analyzing-tabular-data-with-pandas)


Step 3 - Set up a recurring job on AWS Lambda
* Create an AWS Lambda Python function
* Deploy a sample script and observe the output
* Add layers for Selenium and Chromium
* Set up recurring job using AWS CloudWatch
* References:
    * Python on AWS Lambda tutorial: [https://stackify.com/aws-lambda-with-... ](https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/)
    * Chromium & Selenium on AWS Lambda: [https://dev.to/awscommunity-asean/cre...](https://dev.to/awscommunity-asean/creating-an-api-that-runs-selenium-via-aws-lambda-3ck3)
    * Recurring AWS Lambda functions: [https://docs.aws.amazon.com/lambda/la... ](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html)

Step 4 - Send results over email using SMTP
* Create email client using smtplib
* Set up SSL, TLS and authenticate with password
* Send a sample email with just text
* Send an email with text and attachment
* References:
    * Sending Email with Python: [https://stackabuse.com/how-to-send-em...](https://stackabuse.com/how-to-send-emails-with-gmail-using-python/)
    * Send email using Python: [https://www.geeksforgeeks.org/send-ma...](https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/)
    * Environment variables on Replit: [https://docs.replit.com/programming-i...](https://docs.replit.com/programming-ide/workspace-features/secrets)
    * [https://docs.aws.amazon.com/lambda/la... ](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)
    * Update Google sheets using Python:[ https://www.analyticsvidhya.com/blog/...
](https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/)https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/

important

Locating by XPath
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
</html>

</mark>login_form = driver.find_element(By.XPATH, "/html/body/form[1]")</mark>
</mark>login_form = driver.find_element(By.XPATH, "//form[1]")</mark>
</mark>login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")</mark>
<mark>username = driver.find_element(By.XPATH, "//form[input/@name='username']")</mark>
<mark>username = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]")</mark>
<mark>username = driver.find_element(By.XPATH, "//input[@name='username']")</mark>
<mark>clear_button = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")</mark>
<mark>clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")</mark>

Locating Hyperlinks by Link Text
<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
</html>
<mark>continue_link = driver.find_element(By.LINK_TEXT, 'Continue')</mark>
<mark>continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')</mark>


Locating Elements by CSS Selectors

<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
</html>
The “p” element can be located like this:
<mark>content = driver.find_element(By.CSS_SELECTOR, 'p.content')</mark>
