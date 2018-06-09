import os
from bs4 import BeautifulSoup
import requests

class Updater:
	BASE_URL = "https://rocketleague.tracker.network"

	def __init__(self, team_url):
		self.stats = {}
		self.team_url = team_url

	def get_team(self):
		team = {}

		page = requests.get(self.BASE_URL + self.team_url)
		soup = BeautifulSoup(page.content, 'html.parser')

		members = soup.find('table', { 'id': 'team-members' })
		team['members'] = []
		for member in members.find_all('td', { 'class': 'details' }):
			anchor = member.find('a')

			name = anchor.text.strip()
			link = anchor['href']

			team['members'].append({ 'name': name, 'link': link })

		return team

	def update_members(self, members):
		count = len(members)

		print "Updating %d members..." % count
		for idx, member in enumerate(members):
			try:
				url = self.BASE_URL + member['link']
				print "[%d/%d] Update player '%s', url: %s" % (idx + 1, count, member['name'], url)

				res = requests.get(url) # TODO: get stats?
				res.raise_for_status()
			except requests.HTTPError as e:
				print "Updating failed, %s" % e

		print "Updating completed"

def env_var(name):
	var = os.getenv(name)
	if not var:
		raise ValueError("missing required environment variable '%s'" % name)
	return var

if __name__ == "__main__":
	team_url = env_var('TEAM_URL')

	updater = Updater(team_url)
	team = updater.get_team()
	updater.update_members(team['members'])