# API compatibility
Use Python 3.12 and the pinned root lock for the tested environment. The labs execute StateGraph, Command, Send, interrupt, savers, Runtime context, ToolNode, RetryPolicy, CachePolicy, and the functional API against installed packages. ToolNode is executed inside a compiled graph because the installed version requires graph runtime context.

Optional trace export uses the installed LangSmith SDK's tracing writer and modern v2 readback. Account behavior and managed deployments were not live-verified. Official documentation hosts were blocked, so installed signatures/source and executable tests provide the API evidence recorded here.

Windows/macOS launch and CI are configured but not claimed successful before those workflows run. Root locks are for Python 3.12. Per-lab requirements are standalone; no parent source import is required.
