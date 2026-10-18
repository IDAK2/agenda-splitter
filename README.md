# Agenda Splitter

## The procedural problem

A single motion can hide several decisions. Voting on the bundle makes disagreement unreadable.

The clerk files one proposal beside independent agenda rules. GenLayer validators extract one to eight source-anchored questions, each with one action. The chair may adopt the split or request one same-origin revision. The clerk may withdraw before adoption. Stored digests keep the rules and motion snapshot attached to the agenda.

## Public safeguards

Questions must end as questions, carry distinct anchors, and remain within the bounded vector. Validators reproduce the whole vector rather than approving its shape. Adoption belongs to the chair; revision is limited to one; duplicate agenda IDs never overwrite history.

## Procedure check

```text
python -m pytest -q
genvm-lint lint contracts/contract.py
```
