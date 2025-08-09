# **Prefect Deployment Setup**

**0. Set the dockerfile for requested packages and everything:**
<br/> First, you need to set dockerfile for any other packages. If you are not do this, you can not import custom libraries which does not exist in default base image like **prefect-github**

**1. Docker Compose Up:**
docker compose up -d <br/> 
docker compose logs -f prefect-server <br/>

**2. Set Prefect API URL:**
export PREFECT_API_URL=http://localhost:4200/api <br/>
prefect config set PREFECT_API_URL=http://localhost:4200/api <br/> 

**3. Check Connection:**
curl http://localhost:4200/api/health<br/> 

**4. Create Work Pool and Worker:** <br/>
prefect work-pool create my-pool --type process <br/>
prefect work-pool ls<br/>

## 4.1 Run Worker with nohup
prefect worker start --pool my-pool <br/>
nohup prefect worker start --pool my-pool > worker.log 2>&1 & <br/>

**5. Deactivate Everything:**
pkill -f "prefect worker" <br/>
docker compose down -v <br/>

**6. How it works in Prefect3?**

Remember it works like this as per my understanding: we need workpools and workers, in this workpools, workers run the code like following: tasks->flows. But for this, we need deployments.
<br/>
For every deployment, we need to specify worker. I do not exacly know how can I do this with code but I found out from UI. 

This code block: 
```
    from prefect import flow
    from main import main

    @flow(log_prints=True, persist_result=True)
    def market_prices_flow():
        main()

    if __name__ == "__main__":
        market_prices_flow.serve(name="market-prices-deployment", tags=["market-prices"], interval=1800) # 30 minutes in seconds
```
<br/>
After I run this with same environment with prefect deployment, It will run automatically even if the actual code within different directory. 
<br/>
**Please not that this is not the best practice, I will configure this with github and then update the file. Nobody wants to push every flow.py file into prefect directory.**
<br/>
There are many methods for deployments but in my codebase, I need github configuration. 
<br/>


**Addition:** I created a venv but it should not be required. Somehow without venv, I can not run it. That's why I created it. 
<br/>