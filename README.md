# **Prefect Deployment Setup**

**1. Docker Compose Up:**
docker compose up -d
docker compose logs -f prefect-server

**2. Set Prefect API URL:**
export PREFECT_API_URL=http://localhost:4200/api
prefect config set PREFECT_API_URL=http://localhost:4200/api

**3. Check Connection:**
curl http://localhost:4200/api/health

**4. Create Work Pool and Worker:**
prefect work-pool create my-pool --type process
prefect work-pool ls

## 4.1 Run Worker with nohup
prefect worker start --pool my-pool
nohup prefect worker start --pool my-pool > worker.log 2>&1 &

**5. Deactivate Everything:**
pkill -f "prefect worker"
docker compose down -v

**Addition:** I created a venv but it should not be required. Somehow without venv, I can not run it. That's why I created it. 