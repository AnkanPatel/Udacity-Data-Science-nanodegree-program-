import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    input:
        categories_filepath - path of the categories csv 
        messages_filepath -path of the messages csv d
    output:
        df - the dataframe after concatenation of both the message and categories 
                csv files
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, how='left', on='id')
    
    return df

def clean_data(df):
    '''
    input:df:merged dataset in previous step.
    output:df:Cleaned dataset
    '''
    categories = df['categories'].str.split(pat=';', expand=True)
    
    row = categories.iloc[0,:]
    
    category_colname= row.apply(lambda x: x[:-2])
    
    categories.columns = category_colname
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(int)
    #dropping categoriescolumn    
    categories = categories.clip(0,1)
    df.drop('categories', axis=1, inplace=True)
    #concatinating df and categories together
    df = pd.concat((df, categories), axis=1)
    df.drop_duplicates(inplace=True)
    #after cleaning
    return df

def save_data(df, database_filepath):
    """
     input:
        df -the disaster messages dataframe
        database_filepath - the path to store the SQLite database
    """
    engine = create_engine('sqlite:///' + database_filepath)
    conn = engine.connect()
    df.to_sql('Final_Messages', engine, index=False, if_exists='replace')
    conn.close()

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()