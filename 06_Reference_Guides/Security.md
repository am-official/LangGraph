# Identity and data boundaries
Authentication verifies the actor; authorization determines whether that actor may use a resource or action. A thread ID, namespace, model-generated tool name, UI role selector, or successfully parsed token payload is not sufficient authorization.

A11 signs and verifies an ephemeral local token to teach signature and expiry checks. It is not a production identity provider. A12 filters tenant records before graph execution; production must supply verified claims rather than a user-selected tenant string.

Keep secrets in ignored environment configuration and inspect presence rather than values. Redact sensitive trace data before constructing/exporting records. Hashes verify byte integrity only against the expected digest; they do not establish authenticity unless the digest's provenance is trusted.

The labs do not execute arbitrary generated code. Production code execution requires a suitable verified isolation boundary, not merely a timeout. Privacy, retention, and role policy need their own tests and operational ownership.
