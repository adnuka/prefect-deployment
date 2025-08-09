# **Prefect Deployment Setup**

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

**Addition:** I created a venv but it should not be required. Somehow without venv, I can not run it. That's why I created it. <br/>