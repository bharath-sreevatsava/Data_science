from fastapi import FastAPI
from covid import covid_analysis_module
app = FastAPI()

@app.get('/')
def covid_analysis():
    df = covid_analysis_module()
    print(df)
    return {"output" : df.to_dict('dict')}
