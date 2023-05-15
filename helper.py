from urlextract import URLExtract
from wordcloud 
extractor = URLExtract()



def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df =df[df['user']  == selected_user]

    #if selected_user == 'Overall':
    # 1. fetch number of meassage 
    num_messages =df.shape[0]
     #  2. fetch number of words
    words=[]
    for message in df['message']:
            
            words.extend(message.split())
           
    num_media_messages = df[df['message']=='<Media omitted>\n '].shape[0]
    links = []
    for message in df ['message']:
            links.extend(extractor.find_urls(message))
    return num_messages ,len(words) ,num_media_messages , len(links)


'''------------------------------------------------- Graph vala----------------------------------------------'''
def most_busy_users(df):
    x= df['user'].value_counts().head()

    df = round((df['user'].value_counts() / df.shape[0]) * 100 , 2).reset_index().rename(
          columns = { 'index ': ' name'  , 'user': 'percent'})
    return x , df


    
         

       
        

    '''if selected_user == 'Overall':

        # 1. fetch number of meassage  
        num_messages=df.shape[0]

         #  2. fetch number of words
        words=[]
        for message in df['message']:
            words.extend(message.split())



        return num_messages ,len(words)
    

    
    else:
        new_df = df[df['user']==selected_user]
        num_messages = new_df.shape[0]
        words = []
        for message in new_df['message']:
            words.extend(message.split())

        return num_messages ,len(words)
    
    '''
