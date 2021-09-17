# Porter

## Description
Discord bot for Animal Crossing: New Horizons

![Porter Output](https://i.imgur.com/CTOacEV.png)

Utilises the [ACNH RESTful API](http://acnhapi.com/)

## Commands

Prefix for all commands is `p!`

* `p!fish {fish_name}`: Get information about the specified fish
* `p!bug {bug_name}`: Get information about the specified bug


## Installation

**Installation via requirements.txt**

```shell
$ cd porter
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

## Configuration

For Porter to run, a .env file must be created in the root of the directory with the following variables.

```
# .env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-server-name}
```

`{your-bot-token}` can be obtained through the [Discord Developer Portal](https://discord.com/developers/applications), and `{your-server-name}` is the name of the Discord server you want Porter to join.

## Execution

**Running the application**

With the virtual environment activated:

````shell
$ py -3 bot.py
```` 
