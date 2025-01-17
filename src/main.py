import bot
from util import get_token

def main():
    client = bot.SegFartBot()
    client.run(get_token())

if __name__ == "__main__":
    main()