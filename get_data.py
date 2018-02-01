import pgn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_dfs(filename, playername):

    pgn_text = open(filename).read()
    pgn_game = pgn.PGNGame()

    dat = pgn.loads(pgn_text) # Returns a list of PGNGame
    sdat = pgn.dumps(pgn_game) # Returns a string with a pgn game


    f_g = dat[0]

    games = list()

    for game in dat:
        keys = [key for key in dir(game) if not '_' in key]
        game_dict = dict()
        for key in keys:
            game_dict[key] = game.__getattribute__(key)
        games.append(game_dict)

    df = pd.DataFrame(games)


    df.whiteelo = pd.to_numeric(df.whiteelo, errors='coerce')
    df.blackelo = pd.to_numeric(df.blackelo, errors='coerce')

    #df.dropna(inplace=True)

    me_black = df.loc[df.black == playername]
    me_white = df.loc[df.white == playername]

    return me_black, me_white, df


def show_events(df):

    black_events = df.groupby('event')['opening'].count()
    print(type(black_events))

    print(black_events.index.values)

    black_events.plot(kind='barh', x=range(len(black_events)))
    plt.show()

def show_openings(df, color='black'):
    black_events = df.groupby('opening')[color].count()
    print(type(black_events))

    black_events = black_events.drop_duplicates()
    print(black_events)

    black_events.plot(kind='barh', x=range(len(black_events)))
    plt.tight_layout()
    plt.show()

def show_corr(df):
    #df.timecontrol = pd.to_numeric(df.timecontrol, errors='coerce')
    print(df.timecontrol)
    sns.swarmplot(x="result", y="opening", data=df)
    plt.show()

gd_black, gd_white, gd_both = make_dfs(filename='lichess_grossmendPro_2018-01-30.pgn', playername='grossmendPro')
me_black, me_white, me_both = make_dfs(filename='lichess_GrailFinder_2018-01-30.pgn', playername='GrailFinder')

show_openings(gd_black)
show_openings(gd_white)

show_openings(me_black)
show_openings(me_white)

# show_corr(me_both)
# show_corr(gd_both)