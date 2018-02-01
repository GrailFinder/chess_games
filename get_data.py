import pgn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import uuid


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
    split_timecontrol(df)

    df.whiteelo = pd.to_numeric(df.whiteelo, errors='coerce')
    df.blackelo = pd.to_numeric(df.blackelo, errors='coerce')

    #df.dropna(inplace=True)

    me_black = df.loc[df.black == playername]
    me_white = df.loc[df.white == playername]

    return me_black, me_white, df

def split_timecontrol(df):
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.split.html
    df[['timecontrol_base', 'increment']] = df.timecontrol.str.split('+', expand=True)
    df.timecontrol_base = pd.to_numeric(df.timecontrol_base, errors='coerce')
    df.increment = pd.to_numeric(df.increment, errors='coerse')
    return df

def show_events(df):

    events = df.groupby('event')['opening'].count()

    events = events[events > 1]

    ax = events.plot(kind='barh', x=range(len(events)))
    for i in ax.patches:
        ax.text(i.get_width()+.1, i.get_y()+.31, \
            str(round((i.get_width()), 2)), fontsize=6, color='dimgrey')
    plt.tight_layout()
    plt.savefig(path_to_img + f'/events{str(uuid.uuid1())}.png')
    #plt.show()
    plt.cla()

def show_openings(df, color='black'):
    opens = df.groupby('opening')[color].count()

    opens = opens.drop_duplicates()
    opens = opens[opens > 1]

    ax = opens.plot(kind='barh', x=range(len(opens)))
    for i in ax.patches:
        ax.text(i.get_width()+.1, i.get_y()+.1, \
            str(round((i.get_width()), 2)), fontsize=6, color='dimgrey')
    plt.tight_layout()
    plt.savefig(path_to_img + f'/opening{str(uuid.uuid1())}.png')
    #plt.show()
    plt.cla()

def show_timecorr(df):
    splot = sns.swarmplot(x="result", y="timecontrol_base", hue='increment', data=df)
    fig = splot.get_figure()
    fig.savefig(path_to_img + f'/timecorr{str(uuid.uuid1())}.png')
    #plt.show()
    plt.cla()


def check_create_dir(path='./img'):
    os.makedirs(path, exist_ok=True)

if __name__ == '__main__':

    path_to_img = './img'

    check_create_dir(path=path_to_img)

    gd_black, gd_white, gd_both = make_dfs(filename='lichess_grossmendPro_2018-01-30.pgn', playername='grossmendPro')
    me_black, me_white, me_both = make_dfs(filename='lichess_GrailFinder_2018-01-30.pgn', playername='GrailFinder')


    show_openings(me_black)
    show_openings(me_white)

    show_events(me_both)

    # show_timecorr(me_black)
    # show_timecorr(me_white)
