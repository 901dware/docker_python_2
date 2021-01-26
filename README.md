## Thanks for reviewing!

---

1. Clone this repository
   
2. Create `env` file in the project directory from `env.example`
```json
AWS_DEFAULT_REGION=us-east-1
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
QUEUE_NAME=test-queue
PUMP_INTERVAL=3
WEBHOOK_URL=https://webhook.site/f054fb31-23b1-4479-918b-d71abf95e227
```
Please put correct information.

3. Build Docker image
> docker image build -t docker_python .

4. Run Docker image
>docker run -it --env-file=env docker_python
