import tkinter as tk
import tkinter.messagebox as messagebox
import datetime as datetime
import pandas as pd
import os


def approve_generated_tweets():
    in_file = e1.get()
    out_file = e2.get()
    # do validation of fields, and response to error...
    if (os.path.exists(in_file) & os.path.exists(out_file)):
        print("In file: %s\nOut File: %s" % (in_file, out_file))
        with open(in_file, 'r') as f:
            lines = f.read()
            f.close
        slines = lines.split("\n\n")
        i = 0
        for l in slines:
            # print(l+"\n===========\n")
            char_list = [l[j]
                         for j in range(len(l)) if ord(l[j]) in range(65536)]
            tweet = ''
            for j in char_list:
                tweet = tweet+j
            # tk.Label(master, text=tweet).grid(row=i,column=2)
            # tk.Button(master, text="keep", command=keep_tweet).grid(row=i,column=3)
            #tk.Button(master, text="kill", command=kill_tweet).grid(row=i,column=4)
            answer = messagebox.askquestion("is this a valid question", tweet)
            if answer == 'yes':
                #print("keep this tweet "+tweet)
                keep_tweet(tweet, out_file)
            i = i+1
            print(i)
            # if i >= 10:
            #     break
        f = open(in_file, 'w')
        f.write("")
        f.close()
    else:
        messagebox.showerror(title="file paths do not exist",
                             message="One of the input/output files does not exist at the described path")


def keep_tweet(tweet, out_file):
    print("keep clicked")
    print(tweet)
    df = pd.read_csv(out_file)
    curr_tweets = pd.read_csv(out_file)
    curr_tweets = curr_tweets.append({'category': 0, 'question': tweet,
                                      'expiration': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}, ignore_index=True)
    curr_tweets.to_csv(out_file, index=False)


master = tk.Tk()
tk.Label(master,
         text="Input File").grid(row=0)
tk.Label(master,
         text="Output File").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Start', command=approve_generated_tweets).grid(row=3,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)

tk.mainloop()
