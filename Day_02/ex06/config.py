file_path = 'data.csv'
num_of_step = 3
report = "Report We have made {} observations from tossing a coin: {} of them were tails and {} of them were heads." + \
"The probabilities are {:.2f}% and {:.2f}%, respectively. Our forecast is that in the next {} observations we will have: {} tail and {} heads."
save_file = 'report'
log_file = 'analytics.log'
logging_format = '%(asctime)s %(message)s'
slack_webhook = None
success = 'The report has been successfully created'
fail = 'The report hasn’t been created due to an error'