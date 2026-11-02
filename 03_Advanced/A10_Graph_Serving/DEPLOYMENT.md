# Local functional endpoint
From this folder with dependencies installed:
```sh
python server.py --port 8124
```
POST JSON `{"request":"hello"}` to `/invoke`. Expect `{"request":"hello","answer":"Graph response: hello"}`. GET `/health` checks process readiness; it does not replace the functional request. An invalid body receives 400. The endpoint binds only to loopback and has no authentication; it is a local teaching service.

langgraph.json and the project metadata declare a compiled graph export for a later managed workflow. Copy .env.example to .env before using tooling that expects that file. Managed deployment requires its CLI/service, account access, secrets, durable backends, authorization, and live validation. No managed service is created by this example.
