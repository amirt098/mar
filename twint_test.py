import twint

c = twint.Config()
c.Search = "Bitcoin"  # Specify your search term
c.Limit = 100         # Limit the number of tweets
c.Lang = "en"        # Language of the tweets

twint.run.Search(c)
