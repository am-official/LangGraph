# Serving and deployment
A10 exports a compiled graph and includes a loopback-only HTTP server plus langgraph.json. Run the local functional endpoint and verify an actual request. A manifest, PID, health check, or open port alone does not prove the application behavior.

Graphs describe computation. Deployments host graph code and runtime configuration. Revisions identify deployed versions. Assistants configure graph behavior. Threads hold continuing state, and runs represent executions. Do not substitute one object's ID for another's responsibility.

A real deployment also needs authenticated ingress, resource limits, durable shared storage, secrets management, concurrency policy, health/readiness probes, operational telemetry, and a rollback strategy. The local examples create none of those cloud resources automatically.

Postgres checkpoint/store backends can be appropriate for shared deployments, but require their own supported package versions, credentials, migrations, network access, backups, and failure testing. No Postgres or managed cloud deployment was validated here. Rehearse migrations against saved histories before changing persistent schemas.
