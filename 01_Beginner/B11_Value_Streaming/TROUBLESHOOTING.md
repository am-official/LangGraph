# Troubleshooting
| Symptom | Diagnosis and action |
|---|---|
| Import error | Install requirements with the same interpreter used to run Streamlit and pytest. |
| Invalid JSON | Use double quotes, arrays/objects as shown in samples, and no trailing commas. |
| Input rejected | Read the explicit length, numeric, role, or state constraint in the error and run function. |
| Resume rejected | Use the same thread/key and the documented action. A completed job is not a pending interrupt. |
| Version conflict | Reload current state before retrying; do not overwrite another writer silently. |
| Old result appears | Run the form again after changing inputs; Reset results clears only displayed evidence. |
| Theme absent | Launch from this folder so .streamlit/config.toml is loaded. |
| Port occupied | Add --server.port 8502 to the Streamlit command. |
| Cloud permission error | Confirm account access and secure configuration; do not expose keys or disable TLS. |

The lab inspects collected stream events; it does not claim incremental model-token delivery. Local timing is not a load test. Cloud feature behavior and Windows/macOS launch are separate verification boundaries.
