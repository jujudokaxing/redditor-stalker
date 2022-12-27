import praw
import datetime

# token
reddit = praw.Reddit(client_id = '',
					client_secret = '', 
					username = '',
					password = '',
					user_agent = '',)

def get_date(submission):
	time = submission.created
	d = datetime.datetime.fromtimestamp(time)
	d = str(d)
	return d


while True: 
	print('Username')
	st = input('>>> ')
	reddituser = reddit.redditor(str(st))
	posts_user = reddituser.submissions.new(limit=None)

	user_posts = []
	subreddit_dump = []
	temp_list_subm = []

	print('\n\n')
	print(str(reddituser) + '  ' + ' Total Karma: ' + str(reddituser.total_karma))
	print('\n')

	for submissions in posts_user:
		temp_list_subm.append(submissions)
		subreddit_dump.append(submissions.subreddit)

	ints_list = subreddit_dump
	ints_list1 = list(set(ints_list))
	print('\tTotal Posts: ' + str(len(temp_list_subm)))
	print('\tActive Subreddits ('+  str(len(ints_list1)) + ') :  ', end='')
	for g in ints_list1:
		print(str(g) + ', ', end='')

	print('\n\n----------------------\nPosts: \n')

	for submission in temp_list_subm:
		print(get_date(submission), end='')
		print('\t' + str(submission.subreddit))
		print('\t\t\t' + str(submission.title))
		print('\n')

	print('\n----------------------\n\n')
