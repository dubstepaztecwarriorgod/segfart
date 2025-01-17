import discord

JESS = 688488105418031142

def is_british(user: discord.Member) -> bool:
    return any(role.name == 'british (ew)' for role in user.roles) or user.id == JESS

def get_token() -> str:
    try:
        return open("token.txt").read()
    except FileNotFoundError:
        print("Retard only I HAVE THE SECRET TOKEN FILE KUAHAHAHAHAH")
    except:
        print("Not very sigma")
    