import json
import polars as pl

def create_csv(df, columns, file_name):
    df_selected = df.select(columns)
    df_selected.write_csv(f'page_data/{file_name}')

def create_json(df, columns, file_name):
    df_selected = df.select(columns)
    df_dicts = df_selected.to_dicts()
    json_data = json.dumps(df_dicts, indent=2)
    with open(f"page_data/{file_name}.json", "w") as f:
        f.write(json_data)



def main():
    df = pl.read_csv('det_tools.csv')
    columns = ['name','isOpenSource','pageUrl','category','logo','shortDescription']
    create_csv(df,columns,'home.csv')
    columns = ['pageUrl','name','category','description','logo','getStarted','EITMLI18','url','useCases','isOpenSource']
    create_json(df,columns,'tools')


if __name__ == '__main__':
    main()
