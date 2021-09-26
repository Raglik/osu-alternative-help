import discord

def help(arg=None):
    embed = discord.Embed(colour=0xcc5288)
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
        `queuelength`
        `scorequeue`
        `uploadscores`
        `uploadqueue`
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
```""", inline=True)
    elif arg == "totalhits":
        embed.title = "!totalhits"
        embed.description = "Total hits leaderboard"
        embed.add_field(name="Optional parameters", value="""```ahk
-country: specify a country using the ISO 2 letter code  
-filter: specify a year or a difficulty range if applicable  
```""", inline=False)
        embed.add_field(name="Global parameters", value="""```ahk
-l: specify how many results to output. Beware the 2000 character limit  
-p: specify the resulting page to output  
-u: specify a user (if there is a space in the username, use `+`)  
```""",inline=False)
    return embed