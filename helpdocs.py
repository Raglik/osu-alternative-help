import discord

def help(arg=None):
    embed = discord.Embed(colour=0xcc5288)
#Default Help page
    if arg == None:
        embed.title = "Help"
        embed.description = "Request help for a specific command using !help command-name and help for filters can be requested using !help parameters."
        embed.add_field(name = "Global Stats:", value = """
        `a_ranks`
        `clears`
        `gold_s`
        `gold_ss`
        `hitsperplay`
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
        embed.add_field(name = "Beatmap Lists:", value = """
        `first_fc_list`
        `first_ss_list`
        `least_fced`
        `least_ssed`
        `neverbeenfced`
        `neverbeenssed`
        `unique_fc_list`
        `unique_ss_list`
        """,inline = True)        
        embed.add_field(name = "Advanced:", value = """
        `getscores`
        `query`
        `queue`
        `scorequeue`
        `uploadscores`
        """,inline = True)
        embed.add_field(name = "PP:", value = """
        `pp`
        `pp_fun`
        `ppv1`
        `ppv1_unstable`
        `totalpp`
        """,inline = True)
        embed.add_field(name = "Custom:", value = """
        `first_fc`
        `first_ss`
        `ss_bounty`
        `tragedy`
        `unique_ss`
        """,inline = True)
        embed.add_field(name = "Beatmap:", value = """
        `beatmaps`
        `beatmapsets`
        `maxscore`
        `most_static`
        `nomodscore`
        `toprated`
        `worst_acc`
        """,inline = True)       
        embed.add_field(name = "Project Beatmaps:", value = """
        `projectdemetori`
        `projectdragonforce`
        `projecthitogata`
        `projectsao`
        `projecttouhou`
        `projectXYZ`
        """,inline = True)        
        embed.add_field(name = "Project 2021:", value = """
        `firstmap`
        `stats`
        `update`
        `weekly`
        `yeartodate`
        """,inline = True)        
        embed.add_field(name = "General Stats:", value = """
        `fc_count`
        `oldestnumberone`
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
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
        ```""", inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-o: leaderboard option in multi-purpose commands
-letter: X XH SH S A B C D
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true / false
-order: od, ar, cs, length, approved_date
-direction: desc, asc
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-year: specify a year
-time: minimum interval between rank date and play date
-filter: specify a year or a difficulty range if applicable
-country: specify a country using the ISO 2 letter code
-unplayed: true/false
        ```""", inline = False)
        embed.add_field(name="Beatmap parameters", value="""```ahk
-ar-min, -od-max, -cs-min, -length-max, etc: map parameters
-tags: queue a subset of maps with given tags
-title: queue a subset of maps with a given title
-mapper: queue a subset of maps with a given mapper name
-artist: queue a subset of maps with a given artist name
        ```""", inline = False)

#Global Stats commands

    elif arg == "a_ranks":
        embed.title = "!a_ranks"
        embed.description = "Total A rank leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")  
```""",inline=False)

    elif arg == "clears":
        embed.title = "!clears"
        embed.description = "Clears leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""", inline=False)

    elif arg == "gold_s":
        embed.title = "!gold_s"
        embed.description = "Golden S leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "gold_ss":
        embed.title = "!gold_ss"
        embed.description = "Golden SS leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "hitsperplay":
        embed.title = "!hitsperplay"
        embed.description = "Hitsperplay leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "playcount":
        embed.title = "!playcount"
        embed.description = "playcount leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "playtime":
        embed.title = "!playtime"
        embed.description = "playtime leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "silver_s":
        embed.title = "!silver_s"
        embed.description = "Silver S leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "silver_ss":
        embed.title = "!silver_ss"
        embed.description = "Silver SS leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "totalhits":
        embed.title = "!totalhits"
        embed.description = "Total hits leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code  
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit  
-p: specify the resulting page to output  
-u: specify a user (For a space in the username, use "+")  
```""",inline=False)

    elif arg == "total_s":
        embed.title = "!total_s"
        embed.description = "Total S leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "total_ss":
        embed.title = "!total_ss"
        embed.description = "Total SS leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Score commands

    elif arg == "fcscore":
        embed.title = "!fcscore"
        embed.description = "Scores only on maps a player has FCed"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "notfcscore":
        embed.title = "!notfcscore"
        embed.description = "Scores only on maps a player has not FCed"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "przegranyscore":
        embed.title = "!przegranyscore"
        embed.description = "Score only on maps Przegrany has played when he finished the game. (August 11th, 2021)"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "rankedscore":
        embed.title = "!rankedscore"
        embed.description = "Ranked score leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
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
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "scoresquared":
        embed.title = "!scoresquared"
        embed.description = "the square root of the sum of the square of every play "
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "scorev0":
        embed.title = "!scorev0"
        embed.description = "Simulates how the score ranking system worked before pp existed."
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "ssscore":
        embed.title = "!ssscore"
        embed.description = "Scores only on maps a player has SSed"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "totalscore":
        embed.title = "!totalscore"
        embed.description = "Total score leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code
-filter: specify a year or a difficulty range if applicable
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "weightedscore":
        embed.title = "!weightedscore"
        embed.description = "Ranked score leaderboard if it was weighted like pp"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "xasumascore":
        embed.title = "!xasumascore"
        embed.description = "Score only on maps xasuma has played when he finished the game. (April 28th, 2019)"
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#Beatmap lists commands

    elif arg == "first_fc_list":
        embed.title = "!first_fc_list"
        embed.description = "Generates a list of first fcs. User lists may be inaccurate."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "first_ss_list":
        embed.title = "!first_ss_list"
        embed.description = "Generates a list of first ss's. User lists may be inaccurate."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
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
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "least_ssed":
        embed.title = "!least_ssed"
        embed.description = "Returns a list of beatmaps ordered by their SS count (starts at 0)."
        embed.add_field(name="Command parameters", value="""```ahk
-ss-min: minimum amount of FC count  
-ss-max: maximum amount of FC count
```""",inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "neverbeenssed":
        embed.title = "!neverbeenssed"
        embed.description = "Returns a list of maps that have never been SSed that are at least 30 days old."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "neverbeenfced":
        embed.title = "!neverbeenfced"
        embed.description = "Returns a list of maps that have never been FCed that are at least 7 days old."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
```""",inline=False)

    elif arg == "unique_fc_list":
        embed.title = "!unique_fc_list"
        embed.description = "Generates a list of maps which only have 1 FC."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

    elif arg == "unique_ss_list":
        embed.title = "!unique_ss_list"
        embed.description = "Generates a list of maps which only have 1 SS."
        embed.add_field(name="Optional parameters", value="""```ahk
-order: od, ar, cs, length, approved_date
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
        ```""", inline = False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit
-p: specify the resulting page to output
-u: specify a user (For a space in the username, use "+")
```""",inline=False)

#incomplete query command as a first test

    elif arg == "query":
        embed.title = "!query"
        embed.description = "**Description:** Allows for precise star rating filtering on typical leaderboards for registered users"
        embed.add_field(name="Command parameters", value="""```ahk
-o: score, completion
-status: sliderbreak
```""", inline=False)
        embed.add_field(name="Optional parameters", value="""```ahk
-is_ss,-is_fc,-is_ht,-is_dt,-is_hr and etc. : true / false
-letter: X XH SH S A B C D
-min: minimal star rating of maps to include (inclusive)
-max: maximal star rating of maps to include (exclusive)
-start: earliest rank date of maps to include
-end: latest rank date of maps to include
-country: specify a country using the ISO 2 letter code
-year: specify a year
```""", inline=False)

#return the generated embed to bot
    return embed