# PICR

`PICR` means `Progressive Indexed Context Retrieval`.

## Principle

An LLM should not load full detailed instructions before proving they are needed.

## Flow

1. parse the task
2. consult a short catalog
3. select a domain catalog
4. rank candidates
5. read only the chosen item
6. execute
7. record outcome

## Minimal Components

- primary catalog
- domain catalogs
- router
- on-demand reader
- memory log

## Benefits

- lower token cost
- lower latency
- less noise
- better repeatability
- easier portability across models and CLIs
