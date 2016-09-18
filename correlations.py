import master

### ALL ELECTIONS ###
elections = [
	{"year": 2012, "winner": "Barack Obama", "loser": "Mitt Romney"},
	{"year": 2008, "winner": "Barack Obama", "loser": "John McCain"},
	{"year": 2004, "winner": "George W. Bush", "loser": "John Kerry"},
	{"year": 2000, "winner": "George W. Bush", "loser": "Al Gore"},
	{"year": 1996, "winner": "Bill Clinton", "loser": "Bob Dole"},
	{"year": 1992, "winner": "Bill Clinton", "loser": "George H.W. Bush"},
	{"year": 1988, "winner": "George H.W. Bush", "loser": "Michael Dukakis"}
	# {"year": 1984, "winner": "Ronald Reagan", "loser": "Walter Mondale"},
	# {"year": 1980, "winner": "Ronald Reagan", "loser": "Jimmy Carter"},
	# {"year": 1976, "winner": "Jimmy Carter", "loser": "Gerald Ford"},
	# {"year": 1972, "winner": "Richard Nixon", "loser": "George McGovern"},
	# {"year": 1968, "winner": "Richard Nixon", "loser": "Hubert Humphrey"},
	# {"year": 1964, "winner": "Lyndon B. Johnson", "loser": "Barry Goldwater"},
	# {"year": 1960, "winner": "John F. Kennedy", "loser": "Richard Nixon"},
	# {"year": 1956, "winner": "Dwight D. Eisenhower", "loser": "Adlai Stevenson"},
	# {"year": 1952, "winner": "Dwight D. Eisenhower", "loser": "Adlai Stevenson"},
	# {"year": 1948, "winner": "Harry Truman", "loser": "Thomas E. Dewey"},
	# {"year": 1944, "winner": "Franklin D. Roosevelt", "loser": "Thomas E. Dewey"}
]

candidates = [
	### WINNERS ###
	{"name": "Barack Obama", "party": "D", "won": True},
	{"name": "George W. Bush", "party": "R", "won": True},
	{"name": "Bill Clinton", "party": "D", "won": True},
	{"name": "George H.W. Bush", "party": "R", "won": True},
	# {"name": "Ronald Reagan", "party": "R", "won": True},
	# {"name": "Jimmy Carter", "party": "D", "won": True},
	# {"name": "Richard Nixon", "party": "R", "won": True},
	# {"name": "Lyndon B. Johnson", "party": "D", "won": True},
	# {"name": "John F. Kennedy", "party": "D", "won": True},
	# {"name": "Dwight D. Eisenhower", "party": "R", "won": True},
	# {"name": "Harry S. Truman", "party": "D", "won": True},
	# {"name": "Franklin D. Roosevelt", "party": "D", "won": True},
	### LOSERS ###
	{"name": "Mitt Romney", "party": "R", "won": False},
	{"name": "John McCain", "party": "R", "won": False},
	{"name": "John Kerry", "party": "D", "won": False},
	{"name": "Al Gore", "party": "D", "won": False},
	{"name": "Bob Dole", "party": "R", "won": False},
	{"name": "Michael Dukakis", "party": "D", "won": False}
	# {"name": "Walter Mondale", "party": "D", "won": False},
	# {"name": "George McGovern", "party": "D", "won": False},
	# {"name": "Hubert Humphrey", "party": "D", "won": False},
	# {"name": "Barry Goldwater", "party": "R", "won": False},
	# {"name": "Adlai Stevenson", "party": "D", "won": False},
	# {"name": "Thomas E. Dewey", "party": "R", "won": False}
]

def getPath(query, name):
	# This is a stub
	return master.main(query, name)

def pastElectionInfo(query):
	# check to see if query is valid
	if False:
		return 0
	# for each candidate, get path
	paths = []
	for candidate in candidates:
		thisPath = getPath(query, candidate["name"])
		paths.append({"name": candidate["name"], "avg": thisPath["avg"], "path": thisPath["path"]})
	demrepStats = {"avgDemPath": 0, "avgRepPath": 0}
	winloseStats = {"avgWinPath": 0, "avgLosePath": 0}
	dems = 0
	reps = 0
	wins = 0
	losses = 0
	for path in paths:
		for candidate in candidates:
			if candidate["name"] == path["name"]:
				if candidate["party"] == "R":
					demrepStats["avgRepPath"] += path["avg"]
					reps += 1
				else:
					demrepStats["avgDemPath"] += path["avg"]
					dems += 1
				if candidate["won"]:
					winloseStats["avgWinPath"] += path["avg"]
					wins += 1
				else:
					winloseStats["avgLosePath"] += path["avg"]
					losses += 1
				break
	demrepStats["avgDemPath"] /= dems
	demrepStats["avgRepPath"] /= reps
	winloseStats["avgWinPath"] /= wins
	winloseStats["avgLosePath"] /= losses
	return {"partyStats": demrepStats, "winStats": winloseStats}

if __name__ == "__main__":
    print pastElectionInfo("girl scout cookies")
