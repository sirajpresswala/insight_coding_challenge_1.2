import pandas as pd, numpy as np, simplejson
import ast

rolling_median = []
looplist = [0]

df = pd.DataFrame(pd.read_csv(r'C:\Users\ADMIN\Documents\GitHub\insight_coding_challenge_1.2\input_file\venmo-trans.txt',header=None,index_col=None,sep=';',squeeze=True).apply(lambda x: ast.literal_eval(x)).tolist())
df['created_time'] = df['created_time'].astype(np.datetime64)

for i in looplist:
  try:
    df['seconds_gap'] = (df['created_time'] - df['created_time'].ix[i]).apply(lambda x: x.total_seconds())
    df1 = df[df['seconds_gap'] <= np.absolute(60.00)]
    df1 = df1[['actor','target']]
    for v in range(len(df1)):
      rolling_median.append(np.median(pd.melt(df1.ix[:v+1])['value'].value_counts().tolist()))
    df = df.ix[(v+1):].reset_index(drop = True)
    looplist.extend([0])
  except:
    pass

f = open(r'C:\Users\ADMIN\Documents\GitHub\insight_coding_challenge_1.2\output_file\coding_challenge_output.txt','w')
simplejson.dump(rolling_median,f)
f.close()

del df, df1, looplist, rolling_median
    
#comments:
# import libaries pandas, numpy, ast, simplejson
#rolling median is stored in list variable named 'rolling_median'
#looplist is the counter for the number of times the dataframe object is broken into smaller objects based on rolling 60 second window threshold
#import data file, convert data file into pandas DataFrame object
#column 'created_time' is converted into numpy datetime dtype object
#column 'seconds_gap' measures the time difference in seconds between the first record and subsequent records until the time difference exceeds 60 seconds....
#...at which point the loop breaks the bigger dataframe 'df' into smaller dataframe 'df1'
#run a second loop within the smaller dataframe 'df1' to compute rolling median and store the output into the rolling_median list object
#reset the dataframe object 'df1' so that the dataframe is resized to cut out the part of the dataframe for which the rolling median has been computed
# write the output (rolling_median) to text file using simplejson

  
  
    
