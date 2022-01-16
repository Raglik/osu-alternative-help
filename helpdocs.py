import discord

def help(arg=None):
    embed = discord.Embed(colour=0xcc5288)
    if arg != None:
        arg = arg.lower();
#Default Help page
    if arg == None:
        embed.title = "Help"
        embed.description = "Request help for a specific command using !help command-name and help for filters can be requested using !help parameters."
        embed.add_field(name = "Global Stats:", value = """
`a_ranks`
`clears`
`gold_s`
`gold_ss`
`playcount`
`playtime`
`silver_s`
`silver_ss`
`totalhits`
`total_s`
`total_ss`
""",inline = True)
        embed.add_field(name = "Score:", value = """
`fcscore`
`notfcscore`
`przegranyscore`
`rankedscore`
`scorepersecond`
`scoresquared`
`scorev0`
`ssscore`
`totalscore`
`weightedscore`
`xasumascore`
        """,inline = True)        
        embed.add_field(name = "Custom Beatmap Lists:", value = """
`first_fc_list`
`first_ss_list`
`least_fced`
`least_ssed`
`neverbeendted`
`neverbeenfced`
`neverbeenssed`
`unique_fc_list`
`unique_ss_list`
""",inline = True)        
        embed.add_field(name = "Advanced:", value = """
`getscores`
`missingscore`
`query`
`queue`
`scorequeue`
""",inline = True)
        embed.add_field(name = "PP:", value = """
`fcpp`
`pp`
`pp_fun`
`totalpp`
""",inline = True)
# add back to the field when they work again        
#`ppv1`
#`ppv1_unstable`
        embed.add_field(name = "Custom:", value = """
`first_fc`
`first_ss`
`ss_bounty`
`tragedy`
`unique_fc`
`unique_ss`
""",inline = True)
        embed.add_field(name = "Beatmap:", value = """
`beatmaps`
`beatmaplist`
`beatmapsets`
`maxscore`
`most_static`
`nomodscore`
`toprated`
`worst_acc`
""",inline = True)     
#        embed.add_field(name = "Project Beatmaps:", value = """
# `projectdemetori`
# `projectdragonforce`
# `projecthitogata`
# `projectsao`
# `projecttouhou`
# `projectXYZ`
# """,inline = True)        
        embed.add_field(name = "Project 2022:", value = """
`firstmap`
`update`
`weekly`
`yeartodate`
""",inline = True)        
        embed.add_field(name = "Other Stats:", value = """
`fc_count`
`followers`
`hitsperplay`
`most_medals`
`oldestnumberone`
`replayswatched`
`top1s`
`top50s`
""",inline = True)            
        embed.add_field(name = "Mapper:", value = """
`mapsranked`
`setsranked`
""",inline = True)
        embed.add_field(name = "Miscellaneous:", value = """
`generatecollection`
`generateosdb`
`getfile`
`register`
""",inline = True)

#List of all parameters

    elif arg == "parameters":
        embed.title = "!help parameters"
        embed.description = "A list of parameters used in commands"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-o: leaderboard option in multi-purpose commands
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true/false
-replay: true/false
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-pp-min: minimal pp to include (inclusive)
-pp-max: maximal pp to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
-filter: specify a year or a difficulty range if applicable
-country: specify a country using the ISO 2 letter code
-unplayed: true/false
-tragedy: 100, 50, x, miss
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)

#Global Stats commands

    elif arg == "a_ranks":
        embed.title = "!a_ranks"
        embed.description = "Total A rank leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")  
```""",inline=False)

    elif arg == "clears":
        embed.title = "!clears"
        embed.description = "Clears leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "gold_s":
        embed.title = "!gold_s"
        embed.description = "Golden S leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "gold_ss":
        embed.title = "!gold_ss"
        embed.description = "Golden SS leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "playcount":
        embed.title = "!playcount"
        embed.description = "playcount leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "playtime":
        embed.title = "!playtime"
        embed.description = "playtime leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "silver_s":
        embed.title = "!silver_s"
        embed.description = "Silver S leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "silver_ss":
        embed.title = "!silver_ss"
        embed.description = "Silver SS leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "totalhits":
        embed.title = "!totalhits"
        embed.description = "Total hits leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code  
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit  
-p: specify the resulting page to output  
-u: specify a user (For a space in the username, use "+")  
```""",inline=False)

    elif arg == "total_s":
        embed.title = "!total_s"
        embed.description = "Total S leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "total_ss":
        embed.title = "!total_ss"
        embed.description = "Total SS leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Score commands

    elif arg == "fcscore":
        embed.title = "!fcscore"
        embed.description = "Scores only on maps a player has FCed"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "notfcscore":
        embed.title = "!notfcscore"
        embed.description = "Scores only on maps a player has not FCed"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "przegranyscore":
        embed.title = "!przegranyscore"
        embed.description = "Score only on maps Przegrany has played when he finished the game. (August 11th, 2021)"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "rankedscore":
        embed.title = "!rankedscore"
        embed.description = "Ranked score leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "scorepersecond":
        embed.title = "!scorepersecond"
        embed.description = "Score per second"
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)  
-max: maximal star rating of maps to include (exclusive)  
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-year: specify a year  
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "scoresquared":
        embed.title = "!scoresquared"
        embed.description = "the square root of the sum of the square of every play "
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "scorev0":
        embed.title = "!scorev0"
        embed.description = "Simulates how the score ranking system worked before pp existed."
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "ssscore":
        embed.title = "!ssscore"
        embed.description = "Scores only on maps a player has SSed"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "totalscore":
        embed.title = "!totalscore"
        embed.description = "Total score leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "weightedscore":
        embed.title = "!weightedscore"
        embed.description = "Ranked score leaderboard if it was weighted like pp"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "xasumascore":
        embed.title = "!xasumascore"
        embed.description = "Score only on maps xasuma has played when he finished the game. (April 28th, 2019)"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Beatmap lists commands

    elif arg == "first_fc_list":
        embed.title = "!first_fc_list"
        embed.description = "Generates a list of first fcs. User lists may be inaccurate."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "first_ss_list":
        embed.title = "!first_ss_list"
        embed.description = "Generates a list of first ss's. User lists may be inaccurate."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "least_fced":
        embed.title = "!least_fced"
        embed.description = "Returns a list of beatmaps ordered by their FC count (starts at 0)."
        embed.add_field(name="Command parameters", value="""```ahk
-fc-min: minimum amount of FC count  
-fc-max: maximum amount of FC count
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "least_ssed":
        embed.title = "!least_ssed"
        embed.description = "Returns a list of beatmaps ordered by their SS count (starts at 0)."
        embed.add_field(name="Command parameters", value="""```ahk
-ss-min: minimum amount of SS count  
-ss-max: maximum amount of SS count
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "neverbeendted":
        embed.title = "!neverbeendted"
        embed.description = "Returns a list of maps that have never been DTed."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "neverbeenfced":
        embed.title = "!neverbeenfced"
        embed.description = "Returns a list of maps that have never been FCed that are at least 7 days old."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "neverbeenssed":
        embed.title = "!neverbeenssed"
        embed.description = "Returns a list of maps that have never been SSed that are at least 30 days old."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "unique_fc_list":
        embed.title = "!unique_fc_list"
        embed.description = "Generates a list of maps which only have 1 FC."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "unique_ss_list":
        embed.title = "!unique_ss_list"
        embed.description = "Generates a list of maps which only have 1 SS."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Advanced commands

    elif arg == "getscores":
        embed.title = "!getscores"
        embed.description = "Returns maps in the database for a user based on specific criteria."
        embed.add_field(name="Command parameters", value="""```ahk
-status: Returns the amount of beatmaps based on the specified criteria
        • sliderbreak, miss, ss
        status in conjuction with -mods 1
        • 1,1.06,1.12,1.19,1.25,1.33,1.41
-mods 1: Returns the amount of beatmaps based on the mod score (use in conjunction -status)
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true/false
-replay: true/false
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-pp-min: minimal pp to include (inclusive)
-pp-max: maximal pp to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-unplayed: true/false
-tragedy: 100, 50, x, miss
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "missingscore":
        embed.title = "!missingscore"
        embed.description = "Returns an ordered list of plays based on how much score you're msising compared to the #1 play on the map."
        embed.add_field(name="Command parameters", value="""```ahk
-o: nomodscore
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true/false
-replay: true/false
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-unplayed: true/false
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "query":
        embed.title = "!query"
        embed.description = "Allows for precise star rating filtering on typical leaderboards for registered users"
        embed.add_field(name="Command parameters", value="""```ahk
-o: score, completion, pp, totalpp
-status: sliderbreak
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true/false
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-pp-min: minimal pp to include (inclusive)
-pp-max: maximal pp to include (exclusive)
-playcount-min: minimum amount of playcount to include (inclusive)
-playcount-max: maximum amount of playcount to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-direction: desc, asc
-country: specify a country using the ISO 2 letter code
-registered: true/false
-tragedy: 100, 50, x, miss
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)
        embed.add_field(name="Example", value="""```ahk
!query -u RonaldMcDonald -is_ss true -letter X -max 5 -start 2015-01-01 -end 2016-01-01 -ar-max 10 -tags %reol% -title no_title -mapper vinxis -year 2015
```""",inline=False)

    elif arg == "queue":
        embed.title = "!queue"
        embed.description = "Queues up a player for a full check of a specified set of beatmaps. Please use extensive parameters to limit the set. \
                                              Maximum amount of scores a user is allowed to queue is 1000. To check the queue time, use !queuelength."
        embed.add_field(name="Optional parameters", value="""```ahk
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true/false
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-unplayed: true/false
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-u: specify a user (For a space in the username, use "+")
```""",inline=False)
        embed.add_field(name="Example", value="""```ahk
!queue -u Kilgar -is_fc true -min 1 -max 2 -tags %dnb%liquicity% -mapper strategas -artist mage -year 2021 -length-max 300 -start 2021-01-01 -end 2022-01-01 -unplayed true
```""",inline=False)

    elif arg == "queuelength":
        embed.title = "!queuelength"
        embed.description = "Checks how long the !queue will take."

    elif arg == "scorequeue":
        embed.title = "!scorequeue"
        embed.description = "Queues up a single beatmap for a single player."
        embed.add_field(name="Command parameters", value="""```ahk
-b: Which beatmap id to check
-u: Which user id to check
```""",inline=False)
        embed.add_field(name="Example", value="""```ahk
!scorequeue -u Kilgar -b 75
```""",inline=False)

#PP commands
    elif arg == "fcpp":
        embed.title = "!fcpp"
        embed.description = "Weighing pp plays based on how many FCs there are, how popular the map is, and how hard the map is and ignoring mods"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "pp":
        embed.title = "!pp"
        embed.description = "Performance Points leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "pp_fun":
        embed.title = "!pp_fun"
        embed.description = "PP leaderboards with only specific types of maps."
        embed.add_field(name="Command parameters", value="""```ahk
-o: Operation to perform. Defaults to count
        • MARATHONS: MARATHON MAPS ONLY (10 minute+ maps)
        • NOMOD: NOMOD SCORES ONLY
        • ANIMEBAN: NO ANIME
        • NOSHORTMAP: NO SHORT MAPS
        • LONGMAPSONLY: LONGS MAPS ONLY
        • HIDDEN: HIDDEN ONLY
        • NODTNOHR NO DT NO HR
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#    elif arg == "ppv1":
#        embed.title = "!ppv1"
#        embed.description = "The first performance point system leaderboards; however, the algorithm is not public knowledge \
#                                              so it is just a rough guess of how it worked."
#        embed.add_field(name="Global parameters", value="""```ahk
#-l: specify how many results to output. Beware the 4000 character limit
#-p: specify the resulting page to output
#-u: specify a user (For a space in the username, use "+")
#```""",inline=False)

#    elif arg == "ppv1_unstable":
#        embed.title = "!ppv1_unstable"
#        embed.description = "The first performance point system leaderboards; however, the algorithm is not public knowledge \
#                                              so it is just a rough guess of how it worked and pp values are not inflated."
#        embed.add_field(name="Global parameters", value="""```ahk
#-l: specify how many results to output. Beware the 4000 character limit
#-p: specify the resulting page to output
#-u: specify a user (For a space in the username, use "+")
#```""",inline=False)


    elif arg == "totalpp":
        embed.title = "!totalpp"
        embed.description = "PP Leaderboard if PP wasn't weighted."
        embed.add_field(name="Required parameters", value="""```ahk
-filter: Specify a year (use full for every year)
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Custom commands

    elif arg == "first_fc":
        embed.title = "!first_fc"
        embed.description = "Generates a leaderboard of first fcs. May be inaccurate."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-country: Specify a country using the ISO 2 letter code
-time: minimum interval between rank date and play date

```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "first_ss":
        embed.title = "!first_ss"
        embed.description = "Generates a leaderboard of first ss's. May be inaccurate."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-country: Specify a country using the ISO 2 letter code
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "ss_bounty":
        embed.title = "!ss_bounty"
        embed.description = "For each first ss a player has, they get the number of days between rank date and play date added to their total."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-country: Specify a country using the ISO 2 letter code
-time: minimum interval between rank date and play date
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "tragedy":
        embed.title = "!tragedy"
        embed.description = "Leaderboard for the most players who scored 1 of the parameters."
        embed.add_field(name="Command parameters", value="""```ahk
-o: 100, 50, miss, x
• 100: 1x100 only score for an SS
• 50: 1x50 only score for an SS
• miss: 1 miss only score for an SS
• x: 1 miss only score for an FC
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "unique_fc":
        embed.title = "!unique_fc"
        embed.description = "Generates a leaderboard of players who have the only FC on maps."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-country: Specify a country using the ISO 2 letter code
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "unique_ss":
        embed.title = "!unique_ss"
        embed.description = "Generates a leaderboard of players who have the only SS on maps."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-country: Specify a country using the ISO 2 letter code
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Beatmap commands

    elif arg == "beatmaps":
        embed.title = "!beatmaps"
        embed.description = "Returns statistics of a set of beatmaps"
        embed.add_field(name="Command parameters", value="""```ahk
-o: Operation to perform. Defaults to count of every beatmap
        • count: Returns the amount of beatmaps fitting the criteria
        • length: Returns the total length of beatmaps fitting the criteria
-mode: 0 = standard, 1 = taiko, 2 = ctb, 3 = mania. Defaults to 0
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)

    elif arg == "beatmaplist":
        embed.title = "!beatmaplist"
        embed.description = "Lists every osu! standard map."
        embed.add_field(name="Command parameters", value="""```ahk
-mode: 0 = standard, 1 = taiko, 2 = ctb, 3 = mania. Defaults to 0
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-order: score, length, approved_date, accuracy, ar, od etc.
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "beatmapsets":
        embed.title = "!beatmapsets"
        embed.description = "Returns statistics of beatmap sets"
        embed.add_field(name="Command parameters", value="""```ahk
-o: Operation to perform. Defaults to count of every beatmap
        • count: Returns the amount of beatmap sets that fit the criteria
        • length: Returns the total length of beatmap sets that fit the criteria
-mode: 0 = standard, 1 = taiko, 2 = ctb, 3 = mania. Defaults to 0
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-length-min, -length-max
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)

    elif arg == "maxscore":
        embed.title = "!maxscore"
        embed.description = "Outputs the sum of the best play on each map contained in the filter."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
```""",inline=False)

    elif arg == "most_static":
        embed.title = "!most_static"
        embed.description = "Returns maps in the database with the least amount of movement in the top 50 leaderboard. (Currently Broken)"
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)

    elif arg == "nomodcore":
        embed.title = "!nomodscore"
        embed.description = "Outputs the sum of the best nomod play on each map contained in the filter."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
```""",inline=False)

    elif arg == "toprated":
        embed.title = "!toprated"
        embed.description = "Returns maps in the database with the highest user ratings"
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)

    elif arg == "worst_acc":
        embed.title = "!worst_acc"
        embed.description = "Returns maps in the database for the worst acc on the global leaderboards."
        embed.add_field(name="Optional parameters", value="""```ahk
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-direction: desc, asc
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
```""",inline=False)

#Project Beatmap Commands

    elif arg == "projectdemetori":
        embed.title = "!projectdemetori"
        embed.description = "Leaderboard for maps tagged with Demetori."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "projectdragonforce":
        embed.title = "!projectdragonforce"
        embed.description = "Leaderboard for maps tagged with Dragonforce."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "projecthitogata":
        embed.title = "!projecthitogata"
        embed.description = "Leaderboard for the 50 diff mapset known as Hitogata sung by HIMEHINA and hosted by Ryuusei Aika featuring 49 different mappers excluding Ryuusei \
                             including: bossandy, -Nanako-, Niva, Firika, deetz, Narcissu, lv9, Beomsan, Present, Starfy, papple104, - Frontier -, semaphore, Lami, Trynna, \
                             Ujimatcha, rui, Frey, jonathanlfj, LMT, -ClariS-, appleeaterx, tomadoi, -Nanaka-, AIR, z1085684963, CoLouRed GlaZeE, ScubDomino, Silky, moph, \
                             Necho, Kalibe, Shizuku-, kanor, Len, irotuk, contagious, melloe, Bariton, xLolicore-, Regou, Luscent, Yusomi, Jounzan, Yugu, ak74, val0108, \
                             -[Pino]- and Taeyang."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "projectsao":
        embed.title = "!projectsao"
        embed.description = "Leaderboard for maps tagged with the hit anime sensation Sword Art Online."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "projecttouhou":
        embed.title = "!projecttouhou"
        embed.description = "Leaderboard for maps tagged with touhou."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "projectXYZ":
        embed.title = "!projectXYZ"
        embed.description = "Specific star rating range leaderboards."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
-v: 5.00, 6.00 (use in conjunction with -o)
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "projectdemetori":
        embed.title = "!projectdemetori"
        embed.description = "Leaderboard for maps tagged with demetori."
        embed.add_field(name="Command parameters", value="""```ahk
-o: ss, fc, clears, score
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Project 2021 commands

    elif arg == "firstmap":
        embed.title = "!firstmap"
        embed.description = "Returns the first beatmap set of a given week."
        embed.add_field(name="Command parameters", value="""```ahk
-w: The week to output. Defaults to this week
```""",inline=False)

    elif arg == "update":
        embed.title = "!update"
        embed.description = "Refresh bot output for Project 2022 commands."

    elif arg == "weekly":
        embed.title = "!weekly"
        embed.description = "Returns a leaderboard for one week in project 2022."
        embed.add_field(name="Command parameters", value="""```ahk
-o: Leaderboard type. ss, fc, clears, plays, score
-w: The week to output. Defaults to this week
-u: User to lookup (optional)
```""",inline=False)

    elif arg == "yeartodate":
        embed.title = "!yeartodate"
        embed.description = "Returns a leaderboard for the entirety of project 2022."
        embed.add_field(name="Command parameters", value="""```ahk
-o: Leaderboard type. fc, clears, plays, score, ss, s, silver_s, gold_s, etc
-u: User to lookup (optional)
-o: Beatmap difficulty filter. easy, normal, hard, insane, extra, extreme
```""",inline=False)

#Other stats command

    elif arg == "fc_count":
        embed.title = "!fc_count"
        embed.description = "Total FC counts for users"
        embed.add_field(name="Required parameters", value="""```ahk
-filter: Specify a year (use full for every year)
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "followers":
        embed.title = "!followers"
        embed.description = "Followers count leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-rankedscore: min. score for a user to be on the board
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "hitsperplay":
        embed.title = "!hitsperplay"
        embed.description = "Hitsperplay leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-playcount-min: minimum amount of playcount to include (inclusive)
-playcount-max: maximum amount of playcount to include (exclusive)
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "most_medals":
        embed.title = "!most_medals"
        embed.description = "Medal count leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-rankedscore: min. score for a user to be on the board
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "oldestnumberone":
        embed.title = "!oldestnumberone"
        embed.description = "oldest number ones <user ID> | <beatmap ID>"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "top1s":
        embed.title = "!top1s"
        embed.description = "Global #1 leaderboards"
        embed.add_field(name="Required parameters", value="""```ahk
-filter: Specify a year (use full for every year)
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "top50s":
        embed.title = "!top50s"
        embed.description = "Top 50 global leaderboards."
        embed.add_field(name="Required parameters", value="""```ahk
-filter: Specify a year (use full for every year)
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Mapper commands

    elif arg == "mapsranked":
        embed.title = "!mapsranked"
        embed.description = "Returns a leaderboard for the most difficulties ranked by a mapper."
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "setsranked":
        embed.title = "!setsranked"
        embed.description = "Returns a leaderboard for the most sets ranked by a mapper."
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-direction: desc, asc
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Miscellaneous commands

    elif arg == "generatecollection":
        embed.title = "!generatecollection"
        embed.description = "Uses the specified filters to create an osu collection. Best imported using collection manager."
        embed.add_field(name="Command parameters", value="""```ahk
-o: External information to include to the dataset (neverbeenssed, neverbeenfced, status, mods)
-status: used in conjunction with -o status or -o mods, allows for the same filtering as !getscores
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true / false
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-rank: number of rank #
-unplayed: true/false
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "generateosdb":
        embed.title = "!generateosdb"
        embed.description = "Uses the specified filters to create an osu collection. Best imported using collection manager."
        embed.add_field(name="Command parameters", value="""```ahk
-o: External information to include to the dataset (neverbeenssed, neverbeenfced, status, mods)
-status: used in conjunction with -o status or -o mods, allows for the same filtering as !getscores
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true / false
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-rank: number of rank #
-unplayed: true/false
```""",inline=False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
-diff: queue a subset of maps with a given difficulty name
```""",inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 4000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "getfile":
        embed.title = "!getfile"
        embed.description = "Returns the entire list in a file, if discord allows it."
        embed.add_field(name="Command parameters", value="""```ahk
-type: List to fetch. neverbeenssed, neverbeenfced
```""",inline=False)

    elif arg == "register":
        embed.title = "!register"
        embed.description = "Registers a player for more frequent updates"
        embed.add_field(name="Required parameter", value="""```ahk
Username or user id if username does not work
```""",inline=False)
        embed.add_field(name="Example", value="""```ahk
!register 8967040 or !register Kilgar
```""",inline=False)

#Secret Commands

    elif arg == "help":
        embed.title = "!help"
        embed.description = "Command for seeing every command"
        embed.add_field(name="Command parameter", value="""```ahk
See !help for list of commands
```""",inline=False)

    elif arg == "streamin":
        embed.title = "!streamin"
        embed.description = "stinks"

    elif arg == "me":
        embed.title = "no"

    elif arg == "you":
        embed.title = "no"

    elif arg == "!!":
        embed.title = "!!"
        
    elif arg == "abababa":
        embed.color=0xc85050 
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/653927651618193428.gif?size=96")

    elif arg == "kilgar":
        embed.color=0xc85050 
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/931703750983299072.webp?size=96&quality=lossless")
#return the generated embed to bot
    return embed

def save(arg=None):
    embed = discord.Embed(colour=0xcc5288)
    if arg != None:
        arg = arg.lower();
    if arg == "None":
        embed.title = "who"
    else:
        embed.title = "no"
    return embed